#Here you can input an image and check whether the system recognizes it
import cv2
import numpy as np
import utlis
import torch
path = 'C:/Users/dell/OneDrive/Desktop/my ml model/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)
img = cv2.imread("13.jpeg")
imgResult = img
result = model(img)
frame = np.squeeze(result.render())
frame = cv2.resize(frame, (240, 480))

while True:
    cv2.imshow('frm', frame)
    if(cv2.waitKey(1) & 0xFF ==27):
        break
        #cv2.imshow('Vid',img)
    cv2.waitKey(1)
