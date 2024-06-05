import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw shapes on the image
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # Blue diagonal line
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # Green rectangle
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)  # Red circle
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)  # Blue ellipse
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))


# Display the image
cv.imshow('image', img)

# Wait for a key press to close the window (optional)
cv.waitKey(0)
cv.destroyAllWindows()
