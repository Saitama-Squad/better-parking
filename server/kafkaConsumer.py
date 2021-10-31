from json import load
import joblib
from kafka import KafkaConsumer
import os
from dotenv import load_dotenv
from ast import literal_eval
import json
import numpy as np
import base64
from PIL import Image
import io
import matplotlib.pyplot as plt
import cv2
from skimage.transform import resize
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.base import BaseEstimator, TransformerMixin
from skimage.color import rgb2gray

load_dotenv()

class RGB2GrayTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
 
    def fit(self, X, y=None):
        return self
 
    def transform(self, X, y=None):
        return np.array([rgb2gray(img) for img in X])

def bytestojson(bytes):
    data = literal_eval(bytes.decode('utf8'))
    s = json.loads(json.dumps(data, indent=4, sort_keys=True))
    s["data"] = json.loads(s["data"])
    b64toimage(s["data"]["image"])

def b64toimage(b64):
    base64_decoded = base64.b64decode(b64)
    image = Image.open(io.BytesIO(base64_decoded))
    image_np = np.array(image)
    pred(image_np)

def pred(sample):
    ref = cv2.imread(os.path.join(os.getcwd(),'server', 'empty.jpg'))
    grayA = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    grayB = cv2.resize(sample,(130,200))
    grayB = cv2.cvtColor(grayB, cv2.COLOR_BGR2GRAY)
    grayA = cv2.resize(grayA,(130,200))
    print(grayA.shape,grayB.shape)
    diff = cv2.absdiff(grayB, grayA)
    ret, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    im = resize(thresh, (130, 200))
    grayify = joblib.load(os.path.join(os.getcwd(),'server','grayify.sav'))
    scalify = joblib.load(os.path.join(os.getcwd(),'server','scalify.sav'))
    pred_im = grayify.transform([im,])
    twodim = pred_im.reshape(1,-1)
    print(twodim.shape)
    prep_im = scalify.transform(twodim)
    sgd_clf = joblib.load(os.path.join(os.getcwd(),'server','savedmodel.sav'))
    y_pred = sgd_clf.predict(prep_im)
    print(y_pred)

bootstrap_kafka_servers = [
    os.environ.get('BROKER1'),
    os.environ.get('BROKER2'),
    os.environ.get('BROKER3'),
    os.environ.get('BROKER4'),
    os.environ.get('BROKER5'),
    os.environ.get('BROKER6')
]

print("Starting Connection")
consumer = KafkaConsumer('alldata',
                         bootstrap_servers=bootstrap_kafka_servers,
                         security_protocol='SASL_SSL',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username='username',
                         sasl_plain_password=os.environ.get('SASL_PASSWORD')
                         )
print("Connected!")
print(consumer.bootstrap_connected)

# Asynchronous by default
for message in consumer:
    print("Printing Message")
    bytestojson(message.value)
