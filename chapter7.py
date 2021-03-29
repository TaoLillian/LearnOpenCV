import cv2
# 从Github上面下载了haarcascade_frontalface_alt.xml放在了resources，编译一直出问题.
# 后来才发现在安装cv2这个模块的时候，会在你python安装路径下面生成”C:\Users\28032\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data“
# 加载人脸模型
faceCascade= cv2.CascadeClassifier(r"C:\Users\28032\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
# 下面这条语句运行会报错。
# faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img = cv2.imread("resources/lena.png")
# 调整图片灰度，只是为了提高性能。
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 检查人脸
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
# 标记人脸
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow(" img ",img)
cv2.waitKey(0)