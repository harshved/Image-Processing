import cv2 as cv
import numpy as np

img = cv.imread('../image/gradient.png',3)
_, thimg1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)#Covert Image below 100pixel to black and above it to white
_, thimg2 = cv.threshold(img, 170, 255, cv.THRESH_BINARY_INV)#Covert Image above 170pixel to black and below it to white
_, thimg3 = cv.threshold(img, 140, 255, cv.THRESH_TRUNC)#Covert Image above 140pixel to the point of color which it get at 140pixel
_, thimg4 = cv.threshold(img, 143, 255, cv.THRESH_TOZERO)#Convert Image below 143pixel to black and above it stay as it is
_, thimg5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)#Convert Image above 143pixel to black and below it stays as it is


cv.imshow("Image", img)
cv.imshow("th1", thimg1)
cv.imshow("th2", thimg2)
cv.imshow("th3", thimg3)
cv.imshow("th4", thimg4)
cv.imshow("th5", thimg5)

cv.waitKey(0)
cv.destroyAllWindows()
