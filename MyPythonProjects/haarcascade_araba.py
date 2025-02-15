import cv2

cap=cv2.VideoCapture("resimler_videolar/Trafik - Otoyol - Araçlar - Araba - Otomobil - Telifsiz video.mp4")
araba=cv2.CascadeClassifier("carr.xml")

while True:
    ret, frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=araba.detectMultiScale(gri,1.1,3)

    for x,y,w,h in cars:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow("1",frame)
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()