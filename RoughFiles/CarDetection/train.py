from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import StandardScaler, Normalizer
import skimage
from skimage.transform import resize
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import joblib 
from sklearn.model_selection import train_test_split
from skimage.color import rgb2gray
import cv2
import os
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

class RGB2GrayTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
 
    def fit(self, X, y=None):
        return self
 
    def transform(self, X, y=None):
        return np.array([rgb2gray(img) for img in X])

def processing(src,sample):
    ref = cv2.imread(os.path.join(src, 'empty.jpg'))
    grayA = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(grayB, grayA)
    ret, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    dilated = cv2.dilate(thresh,kernel,iterations = 1)
    im = resize(dilated, (width, height))
    return im

grayify = RGB2GrayTransformer()
scalify = StandardScaler()

base_name = 'pkl'
width = 130
height = 200

data = joblib.load(f'{base_name}_{width}x{height}px.pkl')
X = np.array(data['data'])
y = np.array(data['label'])

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    shuffle=True,
    random_state=42,
)


X_train_gray = grayify.fit_transform(X_train)
dataset_size = len(X_train)
TwoDim_dataset = X_train_gray.reshape(dataset_size,-1)
print(TwoDim_dataset.shape)
X_train_prepared = scalify.fit_transform(TwoDim_dataset)

sgd_clf = SGDClassifier(random_state=42, max_iter=1000, tol=1e-3)
sgd_clf.fit(X_train_prepared, y_train)

#Testing

X_test_gray = grayify.transform(X_test)
dataset_size = len(X_test)
TwoDim_dataset_test = X_test_gray.reshape(dataset_size,-1)
print(TwoDim_dataset_test.shape)
X_test_prepared = scalify.transform(TwoDim_dataset_test)

y_pred = sgd_clf.predict(X_test_prepared)
print(np.array(y_pred == y_test)[:25])
print('')
print('Percentage correct: ', 100*np.sum(y_pred == y_test)/len(y_test))
ConfusionMatrixDisplay.from_predictions(y_test,y_pred)
plt.show()

filename = "savedmodel.sav"
joblib.dump(sgd_clf,filename)
