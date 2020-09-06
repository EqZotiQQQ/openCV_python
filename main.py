from math import sqrt
from enum import Enum
import cv2
import numpy as np
import random
import datetime
import time


class DEBUG(Enum):
    NON_DEBUG = 0
    DEBUG_STREAM = 1
    DEBUG_STATIC = 2


class ALGORITHM(Enum):
    EACH_TO_EACH = 0
    PRIME = 1


# class Picture:
#     picture = np.zeros([512, 1024, 3], np.uint8)

debug = DEBUG.NON_DEBUG
# debug = DEBUG.DEBUG_STREAM
# debug = DEBUG.DEBUG_STATIC


# algorithm = ALGORITHM.EACH_TO_EACH
algorithm = ALGORITHM.PRIME


print("Type: {}; Algorithm: {}".format(debug, algorithm))

s = None

black_pic = np.zeros([512, 1024, 3], np.uint8)      # default pic


nodes = []                  # collection of all nodes
distances = {}              # dic:  {pair_of_dots: distance_between}
not_tree = []
tree = []


if debug == DEBUG.DEBUG_STATIC:             # to debug static dataset
    nodes = [(50, 40), (61, 250), (412, 551), (123, 321), (255, 255)]   # debug


def rand():
    return random.randint(35, 255), random.randint(35, 255), random.randint(35, 255)


white = (255, 255, 255)


def click_event(event, x, y, flags, param):
    global s

    try:
        if event == cv2.EVENT_LBUTTONDOWN:
            tree.clear()
            nodes.append((x, y))
            if len(nodes) > 1:
                if algorithm == ALGORITHM.EACH_TO_EACH:
                    connection_each_to_each()
                elif algorithm == ALGORITHM.PRIME:
                    connect_nodes_using_prim_alg()
            else:
                s = cv2.circle(black_pic, (x, y), 2, rand(), -1)
                cv2.imshow("foo", s)
        if event == cv2.EVENT_MOUSEMOVE:
            if s is not None:
                find_nearest(x, y)
    except:
        print("Error!")
        exit()


def find_nearest(x_ms, y_ms):
    global s
    min_distance = 0
    pair = None
    for x_dot, y_dot in nodes:
        distance = sqrt((x_dot - x_ms) ** 2 + (y_dot - y_ms) ** 2)
        if min_distance == 0 or min_distance > distance:
            min_distance = distance
            pair = (x_dot, y_dot)
    line = cv2.line(s, (x_ms, y_ms), pair, rand(), 1)
    cv2.imshow("foo", line)


def stream_simulation():
    while True:
        nodes.append((random.randint(0, 1000), random.randint(0, 500)))
        connect_nodes_using_prim_alg()
        tree.clear()
        cv2.waitKey()


def connect_nodes_using_prim_alg():
    global s
    s = np.zeros([512, 1024, 3], np.uint8)
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
            s = cv2.circle(s, nodes[-1], 2, rand(), -1)
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
            s = cv2.line(s, nearest_in_tree, nearest_out_of_tree, rand(), 1)
        cv2.imshow("foo", s)


def connection_each_to_each():
    picture = black_pic
    for x_first, y_first in nodes:
        for x_sec, y_sec in nodes:
            if x_first == x_sec and y_first == y_sec or ((x_sec, y_sec), (x_first, y_first)) in distances:
                continue
            distances[((x_first, y_first), (x_sec, y_sec))] = sqrt((x_sec - x_first)**2 + (y_sec - y_first)**2)
            picture = cv2.circle(picture, (x_first, y_first), 2, rand(), -1)
            picture = cv2.line(picture, (x_first, y_first), (x_sec, y_sec), rand(), 1)
            cv2.imshow("foo", picture)


def main_loop():
    cv2.imshow("foo", black_pic)
    if debug == DEBUG.DEBUG_STATIC:
        connect_nodes_using_prim_alg()
    elif debug == DEBUG.DEBUG_STREAM:
        stream_simulation()
    else:
        cv2.imshow("foo", black_pic)
        cv2.setMouseCallback("foo", click_event)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    main_loop()

if __name__ == '__main__':
    main()
