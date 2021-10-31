import joblib
from matplotlib.colors import Colormap
from skimage.io import imread
from skimage.transform import resize
import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt
def resize_all(src, pklname, include, width=150, height=None):
    height = height if height is not None else width
    data = dict()
    data['description'] = 'resized ({0}x{1})  images in rgb'.format(int(width), int(height))
    data['label'] = []
    data['filename'] = []
    data['data'] = []   
     
    pklname = f"{pklname}_{width}x{height}px.pkl"
 
    # read all images in PATH, resize and write to DESTINATION_PATH
    for subdir in os.listdir(src):
        if subdir in include:
            print(subdir)
            current_path = os.path.join(src, subdir)
 
            for file in os.listdir(current_path):
                if file[-3:] in {'jpg', 'png'}:
                    ref = cv2.imread(os.path.join(src, 'empty.jpg'))
                    sample = cv2.imread(os.path.join(current_path, file))
                    grayA = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
                    grayB = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
                    diff = cv2.absdiff(grayB, grayA)
                    ret, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
                    im = resize(thresh, (height, width)) #[:,:,::-1]
                    data['label'].append(subdir)
                    data['filename'].append(file)
                    data['data'].append(im)
 
        joblib.dump(data, pklname)
    
data_path = './Images'
print(os.listdir(data_path))
base_name = 'pkl'
width = 130
height = 200
include = {'False','True'}
 
resize_all(src=data_path, pklname=base_name, width=width, height=height, include=include)
