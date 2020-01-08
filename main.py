import numpy as np
import cv2
import requests
from json import JSONDecoder
import os
import json
import time
import pygame
file=r'/home/pi/python2.7_guest/audio.mp3'
#fps = 0
#fps_plus = 24
pygame.mixer.init()
def camera():
    face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret,img = cap.read()
        #img = cv2.VideoCapture(0)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite("Face/face" + str(count) + '.jpg', gray[y:y + h, x:x + w])
        cv2.imshow('img', img)
        if count > 4:
            time.sleep (2)
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def save_pricame():
    w_size = []
    for i in range(1, 5):
        fn = "Face/face" + str(i) + ".jpg"
        # print 'load %s as ...' % fn
        img = cv2.imread(fn)
        sp = img.shape
        # print sp
        sz1 = sp[0]  # height(rows) of image
        sz2 = sp[1]  # width(colums) of image
        sz3 = sp[2]  # the pixels value is made up of three primary colors
        # print 'width: %d \nheight: %d \nnumber: %d' % (sz1, sz2, sz3)
        w_size.append(sz2)
    a = w_size
    b = max(w_size)
    c = a.index(b)
    c += 1
    print(c)
    return c;


def drawFace(face_rectangle,img):
    width=face_rectangle['width']
    top = face_rectangle['top']
    left = face_rectangle['left']
    height = face_rectangle['height']
    start = (left, top)
    end = (left + width, top + height)
    color = (55, 255, 155)
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)

def  cheack():
    detect_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    key = "Jza_grmxv0wRt1wBvd5645tSUgvvviqC"
    secret = "sYgt4gwzyVGOWj7_Nbbk7FxiPMwlU6tb"
    data = {"api_key": key, "api_secret": secret}
    faceId = "/home/pi/face_v2/face.jpg"
    files = {"image_file": open(faceId, "rb")}
    response = requests.post(detect_url, data=data,files=files)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    #face_token = req_dict['faces'][1]['face_token']
    #analyze_url = "https://api-cn.faceplusplus.com/facepp/v3/face/analyze"
    key = "Jza_grmxv0wRt1wBvd5645tSUgvvviqC"
    secret = "sYgt4gwzyVGOWj7_Nbbk7FxiPMwlU6tb"
    attributes = 'gender,age'
    faceId = "/home/pi/face_v2/face.jpg"
    data = {"api_key": key, "api_secret": secret,"return_attributes":attributes}
    files = {"image_file": open(faceId, "rb")}
    # file_2 = {"image_file2": open(faceId2, "rb")}
    response = requests.post(detect_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print req_dict
    #print response.json()
    gender = req_dict['faces'][0]['attributes']['gender']['value']
    print(gender)
    age = req_dict['faces'][0]['attributes']['age']['value']
    print(age)
    os.system("sudo python /home/pi/warn.py " + str(gender) +" "+ str(age))
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    face_rectangle = req_dict['faces'][0]['face_rectangle']
    # print(face_rectangle_1)
    img1 = cv2.imread(faceId)
    drawFace(face_rectangle, img1)
    img1 = cv2.resize(img1, (500, 500))
    cv2.imshow("img", img1)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()

def detect():
       detect_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
       key = "Jza_grmxv0wRt1wBvd5645tSUgvvviqC"
       secret = "sYgt4gwzyVGOWj7_Nbbk7FxiPMwlU6tb"
       data = {"api_key": key, "api_secret": secret}
       faceId = "Face/face" + str(save_pricame()) + ".jpg"
       files = {"image_file": open(faceId, "rb")}
       response = requests.post(detect_url, data=data,files=files)
       req_con = response.content.decode('utf-8')
       req_dict = JSONDecoder().decode(req_con)
       #face_token = req_dict['faces'][0]['face_token']




def text():
    camera()
    #fps = fps + fps_plus
    #detect()
    cheack()

while True:
    text()
    os.system("rm -rf Face")
    os.system("mkdir Face")
    os.system("rm -rf /home/pi/python2.7_guest/audio.mp3")
