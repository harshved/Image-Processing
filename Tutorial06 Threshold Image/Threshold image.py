import cv2

img = cv2.imread("../image/squirrel.jpg")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresholdImg = cv2.threshold(grayImg, 120, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("threshold.jpg",thresholdImg)

cv2.imshow("squirrel",img)
cv2.imshow("squirrelGray",grayImg)
cv2.imshow("squirrelThreshold",thresholdImg)

