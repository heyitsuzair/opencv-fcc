import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # For Images, Videos And Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('photos/cat_large.jpg')
resized_img = rescaleFrame(img, 0.5)
cv.imshow('Cat', img)
cv.imshow('Cat-Resized', resized_img)
cv.imwrite('photos/cat_large_resized.jpg', resized_img)
cv.waitKey(0)

# def changeRes(width, height):
#     # Live Video
#     capture.set(3, width)
#     capture.set(4, height)

# capture = cv.VideoCapture('videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     frame_resized = rescaleFrame(frame, 0.2)

#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
