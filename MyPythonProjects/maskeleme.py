import cv2
import numpy as np

image =cv2.imread("resimler_videolar/www.doktortakvimi.jpg")
hsv_image= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_red= np.array([0,40,40])
upper_red = np.array([10,255,255])
red_lower2 = np.array([170, 50, 50])
red_upper2 = np.array([180, 255, 255])

mask =cv2.inRange(hsv_image,lower_red,upper_red)
mask1 =cv2.inRange(hsv_image,red_lower2,red_upper2)

maskbirles = cv2.add(mask,mask1)

red_image =cv2.bitwise_and(image,image,mask=maskbirles)

cv2.imshow("img", image)
cv2.imshow("mask", mask)
cv2.imshow("red", red_image)

cv2.waitKey(0)
cv2.destroyAllWindows()