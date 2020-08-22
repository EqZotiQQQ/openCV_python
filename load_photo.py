import cv2


def view_image():
    pic = 'images/grill.jpg'

    img_bgr = cv2.imread(pic, 1)
    cv2.imshow('img', img_bgr)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    cv2.imshow('rgb_img', img_rgb)

    img_cropped = img_bgr[200:600, 150:600]
    cv2.imshow("img_cropped", img_cropped
               )
    cv2.waitKey()


def main():
    view_image()


if __name__ == '__main__':
    main()
