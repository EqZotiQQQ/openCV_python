import cv2
import numpy as np


def onValueChanged(val):
    print(val)


def main():
    prop_window = cv2.namedWindow("properties")
    #vid = cv2.VideoCapture(0)
    vid = cv2.VideoCapture('videos/test_vid.avi')
    # cv2.createTrackbar('LH', "properties", 0, 255, onValueChanged)
    cv2.createTrackbar('LS', "properties", 0, 255, onValueChanged)
    cv2.createTrackbar('LV', "properties", 0, 255, onValueChanged)
    # cv2.createTrackbar('UH', "properties", 255, 255, onValueChanged)
    cv2.createTrackbar('US', "properties", 255, 255, onValueChanged)
    cv2.createTrackbar('UV', "properties", 255, 255, onValueChanged)
    cv2.createTrackbar('Mono', "properties", 0, 255, onValueChanged)
    while True:
        _, pic = vid.read()
        # pic = cv2.imread("images/balls2.jpg")
        hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)          # perform picture from RGB to HSV
        # l_hue = cv2.getTrackbarPos('LH', "properties")
        l_saturation = cv2.getTrackbarPos('LS', "properties")
        l_value = cv2.getTrackbarPos('LV', "properties")
        # r_hue = cv2.getTrackbarPos('UH', "properties")
        r_saturation = cv2.getTrackbarPos('US', "properties")
        r_value = cv2.getTrackbarPos('UV', "properties")
        Mono = cv2.getTrackbarPos('Mono', "properties")
        l_hue = Mono-5
        r_hue = Mono+5
        l_color = np.array([l_hue, l_saturation, l_value])
        r_color = np.array([r_hue, r_saturation, r_value])
        print("l_b: ", l_color)
        print("u_b: ", r_color)
        mask = cv2.inRange(hsv, l_color, r_color)
        res = cv2.bitwise_and(pic, pic, mask=mask)          # use and operation for picture with mask

        cv2.imshow("base picture", pic)
        cv2.imshow("mask", mask)
        cv2.imshow("res", res)
        exit_key = cv2.waitKey(1)
        if exit_key == 27:
            break

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

