import datetime
import cv2
import numpy as np

black_pic = np.zeros([512, 1024, 3], np.uint8)
girl_face = cv2.imread('grill.jpg')

def load_show_pic():
    pic = 'grill.jpg'
    img = cv2.imread(pic, 1)
    cv2.imshow('img', img)
    cv2.waitKey()


def video_capture():
    vid = 'test_vid.avi'
    cap = cv2.VideoCapture(vid)     # 1st arg - file from u want to read video or camera ID (-1,0,etc). Looks like it returns pointer to stream.
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap.set(3, 1500)            # doesn't work for tutor vid cuz of max resolution for it 320x240
    cap.set(4, 1500)            # doesn't work for tutor vid cuz of max resolution for it 320x240
    print(cap.get(3))
    print(cap.get(4))


    # fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')        # or (*'XVID')     for copy from source to file
    # out = cv2.VideoWriter('out_vid.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()     # true/false if frame is available/ 2nd var is the current frame    reads frame from cap
        if not ret:
            break

        font = cv2.FONT_HERSHEY_SIMPLEX
        date = datetime.datetime.now()
        text_on_video = "time is {}".format(date)

        frame = cv2.putText(frame, text_on_video, (0, 50), font, 0.5, (255, 200, 134), 1, cv2.LINE_AA)
        # out.write(frame)                                 # write to out videowriter current frame
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # convert vid thread to white-black pic
        cv2.imshow("frames", frame)                         # image show(win name, object to show)
        if cv2.waitKey(1) & 0xFF == ord('q'):              # ord returns int value of this char
            break
    cap.release()
    cv2.destroyAllWindows()


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


btn_mem = []
# some kind of magic here. x&y - coords
def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(btn_mem) <= 0:
            print(btn_mem)
            btn_mem.append((x, y))
            f = cv2.circle(black_pic, (x,y), 1, (255, 255, 255), 5)
            cv2.imshow('image', f)
        else:
            print(btn_mem)
            btn_mem.append((x, y))
            f = cv2.line(black_pic, btn_mem[-1], btn_mem[-2], (0,255,0), 1)
            f = cv2.circle(f, btn_mem[-1], 1, (255, 255, 255), 5)
            cv2.imshow('image', f)

    if event == cv2.EVENT_RBUTTONDOWN:
        btn_mem.append((x, y))
        f = cv2.circle(black_pic, (x, y), 1, (255, 255, 255), 5)
        f = cv2.line(black_pic, btn_mem[-1], btn_mem[-2], (0, 255, 0), 1)
        f = cv2.line(black_pic, btn_mem[0], btn_mem[-1], (123, 255, 0), 1)
        cv2.imshow('image', f)

    if False:
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
    # load_show_pic()
    # video_capture()
    # draw_geom_shapes()
    handle_events()


if __name__ == '__main__':
    main()

