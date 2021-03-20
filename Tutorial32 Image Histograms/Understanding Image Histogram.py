import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../image/squirrel.jpg",)

cv2.imshow("img", img)

#To get colored histogram uncomment below code
#b, g, r = cv2.split(img)
#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
