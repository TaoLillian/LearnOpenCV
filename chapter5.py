import cv2
import numpy as np


def empty(a):
    pass
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640,340)
cv2.createTrackbar("Hue Min","trackbar",0,179,empty)
cv2.createTrackbar("Hue Max","trackbar",179,179,empty)
cv2.createTrackbar("Sat Min","trackbar",0,255,empty)
cv2.createTrackbar("Sat Max","trackbar",255,255,empty)
cv2.createTrackbar("Val Min","trackbar",0,255,empty)
cv2.createTrackbar("Val Max","trackbar",255,255,empty)

while True:
    img = cv2.imread("resources/car.jpg")
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "trackbar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(img_HSV,lower,upper)

    cv2.imshow(" img ", img)
    cv2.imshow("img_hsv", img_HSV)
    cv2.imshow("mask",mask)
    cv2.waitKey(1)