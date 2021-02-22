import cv2

img = cv2.imread("../image/squirrel.jpg")

print(img.shape)
print(img.size)
print(img.dtype)

#ExampleOutput is 
#(426, 535, 3) -> (Height, Width, Color-Channel(RGB))
#683730
#uint8
