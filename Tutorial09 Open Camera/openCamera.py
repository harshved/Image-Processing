import cv2
vision = cv2.VideoCapture(0)
while True:
    _,img = vision.read() #_ is paramter which is not required
    cv2.imshow("VideoStreaming", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vision.release()
cv2.destroyAllWindows()
