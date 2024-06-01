import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_RBUTTONDOWN:
        print(x, ', ', y)
        
        # strXY = str(x) + ', ' + str(y)
        
        cv.imshow('image', img)

    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0] 
        green = img[y, x, 1]
        red = img[y, x, 2] 
        font = cv.FONT_HERSHEY_COMPLEX
        strBGR = f"{str(blue)}, {str(green)}, {str(red)}"
        cv.putText(img, strBGR, (x, y), font, 1, (190, 145, 198), 2)
        cv.imshow('image', img)

# Load the image
img = cv.imread('robinfranky.jpg')

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load image")
    exit()

cv.imshow('image', img)
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()