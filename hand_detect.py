import cv2
import numpy as np

in_image = 'hand.jpg'
out_image = 'hand_out.jpg'
out_image_thr = 'hand_thr.png'

ORANGE_MIN = np.array([0, 0, 130], np.uint8, ndmin=1)
ORANGE_MAX = np.array([18, 85, 253], np.uint8, ndmin=1)
PINK_MIN = np.array([170, 75, 102], np.uint8, ndmin=1)
PINK_MAX = np.array([179, 149, 218], np.uint8, ndmin=1)
COLOR_MIN = ORANGE_MIN
COLOR_MAX = ORANGE_MAX
COLOR_MIN2 = PINK_MIN
COLOR_MAX2 = PINK_MAX


def test1():
    frame = cv2.imread(in_image, 1)
    (h, w, ch) = frame.shape
    print(frame.shape)
    frameHSV = np.zeros((h, w, ch), np.uint8)
    print(frameHSV.shape)
    cv2.cvtColor(frame, cv2.COLOR_BGR2HSV, frameHSV)
    # cv2.imshow("Wind",frameHSV)
    # cv2.waitKey(0)
    frame_threshed = np.zeros((h, w, 1), np.uint8)
    frame_threshed1 = np.zeros((h, w, 1), np.uint8)
    frame_threshed2 = np.zeros((h, w, 1), np.uint8)
    print(frame_threshed.shape)
    cv2.inRange(frameHSV, COLOR_MIN, COLOR_MAX, frame_threshed1)
    cv2.inRange(frameHSV, COLOR_MIN2, COLOR_MAX2, frame_threshed2)
    cv2.bitwise_or(frame_threshed1, frame_threshed2,frame_threshed)
    cv2.imwrite(out_image_thr, cv2.bitwise_and(frame,frame, mask = frame_threshed))


if __name__ == '__main__':
    test1()
