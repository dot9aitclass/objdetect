import numpy as np
import cv2 as cv
area=[]
avarea=[]
kernel = np.ones((5,5),np.uint8)
cap=cv.VideoCapture(1)
ret,im=cap.read()
print np.size(im,0),np.size(im,1)
imgray = im #cv.cvtColor(im, cv.COLOR_BGR2GRAY)
imgray = cv.morphologyEx(imgray, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(imgray, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(imgray, cv.MORPH_CLOSE, kernel)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
thresh=cv.Canny(imgray,100,200)
cv.imshow("frame",thresh)
cv.waitKey()
cv.destroyAllWindows()
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
        area.append(cv.contourArea(contours[i]))
(x,y),radius = cv.minEnclosingCircle(contours[0])
center = (int(x),int(y))
r = int(radius)
#cv.drawContours(im, contours, -1 , (0,0,255), 3)
for i in range(len(contours)):
        avarea.append(cv.contourArea(contours[i]))
        (x,y),radius = cv.minEnclosingCircle(contours[i])
        if radius > r:
                center = (int(x),int(y))
                r = int(radius)
                ind = i
(x,y),radius = cv.minEnclosingCircle(contours[ind])
center = (int(x),int(y))
radius = int(radius)
#cv.circle(im,center,radius,(0,255,0),2)
f=center[0]
s=center[1]
color=im[s][f]
cv.imshow("frame",im)
cv.destroyAllWindows()
print color
chsv=np.uint8([[color]])
colorhsv=cv.cvtColor(chsv,cv.COLOR_BGR2HSV)
colorhsv=colorhsv[0][0]
print colorhsv
while True:

        # Take each frame
        _, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_color = np.array([colorhsv[0]-10,50,50])
        upper_color = np.array([colorhsv[0]+10,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_color, upper_color)

        # Bitwise-AND mask and original image
        res = cv.bitwise_and(frame,frame, mask= mask)

        #cv.imshow('frame',frame)
        #cv.imshow('mask',mask)
        cv.imshow('res',res)
        break
thresh=cv.Canny(res,100,200)
im3, contours1, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(im, contours1, -1 , (0,0,255), 3)
for i in range(len(contours1)):
        area.append(cv.contourArea(contours1[i]))
(x,y),radius = cv.minEnclosingCircle(contours1[0])
center = (int(x),int(y))
r = int(radius)
for i in range(len(contours1)):
        avarea.append(cv.contourArea(contours1[i]))
        (x,y),radius = cv.minEnclosingCircle(contours1[i])
        if radius > r:
                center = (int(x),int(y))
                r = int(radius)
                ind = i
(x,y),radius = cv.minEnclosingCircle(contours1[ind])
center = (int(x),int(y))
radius = int(radius)
cv.circle(im,center,radius,(0,255,0),2)
print center[0],center[1]
cv.imshow("im3",im)
cv.waitKey()
"""rect = cv.minAreaRect(contours[ind])
box = cv.boxPoints(rect)
box = np.int0(box)
print box"""
#cv.drawContours(img,[box],0,(0,0,255),2)
while True:
        _, im = cap.read()
        cv.circle(res,center,radius,(0,255,0))
        cv.imshow("im3",res)
        if cv.waitKey(30)==27:
                break
cv.destroyAllWindows()
"""
cv.imshow("ed",thresh)
k=cv.waitKey()


maxval=max(area)


print len(area)
print ind
cv.drawContours(im, contours, -1 , (0,0,255), 3)

print x,y

cv.imshow("im",im)
k=cv.waitKey()"""
"""thresh=cv.Canny(thresh,100,200)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
        area.append(cv.contourArea(contours[i]))
(x,y),radius = cv.minEnclosingCircle(contours[0])
center = (int(x),int(y))
r = int(radius)
#cv.drawContours(im, contours, -1 , (0,0,255), 3)
for i in range(len(contours)):
        avarea.append(cv.contourArea(contours[i]))
        (x,y),radius = cv.minEnclosingCircle(contours[i])
        if radius > r:
                center = (int(x),int(y))
                r = int(radius)
                ind = i
(x,y),radius = cv.minEnclosingCircle(contours[ind])
center = (int(x),int(y))
radius = int(radius)
cv.circle(im,center,radius,(0,255,0),2)
f=center[0]
s=center[1]
color=im[s][f]
cv.imshow("frame",im)
if cv.waitKey(30)==27:
        break"""
