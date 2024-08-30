import cv2 as cv
import sys
import numpy as np
from matplotlib import pyplot as plt
import os

def function(alpha):
    new_canny = cv.Canny(blur,alpha,255)

    cv.imshow('slider',new_canny)

def corner_slider(details):
    detect_corner = cv.goodFeaturesToTrack(canny, 20, 0.01, recom_distance)
    raw_copy = raw.copy()
    if detect_corner is not None:
        detect_corner = np.int_(detect_corner)
        for corners in detect_corner:
            x,y = corners.ravel()
            cv.circle(raw_copy, (x,y), 4, 0, -1)

    cv.imshow("corner",raw_copy)

max_slider = 40
recom_distance = 21
title_window = "Corner detect Adjustment"

os.chdir('D:\Vscode_github\Detecting-Glyphs-underwater-1')
raw = cv.imread('glyph.png',cv.IMREAD_GRAYSCALE)

# bw = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)
if(raw is not None):
    print("you return")
    
    blur = cv.GaussianBlur(raw,(7,7),0)

    canny = cv.Canny(blur,255,255)

    # set= np.concatenate((bw,canny),axis=0)

    cv.namedWindow(title_window)
    trackbar_name = 'Details x %d' % max_slider
    cv.createTrackbar(trackbar_name, title_window, 1, max_slider, corner_slider)
        

cv.waitKey()
if(False):
    gradient = cv.Sobel(blur,cv.CV_64F,1,1,ksize= 3)

    thresh = cv.threshold(gradient,100,255,cv.THRESH_BINARY)

    cv.imshow("thresh", thresh)

# erosion_kern = np.ones((5,5), np.uint8)
# erode = cv.erode(bw, erosion_kern, iterations= 1)
# erode_blur = cv.erode(blur, erosion_kern, iterations= 1)

# dilate_kern = np.ones((5,5),np.uint8)
# dilation = cv.dilate(bw, dilate_kern, iterations= 1)
# dilation_blur = cv.dilate(blur, dilate_kern, iterations= 1)

# vert1 = np.concatenate((dilation,erode), axis=0)

# cv.waitKey(8000)
cv.destroyAllWindows()