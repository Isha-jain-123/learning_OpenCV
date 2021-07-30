import cv2
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')      # to create a blank image
# cv.imshow('blank', blank)

# img = cv.imread('cat.jpg')
# cv.imshow('cat',img)

# 1. change the colour of the blank image
blank[:]=0,255,0
blank[200:300, 300:400] = 0, 0, 255  # to paint a certain region a certain color
# cv.imshow('green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0,0,255), thickness=2)
# cv.imshow('rectangle',blank)

# 3. Drawing a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)       # thickness=-1 will fill in the shape
# cv.imshow('circle',blank)

# 4. draw a line
# use cv.line

# 5. write text on the image
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('text',blank)

cv.waitKey(0)