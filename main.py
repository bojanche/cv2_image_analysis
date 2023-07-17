import cv2 as cv

vcap = cv.VideoCapture("rtsp://admin:password@192.168.39.102:8554/fhd")
while(1):
    ret, frame = vcap.read()
    cv.imshow('VIDEO', frame)
    cv.waitKey(1)
