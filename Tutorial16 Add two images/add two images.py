import numpy as np
import cv2

img1 = cv2.imread('../image/squirrel.jpg')
img2 = cv2.imread('../image/opencv-logo.png')

img1 = cv2.resize(img1, (480,480))
img2 = cv2.resize(img2, (480,480))

result = cv2.addWeighted(img1, .6, img2,  .4, 0)
cv2.imshow('Image', result)
cv2.imwrite('Resulted Image.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
