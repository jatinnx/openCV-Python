import cv2 as cv
import datetime as dt
print(cv.__version__)

# Initialize VideoCapture with the correct source
cap = cv.VideoCapture(0)  # 0 is typically the default webcam

if not cap.isOpened():  # This checks if the video capture source is successfully opened.
    print("Error: Could not open video source.")
    exit()

while True:
    ret, frame = cap.read() 

    if not ret:  # ret: A boolean indicating whether the frame was read successfully (True) or not (False).
        print("Error: Failed to read frame.")
        break

    # Mirror the frame horizontally
    frame = cv.flip(frame, 1)

    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Convert the color to gray
    font = cv.FONT_HERSHEY_COMPLEX
    datet = str(dt.datetime.now())
    cv.putText(frame, datet, (3,20), font, 1, (99,134,145), 1, cv.LINE_AA)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
