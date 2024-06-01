import numpy as np
import cv2 as cv

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 3, (0,89,190), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv.line(img,points[-1], points[-2], (25,0,0), 5)
        cv.imshow('image', img)

img = cv.imread('robinfranky.jpg')

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load image")
    exit()
points=[]
cv.imshow('image', img)
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()