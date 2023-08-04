import cv2
import numpy as np

# reading video

cap=cv2.VideoCapture("vtest.avi")

res,frame1=cap.read()
res,frame2=cap.read()

while(1):

    diff=cv2.absdiff(frame1,frame2)

    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)

    blur=cv2.GaussianBlur(gray,(3,3),0)

    _,thres=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    dilated=cv2.dilate(thres,None,iterations=3)

    countour,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


    for i in countour:
        (x,y,w,h)=cv2.boundingRect(i)

        if cv2.contourArea(i)<1400:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(frame1,"Status".format("Movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(2,0,255),3)


    cv2.imshow("feed",frame1)

    frame1=frame2
    _,frame2=cap.read()

    if cv2.waitKey(35)==27:
        break

cv2.destroyAllWindows()
cap.release()
