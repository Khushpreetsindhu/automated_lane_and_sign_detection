#This is for live detection of signs
import cv2
import numpy as np
import torch
path = 'C:/Users/dell/OneDrive/Desktop/my ml model/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (1020, 500))
    result = model(frame)
    frame = np.squeeze(result.render())
    if(cv2.waitKey(1) & 0xFF ==27):
        break
    cv2.imshow('FRAME', frame)

cap.release()
cv2.destroyAllWindows()