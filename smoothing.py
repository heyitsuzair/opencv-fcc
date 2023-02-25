import cv2 as cv

img = cv.imread('photos/cats.jpg')

# Averaging
average = cv.blur(img, (7, 7))

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)

# Median Blur
median = cv.medianBlur(img, 3)

# Bileteral
bileteral = cv.bilateralFilter(img, 10, 35, 25)

cv.imshow('Cats', bileteral)
cv.waitKey(0)
