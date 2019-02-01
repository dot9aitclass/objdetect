import PIL as image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import cv2
name="newpic"
i=1
cap=cv2.VideoCapture(1)
while True:
    ret,frame=cap.read()
    for i in xrange(480):
        frame[i][320]=[0,0,255]
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL)
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(5)== ord('c'):
        i=i+1
        new=name+str(i)+".jpg"
        print new
        cv2.imwrite(new,frame)
cv2.destroyAllWindows()
cap.release()
#22.5=x=57.15cm
#15=y=38.1cm