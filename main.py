from math import sqrt
from enum import Enum
import cv2
import numpy as np
from random import randint
from copy import copy


class DEBUG(Enum):
    NON_DEBUG = 0
    DEBUG_STREAM = 1
    DEBUG_STATIC = 2


class ALGORITHM(Enum):
    EACH_TO_EACH = 0
    PRIME = 1


debug = DEBUG.NON_DEBUG
# debug = DEBUG.DEBUG_STREAM
# debug = DEBUG.DEBUG_STATIC


# algorithm = ALGORITHM.EACH_TO_EACH
algorithm = ALGORITHM.PRIME


image = None
black_pic = np.zeros([512, 1024, 3], np.uint8)      # default pic


nodes = []                  # collection of all nodes
distances = {}              # dic:  {pair_of_dots: distance_between}
not_tree = []               # [(x1,y1),(x2,y2),...]
tree = []                   # [(x1,y1),(x2,y2),...]


if debug == DEBUG.DEBUG_STATIC:             # to debug static dataset
    nodes = [(50, 40), (61, 250), (412, 551), (123, 321), (255, 255)]   # debug


def get_color(clr="rnd"):
    if clr == "white":
        return 255, 255, 255
    elif clr == "gray":
        return 50, 50, 50
    elif clr == "red":
        return 0, 0, 255
    else:
        return randint(35, 255), randint(35, 255), randint(35, 255)


def click_event(event, x, y, flags, param):
  #try:
    global image
    if event == cv2.EVENT_LBUTTONDOWN:
        tree.clear()
        nodes.append((x, y))
        if len(nodes) > 1:
            if algorithm == ALGORITHM.EACH_TO_EACH:
                connection_each_to_each()
            elif algorithm == ALGORITHM.PRIME:
                connect_nodes_using_prim_alg()
        else:
            image = cv2.circle(black_pic, (x, y), 2, get_color("white"), -1)
            cv2.imshow("foo", image)
    if event == cv2.EVENT_MOUSEMOVE:
        if image is not None:
            find_nearest(x, y)
  #except:
  #    print("Error!")
  #    exit()


def find_nearest(x_ms, y_ms):
    picture = copy(image)
    min_distance = 0
    pair = None
    for x_dot, y_dot in nodes:
        distance = sqrt((x_dot - x_ms) ** 2 + (y_dot - y_ms) ** 2)
        if min_distance == 0 or min_distance > distance:
            min_distance = distance
            pair = (x_dot, y_dot)
    picture = cv2.line(picture, (x_ms, y_ms), pair, get_color("gray"), 1)
    cv2.imshow("foo", picture)


def stream_simulation():
    while True:
        nodes.append((randint(0, 1000), randint(0, 500)))
        connect_nodes_using_prim_alg()
        tree.clear()
        cv2.waitKey()


def connect_nodes_using_prim_alg():
    print(nodes)
    global image
    image = np.zeros([512, 1024, 3], np.uint8)
    max_distance = 0
    for x_first, y_first in nodes:
        for x_sec, y_sec in nodes:
            if x_first == x_sec and y_first == y_sec or ((x_sec, y_sec), (x_first, y_first)) in distances:
                continue
            distance = sqrt((x_sec - x_first) ** 2 + (y_sec - y_first) ** 2)
            distances[((x_first, y_first), (x_sec, y_sec))] = distance
            if distance >= max_distance:
                max_distance = distance
        if (x_first, y_first) not in not_tree:
            not_tree.append((x_first, y_first))
    nearest_in_tree = None
    nearest_out_of_tree = None
    while len(not_tree) > 0:
        if len(tree) == 0:   # add 1st elem
            tree.append(not_tree[0])
            not_tree.remove(not_tree[0])
        else:
            min_distance = max_distance
            nearest_in_tree = None
            nearest_out_of_tree = None
            for connected in tree:
                image = cv2.circle(image, connected, 2, get_color("red"), -1)
                for not_connected in not_tree:
                    pair = None
                    if (connected, not_connected) in distances:
                        pair = (connected, not_connected)
                    else:
                        pair = (not_connected, connected)
                    if min_distance >= distances.get(pair):
                        min_distance = distances.get(pair)
                        nearest_in_tree = connected
                        nearest_out_of_tree = not_connected

            tree.append(nearest_out_of_tree)
            not_tree.remove(nearest_out_of_tree)
            image = cv2.line(image, nearest_in_tree, nearest_out_of_tree, get_color("white"), 1)
        cv2.imshow("foo", image)


def connection_each_to_each():
    picture = black_pic
    for x_first, y_first in nodes:
        for x_sec, y_sec in nodes:
            if x_first == x_sec and y_first == y_sec or ((x_sec, y_sec), (x_first, y_first)) in distances:
                continue
            distances[((x_first, y_first), (x_sec, y_sec))] = sqrt((x_sec - x_first)**2 + (y_sec - y_first)**2)
            picture = cv2.circle(picture, (x_first, y_first), 2, get_color(), -1)
            picture = cv2.line(picture, (x_first, y_first), (x_sec, y_sec), get_color(), 1)
            cv2.imshow("foo", picture)


def main():
    cv2.imshow("foo", black_pic)
    if debug == DEBUG.DEBUG_STATIC:
        connect_nodes_using_prim_alg()
    elif debug == DEBUG.DEBUG_STREAM:
        stream_simulation()
    else:
        cv2.setMouseCallback("foo", click_event)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
