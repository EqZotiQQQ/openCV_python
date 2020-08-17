import cv2
import numpy as np


def onChannelChanged(val):
    print(val)


def main():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow("image")                                           # creates blank window with name
    cv2.createTrackbar('B', 'image', 0, 255, onChannelChanged)         # creates scrollbar for diapason [0:255] with callback on its changes
    cv2.createTrackbar('G', 'image', 0, 255, onChannelChanged)
    cv2.createTrackbar('R', 'image', 0, 255, onChannelChanged)

    switch1 = '0 : OFF\n 1: ON'
    cv2.createTrackbar(switch1, 'image', 0, 1, onChannelChanged)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        b = cv2.getTrackbarPos('B', 'image')            # get value of trackbar B
        g = cv2.getTrackbarPos('G', 'image')            # get value of trackbar G
        r = cv2.getTrackbarPos('R', 'image')            # get value of trackbar R
        s1 = cv2.getTrackbarPos(switch1, 'image')            # get value of trackbar R

        if s1 == 0:                          # if switch == 0 - it locks changes
            img[:] = 0
        else:
            img[:] = [b, g, r]
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()