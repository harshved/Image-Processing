import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../image/gradient.png',0)
_, thimg1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)#Covert Image below 100pixel to black and above it to white
_, thimg2 = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)#Covert Image above 170pixel to black and below it to white
_, thimg3 = cv2.threshold(img, 140, 255, cv2.THRESH_TRUNC)#Covert Image above 140pixel to the point of color which it get at 140pixel
_, thimg4 = cv2.threshold(img, 143, 255, cv2.THRESH_TOZERO)#Convert Image below 143pixel to black and above it stay as it is
_, thimg5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)#Convert Image above 143pixel to black and below it stays as it is


titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thimg1 ,thimg2 ,thimg3 ,thimg4, thimg5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
