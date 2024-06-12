import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture(0)

# Get frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Read the first two frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

if not ret:
    print("Failed to read video file or video file is corrupted")
    cap.release()
    cv2.destroyAllWindows()
    exit()

print(frame1.shape)

while cap.isOpened():
    # Compute the absolute difference between the two frames
    diff = cv2.absdiff(frame1, frame2)
    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Blur the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Threshold the blurred image
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # Dilate the thresholded image
    dilated = cv2.dilate(thresh, None, iterations=3)
    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Get the bounding box for each contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # Filter out small contours based on area
        if cv2.contourArea(contour) < 1500:
            continue

        # Filter based on aspect ratio to detect human-like shapes
        aspect_ratio = w / float(h)
        if 0.3 < aspect_ratio < 1.3:
            # Draw a rectangle around the detected contour
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)

    # Resize the frame for display
    image = cv2.resize(frame1, (1280, 720))
    frame1 = cv2.resize(frame1, (1280, 720))
    # Display the frame with contours
    cv2.imshow("feed", frame1)
    
    # Update frames
    frame1 = frame2
    ret, frame2 = cap.read()

    # Break the loop if 'Esc' key is pressed
    if cv2.waitKey(40) == 27 or not ret:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
