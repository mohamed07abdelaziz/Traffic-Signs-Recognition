
import os
import cv2 as cv
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from skimage.exposure import histogram
from matplotlib.pyplot import bar
from skimage.color import rgb2gray,rgb2hsv
from skimage.filters import gaussian
from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from skimage.feature import hog
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from tqdm import tqdm
import random
# import imgaug.augmenters as iaa

# Convolution:
from scipy.signal import convolve2d
from scipy import fftpack
import math

from skimage.util import random_noise
from skimage.filters import median
from skimage.feature import canny
from skimage.measure import label
from skimage.color import label2rgb


# Edges
from skimage.filters import sobel_h, sobel, sobel_v,roberts, prewitt

# Show the figures / plots inside the notebook
def show_images(images,titles=None):
    #This function is used to show image(s) with titles by sending an array of images and an array of associated titles.
    # images[0] will be drawn with the title titles[0] if exists
    # You aren't required to understand this function, use it as-is.
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n)
        if image.ndim == 2: 
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show() 


def showHist(img):
    # An "interface" to matplotlib.axes.Axes.hist() method
    plt.figure()
    imgHist = histogram(img, nbins=256)
    
    bar(imgHist[1].astype(np.uint8), imgHist[0], width=0.8, align='center')

def histogram_eq(img):
    # a.
    G = 256
    H = np.zeros(G)
    
    # b.  histogram
    for pixel in img.flatten():
        H[int(pixel)] += 1
    
    # c. H_c
    H_c = np.cumsum(H)
    
    # d. Set the mapping between gray-levels
    N, M = img.shape
    T = np.round((G - 1) * H_c / (N * M))
    
    # e. Map the gray-levels in the output image
    img_eq = T[img]
    
    return img_eq
