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


class ALGORITHM:
    EACH_TO_EACH = 0
    PRIME = 1


debug = DEBUG.NON_DEBUG
# debug = DEBUG.DEBUG_STREAM
# debug = DEBUG.DEBUG_STATIC


# algorithm = ALGORITHM.EACH_TO_EACH
algorithm = ALGORITHM.PRIME

print("Type: {}; Algorithm: {}".format(debug, algorithm))

black_pic = np.zeros([512, 1024, 3], np.uint8)


nodes = []


if debug == DEBUG.DEBUG_STATIC:
    nodes = [(50, 40), (61, 250), (412, 551), (123, 321), (255, 255)]   # debug


distances = {}


def rand():
    return random.randint(35, 255), random.randint(35, 255), random.randint(35, 255)


def connection_each_to_each():
    s = black_pic
    for x_first, y_first in nodes:
        for x_sec, y_sec in nodes:
            if x_first == x_sec and y_first == y_sec or ((x_sec, y_sec), (x_first, y_first)) in distances:
                continue
            distances[((x_first, y_first), (x_sec, y_sec))] = sqrt((x_sec - x_first)**2 + (y_sec - y_first)**2)
            s = cv2.circle(s, (x_first, y_first), 2, rand(), -1)
            s = cv2.line(s, (x_first, y_first), (x_sec, y_sec), rand(), 1)
            cv2.imshow("foo", s)


all_nodes = {}
not_tree = []
tree = []
white = (255, 255, 255)


def connect_nodes_using_prim_alg():
    s = np.zeros([512, 1024, 3], np.uint8)
    max_distance = 0
    for x_first, y_first in nodes:
        for x_sec, y_sec in nodes:
            if x_first == x_sec and y_first == y_sec or ((x_sec, y_sec), (x_first, y_first)) in all_nodes:
                continue
            distance = sqrt((x_sec - x_first) ** 2 + (y_sec - y_first) ** 2)
            all_nodes[((x_first, y_first), (x_sec, y_sec))] = distance
            if distance >= max_distance:
                max_distance = distance
        if (x_first, y_first) not in not_tree:
            not_tree.append((x_first, y_first))
            s = cv2.circle(s, nodes[-1], 2, rand(), -1)
    # print("global_max_distance = {}".format(max_distance))
    nearest_in_tree = None
    nearest_out_of_tree = None
    # print("-------")
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
                    # print("connected = {}, not_connected = {}".format(connected, not_connected))
                    # print("=====")
                    # print("nodes = {}".format(nodes))
                    # print("tree = {}".format(tree))
                    # print("not a tree = {}".format(not_tree))
                    # print("all_nodes = {}".format(all_nodes))
                    # print("min_distance = {}, current_dist = {}".format(min_distance, all_nodes.get((connected, not_connected))))
                    # print("=====")
                    pair = None
                    if (connected, not_connected) in all_nodes:
                        pair = (connected, not_connected)
                    else:
                        pair = (not_connected, connected)
                    if min_distance >= all_nodes.get(pair):
                        min_distance = all_nodes.get(pair)
                        nearest_in_tree = connected
                        nearest_out_of_tree = not_connected

            tree.append(nearest_out_of_tree)
            not_tree.remove(nearest_out_of_tree)
            # print("tree = {}, not_tree: {}".format(tree, not_tree))
            # print("nearest_in_tree = {}, nearest_out_of_tree: {}".format(nearest_in_tree, nearest_out_of_tree))
            # s = cv2.line(s, nearest_in_tree, nearest_out_of_tree, white, 1)
            s = cv2.line(s, nearest_in_tree, nearest_out_of_tree, rand(), 1)
        cv2.imshow("foo", s)


def stream_simulation():
    while True:
        nodes.append((random.randint(0, 1000), random.randint(0, 500)))
        connect_nodes_using_prim_alg()
        tree.clear()
        cv2.waitKey()
        #time.sleep(0.5)


def click_event(event, x, y, flags, param):
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
    except:
        print("Error!")
        exit()


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
