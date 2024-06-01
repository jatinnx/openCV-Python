import numpy as np
import cv2 as cv

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv.circle(img, (x,y), 3, (0,0,255), -1)
        mycolorImg = np.zeros([512,512,3], np.uint8)

        mycolorImg[:] = [blue, green, red]

        cv.imshow('color', mycolorImg)
        



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