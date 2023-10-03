import cv2
import os 
import random 
import numpy as np
from matplotlib import pyplot as plt
import uuid

vid = cv2.VideoCapture(0)
while vid.isOpened():
    ret, frame = vid.read()
    frame = frame[150:400,250:500,:]
    cv2.imshow('Image Collection',frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    if cv2.waitKey(1) & 0XFF == ord('a'):
        image_path = './anchor/image_{}.jpg'.format(uuid.uuid1())
        cv2.imwrite(image_path,frame)
    if cv2.waitKey(1) & 0XFF == ord('p'):
        image_path = './positive/image_{}.jpg'.format(uuid.uuid1())
        cv2.imwrite(image_path,frame)
vid.release()
cv2.destroyAllWindows()


