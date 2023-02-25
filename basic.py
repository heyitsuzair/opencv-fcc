import cv2 as cv

img = cv.imread('photos/cat.jpg')
img2 = cv.imread('photos/park.jpg')

# Converting Gray Scale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat', gray)

# Blur Image
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Cat', blur)

# Edge Cascade
cany = cv.Canny(img2, 125, 175)
# cv.imshow('Park', cany)

# Dilating Image
dilated = cv.dilate(cany, (7, 7), iterations=1)
# cv.imshow('Park', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Park', eroded)

# Resize
resized = cv.resize(img2, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Park', resized)

# Crop
cropped = img[50:200, 200:400]
cv.imshow('Cat', cropped)
print(type(cropped))

cv.waitKey(0)
