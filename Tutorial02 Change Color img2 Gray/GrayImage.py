import cv2

img = cv2.imread("../image/squirrel.jpg")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("squirrelGrayImage.jpg",grayImg)

cv2.imshow("squirrel",img)
cv2.imshow("squirrelGrayImage",grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
