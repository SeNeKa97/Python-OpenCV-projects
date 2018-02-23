import numpy as np
import cv2


def areaCalc(contour):
    rect = cv2.boundingRect(contour)
    return rect[0]*rect[1]


original = cv2.imread("images/sample.jpg", 1)
ratio = original.shape[0]/original.shape[1]
img = original.copy()

cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Window", 600,500)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0)

ret, gray = cv2.threshold(gray.copy(), 190, 255, cv2.THRESH_BINARY)
im2, cntr, hrh = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = cntr[4]


cntr.sort(key=lambda x: areaCalc(x))

paperCnt = None

peri = cv2.arcLength(cntr[0], True)
approx = cv2.approxPolyDP(cntr[0], 0.02 * peri, True)

if len(approx) == 4:
    paperCnt = approx

paperArr = []
for i in range(len(paperCnt)):
    paper = paperCnt[i][0]
    paperArr.append([paper[0], paper[1]])
print(paperArr)

img2 = cv2.polylines(img, paperCnt, True, (0, 0, 255), 2)
cv2.imshow("Window", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()