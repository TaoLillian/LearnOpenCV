import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
color = (255,0,0)
faceCascade= cv2.CascadeClassifier(r"C:\Users\28032\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, "person", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
    cv2.imshow("vedio",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


