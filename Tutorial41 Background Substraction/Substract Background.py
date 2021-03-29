import cv2

cap = cv2.VideoCapture('../image/vtest.avi')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.BackgroundSubtractorGMG() #This method needs kernal and morphologyEx function
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)#Make detectShadow to False if u don't want the shadow.
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)#Make detectShadow to False if u don't want the shadow.
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == ord('q') or keyboard == 27:
        break
cap.release()
cv2.destroyAllWindows()
