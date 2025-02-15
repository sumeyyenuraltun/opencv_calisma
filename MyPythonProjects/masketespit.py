import cv2

cap =cv2.VideoCapture(0)

fase_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
mouth = cv2.CascadeClassifier("mouth.xml")

while(1):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1) #aynalı geliyo ters çevirdik

    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    fasec=fase_cascade.detectMultiScale(gri,1.1,8)
    if len(fasec) ==0:
        cv2.putText(frame,"yuz tespit edilmedi",(40,40),cv2.FONT_ITALIC,1,(255,255,255),2)
    else :
        for x,y,w,h in fasec:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            roi_gri=gri[y:y+h,x:x+w]
            mout=mouth.detectMultiScale(roi_gri,1.4,15)

            if len(mout)==0:
                cv2.putText(frame, "maske var", (40, 40), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
            else:
                for x1, y1, w1, h1 in mout:
                    cv2.rectangle(frame,(x1+x,y1+y),(x1+w1+x,y1+y+h1),(111,111,111),3)
                    cv2.putText(frame, "maske yok", (40, 40), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    cv2.imshow("ilk hal", frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
