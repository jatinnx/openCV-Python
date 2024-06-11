import cv2 as cv
import numpy as np

# Callback function for trackbar (does nothing)
def nothing(x):
    pass  

# Create a window named 'tracking' for trackbars
cv.namedWindow("tracking")

# Create trackbars for red, blue, and green components
cv.createTrackbar('red', 'tracking', 0, 255, nothing)
cv.createTrackbar('blue', 'tracking', 0, 255, nothing)
cv.createTrackbar('green', 'tracking', 0, 255, nothing)

while True:
    # Read the image
    frame = cv.imread('colorball.jpg')

    # Check if the image is loaded successfully
    if frame is None:
        print("Error: Could not read image 'colorball.jpg'")
        break

    # Convert the image from BGR to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get current positions of the trackbars
    r = cv.getTrackbarPos('red', 'tracking')
    b = cv.getTrackbarPos('blue', 'tracking')
    g = cv.getTrackbarPos('green', 'tracking')

    # Create a BGR color based on the trackbar positions
    color = np.uint8([[[b, g, r]]])

    # Convert the BGR color to HSV
    hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)

    # Extract the HSV values
    h = hsv_color[0][0][0]
    s = hsv_color[0][0][1]
    v = hsv_color[0][0][2]

    # Define the lower and upper bounds for the HSV values
    l = np.array([h-10, 100, 100])  # Lower bounds (with tolerance)
    u = np.array([h+10, s, v])  # Upper bounds (with tolerance)

    # Create a mask based on the bounds
    mask = cv.inRange(hsv, l, u)

    # Apply the mask to the original frame
    res = cv.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and result
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    # Exit if the user presses the 'Esc' key
    key = cv.waitKey(1)
    if key == 27:
        break

# Destroy all windows created
cv.destroyAllWindows()
