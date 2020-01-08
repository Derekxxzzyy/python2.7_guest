import cv2
import numpy
cap = cv2.VideoCapture(0)

while True:
	ret,img = cap.read()
	img = cv2.flip(img,-1)
	cv2.imshow("test",img)
