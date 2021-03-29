import cv2
minarea = 500
color = (255,0,255)
nPlateCascade= cv2.CascadeClassifier(r"C:\Users\28032\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_russian_plate_number.xml")


img = cv2.imread("resources/p1.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
numberPlates = nPlateCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in numberPlates:
    area = w*h
    if area > minarea:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,"number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        imgRoi = img[y:y+h,x:x+w]
        cv2.imshow("ROI",imgRoi)
cv2.imshow(" img ",img)
cv2.waitKey(0)