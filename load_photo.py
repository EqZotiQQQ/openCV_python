import cv2


def load_show_pic():
    pic = 'grill.jpg'
    img = cv2.imread(pic, 1)
    cv2.imshow('img', img)
    cv2.waitKey()


def main():
    load_show_pic()


if __name__ == '__main__':
    main()
