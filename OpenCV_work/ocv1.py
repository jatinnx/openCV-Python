import cv2 as cv
import numpy as np

'''# img = cv.imread('robinfranky.jpg', 1)
img = np.zeros([512,512,3], np.uint8)
print(img)
img = cv.line(img, (0,0), (255,136), (0,127,255), 2)
img = cv.rectangle(img, (12,56),(510,234), (123,76,234), -1)
cv.imshow('image', img)'''

event = [i for i in dir(cv) if 'EVENT' in i]
print(event)
# print(np.zeros([5,5,3]))
cv.waitKey(0)
cv.destroyAllWindows()


