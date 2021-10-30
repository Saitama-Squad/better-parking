import numpy as np
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt
import cv2


def plot_bar(y, loc='left', relative=True):
    width = 0.35
    if loc == 'left':
        n = -0.5
    elif loc == 'right':
        n = 0.5
     
    # calculate counts per type and sort, to ensure their order
    unique, counts = np.unique(y, return_counts=True)
    sorted_index = np.argsort(unique)
    unique = unique[sorted_index]
     
    if relative:
        # plot as a percentage
        counts = 100*counts[sorted_index]/len(y)
        ylabel_text = '% count'
    else:
        # plot counts
        counts = counts[sorted_index]
        ylabel_text = 'count'
         
    xtemp = np.arange(len(unique))
     
    plt.bar(xtemp + n*width, counts, align='center', alpha=.7, width=width)
    plt.xticks(xtemp, unique, rotation=45)
    plt.xlabel('equipment type')
    plt.ylabel(ylabel_text)
 


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
"""
plt.suptitle('relative amount of photos per type')
plot_bar(y_train, loc='left')
plot_bar(y_test, loc='right')
plt.legend([
    'train ({0} photos)'.format(len(y_train)), 
    'test ({0} photos)'.format(len(y_test))
])
plt.show()
"""
"""
ref = cv2.imread('Images/empty.jpg')
sample = cv2.imread('Images/False/16.jpg')
grayA = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
diff = cv2.absdiff(grayB, grayA)
ret, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
kernel = np.ones((1,1),np.uint8)
dilated = cv2.dilate(thresh,kernel,iterations = 1)
plt.imshow(dilated, cmap = 'inferno')
plt.show()
"""
