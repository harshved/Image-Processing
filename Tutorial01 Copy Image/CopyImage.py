import cv2

img = cv2.imread("squirrel.jpg")
cv2.imshow("squirrel",img)
cv2.imwrite("squirrelCopy.jpg",img)
cv2.imshow("squirrelCopy",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
