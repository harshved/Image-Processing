import cv2
import numpy as np

def nottodoanything(x):
    pass

cv2.namedWindow("Tracking")

cv2.createTrackbar("LowerHue", "Tracking", 0, 255, nottodoanything)
cv2.createTrackbar("LowerSaturation", "Tracking", 0, 255, nottodoanything)
cv2.createTrackbar("LowerValue", "Tracking", 0, 255, nottodoanything)

cv2.createTrackbar("UpperHue", "Tracking", 255, 255, nottodoanything)
cv2.createTrackbar("UppperSaturation", "Tracking", 255, 255, nottodoanything)
cv2.createTrackbar("UpperValue", "Tracking", 255, 255, nottodoanything)

while True:
    frame = cv2.imread('../image/opencv-logo.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LowerHue", "Tracking")
    l_s = cv2.getTrackbarPos("LowerSaturation", "Tracking")
    l_v = cv2.getTrackbarPos("LowerValue", "Tracking")

    u_h = cv2.getTrackbarPos("UpperHue", "Tracking")
    u_s = cv2.getTrackbarPos("UppperSaturation", "Tracking")
    u_v = cv2.getTrackbarPos("UpperValue", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
