import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('hand.jpg', 0)
(h, w) = img.shape

# Initiate FAST object with default values
fast = cv2.ORB_create()

# find and draw the keypoints
kp = fast.detect(img, None)

kp, des = fast.compute(img, kp)

img2 = np.zeros((h, w, 3), np.uint8)
cv2.drawKeypoints(img, kp, img2, color=(255, 0, 0))

cv2.imshow('Win', img2)
k = cv2.waitKey(0)&0xFF
if k == ord("p"):
    cv2.imwrite("Win.png", img2)
else:
    cv2.destroyAllWindows()