import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/park.jpg')


# BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)

# BGR To HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)

# BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# HSV TO BGR
bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)

cv.imshow('Park', bgr)
# plt.imshow(rgb)
# plt.show()
cv.waitKey(0)
