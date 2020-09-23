import cv2

img = cv2.imread("/Users/patrickromanescu/Desktop/us.jpeg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

inverted_blurred_img = 255 - blurred_image

pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)

cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_IMG)
cv2.waitKey(0)
