import cv2
import imutils

img = cv2.imread("../image/squirrel.jpg")
resizeImg = imutils.resize(img, width=260)

cv2.imwrite("resizedImage.jpg",resizeImg)
cv2.imshow("squirrel.jpg",img)
cv2.imshow("resizedImage",resizeImg)
