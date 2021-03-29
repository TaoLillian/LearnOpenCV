import cv2
import numpy
# img = cv2.imread("resources/puke.jpg")
# img = cv2.resize(img,(500,500))
# img = img[100:400,:]
# cv2.imwrite("resources/puke_1.jpg",img)

img = cv2.imread("resources/puke_1.jpg")
weith,height = 300,500
pts1 = numpy.float32([[70,320],[240,100],[230,400],[120,500]])
pts2 = numpy.float32([[0,0],[weith,0],[0,height],[weith,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(weith,height))

cv2.imshow("img",img)
cv2.imshow("imgoutput",imgoutput)
hst = numpy.hstack([img,img])
cv2.imshow("hst",hst)
vst = numpy.vstack([img,img])
cv2.imshow("vst",vst)
cv2.waitKey(0)

