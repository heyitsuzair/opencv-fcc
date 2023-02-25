import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')

blank = np.zeros(img.shape, dtype='uint8')

canny = cv.Canny(img, 125, 175)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Blank', blank)

cv.imshow('Cats', canny)
cv.waitKey(0)
