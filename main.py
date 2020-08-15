import cv2


def load_show_pic():
    img = cv2.imread('grill.jpg', 1)
    cv2.imshow('img', img)
    cv2.waitKey()

def video_capture():
    cap = cv2.VideoCapture("test_vid.avi") #1st arg - file from u want to read video or camera ID (-1,0,etc)
    print(cap)
    while(True):
        ret, frame = cap.read()     #true/false if frame is available/ 2nd var is the current frame
        print(ret, frame)
        if(ret == False):
            break
        cv2.imshow("frames", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):              # ord returns int value of this char
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    #load_show_pic()
    video_capture()


if __name__ == '__main__':
    main()

