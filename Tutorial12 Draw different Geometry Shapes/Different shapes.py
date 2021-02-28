import numpy as np
import cv2

img = np.zeros([650, 650, 4], np.uint8) #Used to get image with blackbackground

img = cv2.arrowedLine(img, (0,0), (255,255), (150, 96, 144), 10) # 44, 96, 147
img = cv2.line(img, (0,255), (255,255), (150, 150, 0), 10)
img = cv2.circle(img, (512, 190), 63, (0, 255, 255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Text', (250, 500), font, 2, (255, 0, 255), 6, cv2.LINE_AA)
img = cv2.ellipse(img,(512,256),(100,50),0,0,180,255,-1)


cv2.imshow('image', img)
cv2.imwrite('image.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows() 
