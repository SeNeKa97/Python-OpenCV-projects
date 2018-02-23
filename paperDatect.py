import numpy as np
import cv2


def areaCalc(contour):
    rect = cv2.boundingRect(contour)
    return rect[0]*rect[1]


original = cv2.imread("sample.jpg", 1)
ratio = original.shape[0]/original.shape[1]
img = original.copy()

cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Window", 600,500)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0)

ret, gray = cv2.threshold(gray.copy(), 190, 255, cv2.THRESH_BINARY)
im2, cntr, hrh = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = cntr[4]

# for i in range(len(cntr)):
# x, y, w, h = cv2.boundingRect(cnt)
# img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 5)
print(len(cntr))
cntr.sort(key=lambda x: areaCalc(x))

paperCnt = None

peri = cv2.arcLength(cntr[0], True)
approx = cv2.approxPolyDP(cntr[0], 0.02 * peri, True)

# if our approximated contour has four points, then
# we can assume that we have found our screen
if len(approx) == 4:
    paperCnt = approx




cv2.drawContours(img, paperCnt, -1, (0, 0, 255), 2)

cv2.imshow("Window", img)

cv2.waitKey(0)
