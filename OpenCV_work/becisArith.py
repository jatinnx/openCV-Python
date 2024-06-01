import numpy as np 
import cv2 as cv

img = cv.imread('robinfranky.jpg')
img1 = cv.imread('1298937.jpg')

# print(img.shape)
# print(img.size)
# print(img.dtype) 
# b,g,r = cv.split(img)
# r[:] = 0
# img2 = cv.merge((b,g,r))
img = cv.resize(img, (512, 512))
img1 = cv.resize(img1, (512, 512))
img3 = cv.add(img1, img)
cv.imshow('image', img3)

cv.waitKey(0)
cv.destroyAllWindows()