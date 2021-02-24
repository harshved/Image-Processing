import cv2

img = cv2.imread("../image/squirrel.jpg")

rectangledImg = cv2.rectangle(img,(120,100),(370,380),(0,0,255), 2)
cv2.imwrite("rectangledImg.jpg",rectangledImg)
cv2.imshow("Rect",rectangledImg)
