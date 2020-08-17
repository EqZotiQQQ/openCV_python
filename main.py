import cv2
import numpy as np


def onValueChanged(val):
    print(val)


def main():
    prop_window = cv2.namedWindow("properties")
    cv2.createTrackbar('LH', "properties", 0, 255, onValueChanged)
    cv2.createTrackbar('LS', "properties", 0, 255, onValueChanged)
    cv2.createTrackbar('LV', "properties", 0, 255, onValueChanged)
    cv2.createTrackbar('UH', "properties", 255, 255, onValueChanged)
    cv2.createTrackbar('US', "properties", 255, 255, onValueChanged)
    cv2.createTrackbar('UV', "properties", 255, 255, onValueChanged)
    while True:
        pic = cv2.imread("balls2.jpg")
        hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)          # perform picture from RGB to HSV
        l_h = cv2.getTrackbarPos('LH', "properties")
        l_s = cv2.getTrackbarPos('LS', "properties")
        l_v = cv2.getTrackbarPos('LV', "properties")
        u_h = cv2.getTrackbarPos('UH', "properties")
        u_s = cv2.getTrackbarPos('US', "properties")
        u_v = cv2.getTrackbarPos('UV', "properties")
        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, l_b, u_b)                   # extract mask from pic

        res = cv2.bitwise_and(pic, pic, mask=mask)          # use and operation for picture with mask
        #l_g = np.array([50, 110, 50])
        #l_r = np.array([50, 50, 110])

        cv2.imshow("base picture", pic)
        cv2.imshow("mask", mask)
        cv2.imshow("res", res)
        exit_key = cv2.waitKey(1)
        if exit_key == 27:
            break


    cv2.destroyAllWindows()





if __name__ == '__main__':
    main()

