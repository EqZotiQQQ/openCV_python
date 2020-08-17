import cv2


def main():
    pic1 = cv2.imread('1024x768.jpg')
    print(pic1.shape)
    print(pic1)
    pic2 = cv2.imread('1024x768_2.jpg')
    print(pic2.shape)
    print(pic2)

    dst = cv2.add(pic1, pic2)
    print(dst.shape)
    print(dst)
    cv2.imshow('img', dst)
    #cv2.imshow('img', tmp)
    #cv2.imshow('img', girl_face)
    cv2.waitKey()

if __name__ == '__main__':
    main()
