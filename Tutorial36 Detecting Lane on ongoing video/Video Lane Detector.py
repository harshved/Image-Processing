import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    copied_img = np.copy(img)
    blank_image = np.zeros((copied_img.shape[0], copied_img.shape[1], 3), np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

def process_video(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]

    #for any other image you have to set your region of interest
    region_of_interest_vertices = [
        (100, height),
        (width/2, height/3),
        (width-50, height)
    ]

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #adjust the threshold value as per the image
    canny_image = cv2.Canny(gray_image, 250, 260)
    cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32),)

    lines = cv2.HoughLinesP(cropped_image,
                            rho=10,
                            theta=np.pi/360,
                            threshold=250,
                            lines=np.array([]),
                            minLineLength=80,
                            maxLineGap=80)
    image_with_lines = draw_the_lines(image, lines)
    return image_with_lines

cap = cv2.VideoCapture("2.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = process_video(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


