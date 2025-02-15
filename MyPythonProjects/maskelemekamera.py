import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#mavi renk için renk maskeleme
while(1):
    ret,frame=cap.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    alt_sinir=np.array([75,100,100])
    ust_sinir=np.array([130,255,255])

    mask=cv2.inRange(hsv,alt_sinir,ust_sinir)

    cv2.imshow("resim",frame)
    cv2.imshow("maskelenmis",mask)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break


cv2.destroyAllWindows()



