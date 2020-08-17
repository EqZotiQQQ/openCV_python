import cv2
import numpy as np


def draw_geom_shapes():
    #img = cv2.imread(pic, 1)
    img = np.zeros([512, 512, 3], np.uint8)     #create matrix of zeros
    # source, start coord-s, end coord-s, thickness
    img = cv2.line(img, (0, 0), (234, 344), (0, 255, 0), 1)
    img = cv2.arrowedLine(img, (80, 90), (234, 234), (255, 0, 255), 1)
    img = cv2.rectangle(img, (80, 90), (234, 234), (0, 0, 255), 4)
    img = cv2.circle(img, (80, 90), 42, (0, 123, 255), -2)
    font = cv2.FONT_HERSHEY_SIMPLEX     # choose font for text
    img = cv2.putText(img, "HEEEY", (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # pass


def main():
    draw_geom_shapes()


if __name__ == '__main__':
    main()