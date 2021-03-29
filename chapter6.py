import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    #增加一句
                    imgArray[x][y] = imgArray[x][y].astype(np.uint8)
                    imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    # 基于opncv4.1.0的findContours是可以接受两个返回值的
    # 但是基于opencv3.4.15的findContours是需要接受三个返回值的
    # 修改为：binary, contours, hierarchy = cv2.findContours(gray_temp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    contours,Hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # cnt表示了某一个图形的轮廓点的集合
        area = cv2.contourArea(cnt)
        print(area)


        # draw contours
        #cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]])
        if area > 200:
            cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
            # 计算轮廓长度
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            # cv.approxPolyDP() 的参数1是源图像的某个轮廓；参数2(epsilon)是一个距离值，表示多边形的轮廓接近实际轮廓的程度，值越小，越精确；参数3表示是否闭合
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # 表示它的边数，有几条边
            print(len(approx))
            objCor = len(approx)
            # 矩形边框（Bounding Rectangle）是说，用一个最小的矩形，把找到的形状包起来。
            # x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
            x, y, w, h = cv2.boundingRect(approx)
            #利用rectangle函数将图形画出来
            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"
            cv2.putText(imgcontour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)




img = cv2.imread("resources/shape.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgblack = np.zeros_like(img)
imgcontour = img.copy()

getContours(imgCanny)

imgstack = stackImages(0.6,([img,imgGray,imgBlur],[imgCanny,imgcontour,imgblack]))
cv2.imshow("imgstack",imgstack)


cv2.waitKey(0)