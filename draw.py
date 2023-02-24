import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Black', blank)

# 1. Try To Paint Image a certain color
# blank[200:300,300:400] = 0, 0, 255
# cv.imshow('Green', blank)

# 2. Draw A Rectangle
# cv.rectangle(blank, (0, 0),
#              (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
# 3. Draw A Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
#           40, (0, 0, 255), thickness=-1)
# 4. Draw A Line
# cv.line(blank, (100, 250),
#         (300, 400), (255, 255, 255), thickness=3)
# 5. Write Text
cv.putText(blank, 'Hello World', (0, 255),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Blank', blank)
cv.waitKey(0)
