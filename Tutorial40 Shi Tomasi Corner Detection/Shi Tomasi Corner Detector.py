import numpy as np
import cv2 as cv

img = cv.imread('../image/left12.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 120, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, [255, 0, 255], -1)

cv.imshow('Shi-Tomasi Corner Detector', img)
cv.imwrite('Shi-Tomasi Corner Detected.jpg', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
