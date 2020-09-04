import cv2
import datetime

copy_vid = False        # to store vid copy

def video_capture():
    vid = 'test_vid.avi'
    cap = cv2.VideoCapture(vid)     # 1st arg - file from u want to read video or camera ID (-1,0,etc). Looks like it returns pointer to stream.
    cap.set(3, 1500)            # doesn't work for tutor vid cuz of max resolution for it 320x240
    cap.set(4, 1500)            # doesn't work for tutor vid cuz of max resolution for it 320x240

    if copy_vid:
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')        # or (*'XVID')     for copy from source to file
        out = cv2.VideoWriter('out_vid.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()     # true/false if frame is available/ 2nd var is the current frame    reads frame from cap
        if not ret:
            break

        font = cv2.FONT_HERSHEY_SIMPLEX
        date = datetime.datetime.now()
        text_on_video = "time is {}".format(date)

        frame = cv2.putText(frame, text_on_video, (0, 50), font, 0.5, (255, 200, 134), 1, cv2.LINE_AA)
        if copy_vid:
            out.write(frame)                                 # write to out videowriter current frame
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # convert vid thread to white-black pic
        cv2.imshow("frames", frame)                         # image show(win name, object to show)
        if cv2.waitKey(1) & 0xFF == ord('q'):              # ord returns int value of this char
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    video_capture()


if __name__ == '__main__':
    main()