from math import sqrt

import cv2
import numpy as np
import random
import matplotlib as mp
from matplotlib import pyplot as plt

black_pic = np.zeros([512, 1024, 3], np.uint8)
nodes = []
distances = {}
stupid_var = True

def alg_prim():
    pass


def stream_imput():
    s = black_pic
    if stupid_var:
        for x_first, y_first in nodes:
            distances_for_node = []
            for x_sec, y_sec in nodes:
                if x_first == x_sec and y_first == y_sec:
                    continue
                distances_for_node.append(sqrt((x_sec - x_first)**2 + (y_sec - y_first)**2))
            print("dot: ({}, {}) \tdistances: {}".format(x_first, y_first, distances_for_node))
            s = cv2.line(s, (x_first, y_first), (x_sec, y_sec), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1)
            cv2.imshow("foo", s)
            #distances[node]
    #print(distances)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        nodes.append((x, y))
        if len(nodes) > 1:
            stream_imput()
            alg_prim()
    if event == cv2.EVENT_RBUTTONDOWN:
        nodes.clear()

    print(nodes)


def main_loop():
    cv2.imshow("foo", black_pic)
    cv2.setMouseCallback("foo", click_event)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    main_loop()


if __name__ == '__main__':
    main()