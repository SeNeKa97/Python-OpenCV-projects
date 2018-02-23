import cv2
import numpy as np
import datetime

vid = cv2.VideoCapture('file.mp4')
width = int(vid.get(3))
height = int(vid.get(4))

fourCC = cv2.VideoWriter_fourcc(*'X264')
# out = cv2.VideoWriter(str(datetime.datetime.now())+".avi", fourCC, 20.0, (width, height))

cv2.namedWindow("Window1", cv2.WINDOW_FREERATIO)

while vid.isOpened():
    ret, frame = vid.read()

    if ret is True:
        changes = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # out.write(changes)
        cv2.imshow("Window 1", frame)
        frame = cv2.resize(frame, (640, 480))

        cv2.imwrite(str(datetime.datetime.now())+".png", frame)

        k = cv2.waitKey(30) & 0xFF
        if k == ord('q'):
            break
    else:
        break

vid.release()
# out.release()
cv2.destroyAllWindows()
