import cv2 as cv

# Reading images
# img = cv.imread('cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)     # wait for the user to press a key for infinite time

def rescaleFrame(frame, scale=0.75):
    # works on videos,pictures,live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # works only on live video
    capture.set(3,width)
    capture.set(4,height)

# Reading Videos
capture = cv.VideoCapture('doggy.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):        # if we press the key d , stop the video
        break

capture.release()
cv.destroyAllWindows()                         # close down the window

cv.waitKey(0)


