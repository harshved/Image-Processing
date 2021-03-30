import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)#Make detectShadow to False if u don't want the shadow.
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)
    
    if cv2.waitKey(30) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
