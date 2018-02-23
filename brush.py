import cv2
import numpy as np
import datetime as dt

isDown = False
mousePos = None

def mouse_handler(event, x, y, flags, param):
    global isDown, mousePos
    color = (0, 255, 240)
    radius = 20

    if event == cv2.EVENT_LBUTTONDOWN:
        isDown = True
        mousePos = (x, y)
        cv2.circle(img, (x, y), radius, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDown:
            # cv2.circle(img, (x, y), radius, color, -1)
            cv2.line(img, mousePos, (x, y), color, 40)
            mousePos = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        isDown = False
        mousePos = None


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", mouse_handler)

while 1:
    cv2.imshow("Window", img)

    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord("m"):
        img = np.zeros((512, 512, 3), np.uint8)
    elif k == ord("s"):
        cv2.imwrite(str(dt.datetime.now())+".png", img)

cv2.destroyAllWindows()
