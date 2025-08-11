import cv2
import numpy as np
import utlis
import torch
path = 'C:/Users/khushpreet/OneDrive/Documents/model-k[1]/my ml model/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)
curveList = []
avgVal=10
 
def getLaneCurve(img,display=2):
 
    imgCopy = img.copy()
    imgResult = img.copy()
    #### STEP 1 Thresholding
    imgThres = utlis.thresholding(img) # I/O is image
    
    #### STEP 2  Getting the warped image
    hT, wT, c = img.shape
    points = np.array([[110,  80],[370,  80],[ 20, 214],[460, 214]])
    imgWarp = utlis.warpImg(imgThres,points,wT,hT)
    #### STEP 3
    middlePoint,imgHist = utlis.getHistogram(imgWarp,display=True,minPer=0.5,region=4)
    curveAveragePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint
 
    #### SETP 4 Averaging,to reduce noise
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))
    curve2 = "center"
    if(curve>-3):
        curve2 = "right"
    elif(curve<-3):
        curve2="left"
    else:
        curve2 = "center"

    #### STEP 5
    if display != 0:
        imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 255, 0, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = img
        result = model(img)
        frame = np.squeeze(result.render())
        cv2.putText(imgResult, curve2, (10,50), cv2.FONT_HERSHEY_DUPLEX , 1, (255, 0, 0), 1)

    if display == 1:
        cv2.imshow('Resutlt', imgResult)
        cv2.imshow('histogram', imgHist)
        cv2.imshow('warpinv', imgInvWarp)
        cv2.imshow('warp', imgWarp)
        cv2.imshow('lane', imgLaneColor)
    return curve
 
 
if __name__ == '__main__':
    cap = cv2.VideoCapture(r'C:\Users\khushpreet\OneDrive\Documents\model-k[1]\my ml model\vid6.mp4')
    while True:
        success, img = cap.read()

        
        if not success:
            print("Failed to read frame")
            break
        img = cv2.resize(img,(480,240))
        curve = getLaneCurve(img,display=1)
        if(cv2.waitKey(1) & 0xFF ==27):
            break
        cv2.imshow('Vid',img)
        cv2.waitKey(1)