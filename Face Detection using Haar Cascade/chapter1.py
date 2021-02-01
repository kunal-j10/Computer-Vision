# importing OpenCV
import cv2

# defining my classifier and providing the trained classifier file name 
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
print("successful")

# reading the input img
img = cv2.imread("sample_image.jpg")

#converting the input image into grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Now by applying detectMultiScale method on our trained classifier
# we are going to detect Faces on the grayscale image
# the argument scaleFactor specify how much the img size is ruduced at each image scale
# minNeighbors parameter specify how many neighbors each candidate rectangle should have to retain it.

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=1)
print("s2")

# this will print cordinates of rectangle
print(type(faces))
print(faces)

# this will generate a rectangular box around our face
# the color of rectangular box will depend on RGB combination used here i have taken (255,100,50)
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+w),(255,100,50),3)
resized = cv2.resize(img,(int(img.shape[1]),int (img.shape[1])))


# Display the output image
cv2.imshow("Gray",resized)
cv2.waitKey(0)