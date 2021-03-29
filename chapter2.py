import cv2
import numpy as np
img = cv2.imread("resources/carambula_0_100.jpg")
cv2.imshow("img",img)
print(img.shape)


img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #将彩色图片转化为灰色图片
cv2.imshow("gray img",img_gray)

img_blur = cv2.GaussianBlur(img,(7,7),0)  #将图片进行模糊处理
cv2.imshow("blur img",img_blur)

img_canny = cv2.Canny(img_gray,150,200) #图片进行边缘化处理
cv2.imshow("canny img",img_canny)

kernal = np.ones((5,5),np.uint8)
img_dialation = cv2.dilate(img_canny,kernal,iterations=1)  #将边缘化的图片进行膨胀处理
img_erode = cv2.erode(img_gray,kernal,iterations=1)  #将图片进行腐化处理
#第一个参数：img指需要腐蚀的图

#第二个参数：kernel指腐蚀操作的内核，默认是一个简单的3X3矩阵，我们也可以利用getStructuringElement（）函数指明它的形状

#第三个参数：iterations指的是腐蚀次数，省略是默认为1

cv2.imshow("dilation img",img_dialation)
cv2.imshow("erode img",img_erode)


img = cv2.resize(img,(300,300))
cv2.imshow("large img",img)

img_cropped = img[150:,100:200]  #截取图片的一部分
cv2.imshow("cropped img ",img_cropped)
cv2.waitKey(0)