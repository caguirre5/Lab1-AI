import cv2
from PIL import Image
import numpy as np 

img = cv2.imread(".\Maze200x200.png")
quantized_img = cv2.pyrMeanShiftFiltering(img, 200, 10)
cv2.imwrite("quantized_image.jpg", quantized_img)

super_resolution = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
cv2.imwrite("super_resolution_image.jpg", super_resolution)

low_resolution = cv2.resize(img, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)

ret,thresh_img = cv2.threshold(low_resolution,150,255,cv2.THRESH_BINARY)


cv2.imwrite("low_resolution_image.jpg", low_resolution)
cv2.imwrite("Threshold_image.jpg", thresh_img)


mazeimg = Image.open(".\Threshold_image.jpg")
gray = mazeimg.convert('L')
arr = np.array(gray)

print(arr)