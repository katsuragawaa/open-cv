import numpy as np
import cv2

capture = cv2.VideoCapture(0)


def make_1080p():
    capture.set(3, 1920)
    capture.set(4, 1080)


def make_720p():
    capture.set(3, 1280)
    capture.set(4, 720)


def make_480p():
    capture.set(3, 640)
    capture.set(4, 480)


def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)


make_1080p()
while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Display the resulting frame
    cv2.imshow("frame", frame)

    # press Q to close
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()
