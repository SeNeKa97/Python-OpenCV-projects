import cv2
import numpy as np

img = cv2.imread("kittens.jpg", 1)

cv2.line(img, (0, 0), (150, 150), (255, 255, 0), 3)
cv2.imshow("image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
