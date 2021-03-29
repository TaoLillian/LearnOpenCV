import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# 在图片hsv的格式下，只是显示出我们想要的颜色，杂色进行隐藏
myColors = [[0,164,0,179,255,255],  #橙色
            [108,25,0,179,255,255],  #紫色
            [25,107,74,62,255,255], #绿色
            [95,41,45,150,255,255]]  #蓝色
myColorValues = [[0,128,255],          ## BGR
                 [255,0,77],
                 [77,255,0],
                 [255,115,0]]

mypoints = []  #[x,y,colorid]

def findcolor(img,myColors,myColorValues):
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newpoints = []
    count = 0
    for color in myColors:
        # count = myColors.index(color)
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img_HSV, lower, upper)
        # 根据颜色来查找边框，拿到返回的圆心的坐标
        x,y = getContours(mask)







        if x != 0 and y != 0:
            newpoints.append([x,y,count])
        count +=1
        return newpoints

def getContours(img):
    contours,Hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2 , y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),5,myColorValues[point[2]],cv2.FILLED)

while True:

    #  原因：因为在进行颜色识别时，可能
    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findcolor(img,myColors,myColorValues)
    if len(newpoints)!= 0:
        for newp in newpoints:
            mypoints.append(newp)
    if len(mypoints) != 0:
        drawOnCanvas(mypoints,myColorValues)
    cv2.imshow("vedio",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
