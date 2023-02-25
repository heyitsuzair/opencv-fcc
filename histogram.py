import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/park.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

masked = cv.bitwise_and(img, img, mask=mask)


# Gray Histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])


# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# Of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color Histogram
colors = ('b', 'g', 'r')


plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# Of Pixels')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()
cv.imshow('Pic', mask)

cv.waitKey(0)
