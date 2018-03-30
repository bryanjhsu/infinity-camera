import numpy as np
import cv2
import ipcamera
import time

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# download haar cascades from: https://github.com/opencv/opencv/tree/master/data/haarcascades
video_capture = cv2.VideoCapture(ipcamera.RTSP_URL)

# get the current time in seconds
last_moved = time.time()

recording = 0
direction = "left"
count = 0
ipcamera.pan(0) #-60 to 60
ipcamera.tilt(2)

ipcamera.record('test3.mp4', duration='00:10:00')

speed = -1000

while True:
    ret, frame = video_capture.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ipcamera.move('right')

    # faces = face_cascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.1,
    #     minNeighbors=5,
    #     minSize=(30, 30),
    # )

    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # find the biggest face and center the camera on it
    current_time = time.time()

    if current_time - last_moved > 0.1:
        ipcamera.tilt(2)
        # ipcamera.pan(count * 0.25)
        ipcamera.continuousPan(speed)

        if direction == "left":
            count -= 1
        elif direction == "right":
            count += 1

        if count <= -250:
            direction = "right"
            speed = 1000
        elif count >= 250    :
            direction = "left"
            speed = -1000

        # if count == 0:
        #     ipcamera.pan(panArray[1])
        #     count = 1
        # elif count == 1:
        #     ipcamera.pan(panArray[2])
        #     count = 2
        # elif count == 2:
        #     ipcamera.pan(panArray[1])
        #     count = 3
        # elif count == 3:
        #     ipcamera.pan(panArray[0])
        #     count = 0

        last_moved = time.time()
        
    # comment out these lines if you don't want to see a preview window
    # cv2.imshow('Video', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

video_capture.release()
cv2.destroyAllWindows()