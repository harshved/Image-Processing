import numpy as np
import cv2 as cv

def printValue(x):
    print(x)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, printValue)
cv.createTrackbar('G', 'image', 0, 255, printValue)
cv.createTrackbar('R', 'image', 0, 255, printValue)

switch = 'OFF\ON\n'
cv.createTrackbar(switch, 'image', 0, 1, printValue)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
       img[:] = 0
    else:
       img[:] = [b, g, r]


cv.destroyAllWindows()
