import cv2
import random
import numpy as np


black_pic = np.zeros([512, 1024, 3], np.uint8)
girl_face = cv2.imread('grill.jpg')
cond = False
btn_mem = [] # save here dots that user clicked


# some kind of magic here. x&y - coords
def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(btn_mem) <= 0:
            print(btn_mem)
            btn_mem.append((x, y))
            f = cv2.circle(black_pic, (x,y), 1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 5)
            cv2.imshow('image', f)
        else:
            print(btn_mem)
            btn_mem.append((x, y))
            f = cv2.line(black_pic, btn_mem[-1], btn_mem[-2], (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1)
            f = cv2.circle(f, btn_mem[-1], 1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 5)
            cv2.imshow('image', f)

    if event == cv2.EVENT_RBUTTONDOWN:
        btn_mem.append((x, y))
        f = cv2.circle(black_pic, (x, y), 1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 5)
        f = cv2.line(f, btn_mem[-1], btn_mem[-2], (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 1)
        f = cv2.line(f, btn_mem[0], btn_mem[-1], (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 1)
        cv2.imshow('image', f)

    if cond:
        if event == cv2.EVENT_LBUTTONDOWN:
            print("coords: ", str(x) + ', ' + str(y))
            strXY = str(x) + ', ' + str(y)
            cv2.putText(girl_face, strXY, (x, y), font, 1, (255, 255, 255), 2)
            cv2.imshow('image', girl_face)

        if event == cv2.EVENT_RBUTTONDOWN:
            blue = girl_face[y, x, 0]
            green = girl_face[y, x, 1]
            red = girl_face[y, x, 2]
            print("colors: ", str(blue) + ', ' + str(green) + ', ' + str(red))
            strXY = str(blue) + ', ' + str(green) + ', ' + str(red)
            cv2.putText(girl_face, strXY, (x, y), font, 1, (0, 255, 255), 2)
            cv2.imshow('image', girl_face)


def handle_events():
    #events = [i for i in dir(cv2) if 'EVENT' in i]
    #print(events)
    cv2.imshow('image', black_pic)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey()


def main():
    handle_events()


if __name__ == '__main__':
    main()
