import cv2
import numpy as np

img1 = cv2.imread("../image/bitwise_refrence.jpg")
img2 = np.zeros((300,600, 3), np.uint8)
img2 = cv2.rectangle(img2, (200,0), (400,150), (255,255,255), -1)


bitwiseAnd = cv2.bitwise_and(img1, img2)
bitwiseOr = cv2.bitwise_or(img1, img2)
bitwiseXor = cv2.bitwise_xor(img2, img1)
bitwiseNot1 = cv2.bitwise_not(img1)
bitwiseNot2 = cv2.bitwise_not(img2)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

#cv2.imwrite('Example BitwiseAnd.jpg', bitwiseAnd)
#cv2.imwrite('Example BitwiseOr.jpg', bitwiseOr)
#cv2.imwrite('Example BitwiseXor.jpg', bitwiseXor)
#cv2.imwrite('Example BitwiseNot1.jpg', bitwiseNot1)
#cv2.imwrite('Example BitwiseNot2.jpg', bitwiseNot2)

cv2.imshow('Example BitwiseAnd', bitwiseAnd)
cv2.imshow('Example BitwiseOr', bitwiseOr)
cv2.imshow('Example BitwiseXor', bitwiseXor)
cv2.imshow('Example BitwiseNot1', bitwiseNot1)
cv2.imshow('Example BitwiseNot2', bitwiseNot2)


cv2.waitKey(0)
cv2.destroyAllWindows()
