import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
print("successful")
img = cv2.imread("sample_image.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=1)
print("s2")
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+w),(255,100,50),3)
resized = cv2.resize(img,(int(img.shape[1]),int (img.shape[1])))
cv2.imshow("Gray",resized)
cv2.waitKey(0)