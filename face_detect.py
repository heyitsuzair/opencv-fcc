import cv2 as cv

img = cv.imread('photos/group 1.jpg')

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=1)

print('No Of Faces Found', len(faces_rect))

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Image', img)
cv.waitKey(0)
