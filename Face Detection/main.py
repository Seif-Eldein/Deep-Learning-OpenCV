import cv2

faceCascade = cv2.CascadeClassifier("Modules/haarcascade_frontalface_default.xml")

image = cv2.imread("Resources/lena.png")
GrayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

Faces = faceCascade.detectMultiScale(GrayImg, 1.1, 4)

for (x, y, w, h) in Faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0))

cv2.imshow("Faces", image)

cv2.waitKey(0)
