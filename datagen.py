import cv2
import time
cpt = 0
maxFrames = 850 # if you want 5 frames only.

cap=cv2.VideoCapture('datavid.mp4')

while cpt < maxFrames:
    _,frame = cap.read()
    cv2.imshow("test window", frame) # shows image in window
    cv2.imwrite("picss/%d.png" %cpt, frame)
    time.sleep(0.5)
    cpt += 1
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()