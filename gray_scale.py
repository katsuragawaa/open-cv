import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Make grayscale video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)
    
    # press Q to close
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()
