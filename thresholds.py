import cv2
from matplotlib import pyplot as plt


def onChange(x):
    pass


def thresholding_static():
    img = cv2.imread('images/grill.jpg', 0)
    cv2.namedWindow("settings")
    cv2.createTrackbar("threshold", "settings", 0, 255, onChange)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    while True:
        threshold_value = cv2.getTrackbarPos("threshold", "settings")
        _, img_threshold1 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TOZERO)
        _, img_threshold2 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TOZERO_INV)
        _, img_threshold3 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY_INV)
        _, img_threshold4 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

        titles = ["THRESH_TOZERO", "THRESH_TRIANGLE", "THRESH_BINARY_INV", "THRESH_BINARY"]
        images = [img_threshold1, img_threshold2, img_threshold3, img_threshold4]

        for i in range(4):
            plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
            print(i)
            plt.title(titles[i])
        print(threshold_value)
        plt.show()
        #if cv2.waitKey(1) & 0xFF == ord('q'):  # ord returns int value of this char
        #    break
    cv2.destroyAllWindows()


# works better if u have different quality of illumination on the image
def thresholding_adaptive():
    img = cv2.imread('images/grill.jpg', 0)
    cv2.namedWindow("settings")
    cv2.createTrackbar("threshold", "settings", 0, 50, onChange)
    while True:
        threshold_value = cv2.getTrackbarPos("threshold", "settings")
        img_thr1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, threshold_value)
        img_thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,
                                         threshold_value)
        cv2.imshow("threshold1", img_thr1)
        cv2.imshow("threshold2", img_thr2)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # ord returns int value of this char
            break
    cv2.destroyAllWindows()


def main():
    thresholding_static()
    # thresholding_adaptive()


if __name__ == '__main__':
    main()
