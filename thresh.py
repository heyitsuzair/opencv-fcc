import cv2 as cv

img = cv.imread('photos/cats.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Simple Threshold
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

# Adaptive Threshold
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)

cv.imshow('Adaptive', adaptive_thresh)
# cv.imshow('Threshed', thresh)
# cv.imshow('Threshed Inv', thresh_inv)
cv.waitKey(0)
