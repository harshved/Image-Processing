import cv2

img = cv2.imread("../image/squirrel.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gaussianImg = cv2.GaussianBlur(grayImg, (11,11), 0)
cv2.imwrite("GaussianBlur.jpg",gaussianImg)
cv2.imshow("GaussianBlur",gaussianImg)
