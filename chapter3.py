import cv2
img = cv2.imread("resources/carambula_0_100.jpg")


img = cv2.resize(img,(200,200))
cv2.line(img,(0,0),(100,150),(0,255,0),2)
cv2.rectangle(img,(0,0),(100,50),(255,0,213),5)
cv2.circle(img,(70,120),30,(123,23,168),2)
cv2.imshow("img ",img)
cv2.waitKey(0)