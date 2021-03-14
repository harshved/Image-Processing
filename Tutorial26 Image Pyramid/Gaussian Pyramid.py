import cv2
import numpy as np
img = cv2.imread("../image/squirrel.jpg")
layer = img.copy()
gaussianPyramidList = [layer]

#Every image is 1/4th part of belowed image
for i in range(5, 0, -1):
    layer = cv2.pyrDown(layer)
    gaussianPyramidList.append(layer)
    cv2.imshow("Image : " + str(i), layer)

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
