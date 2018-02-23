import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread("blend.jpg")
# counter = 1


while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:

        # if counter%2 == 0:
        # cv2.rectangle(frame, (10, 10), (630, 470), (0, 255, 255), 1, cv2.LINE_AA)
        frag = frame[0:479, 320:639]
        frame[0:479, 0:319] = cv2.flip(frag, 1)

        cv2.imshow("Window", frame)


        k = cv2.waitKey(1) & 0xFF
        if k == ord('p'):
            cv2.imwrite(str(datetime.datetime.now()) + ".png", frame)
        elif k == ord('q'):
            break

        # counter += 1
    else:
        break

cap.release()
cv2.destroyAllWindows()