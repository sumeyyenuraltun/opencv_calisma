import cv2
from skimage.feature import hog
from skimage import exposure

image=cv2.imread("resimler_videolar/GettyImages-1258889149-1f50bb87f9d54dca87813923f12ac94b.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,hogimage=hog(gray,visualize=True)
rescaled=exposure.rescale_intensity(hogimage,in_range=(0,10))

cv2.imshow("hog",hogimage)
cv2.imshow("orj",image)
cv2.imshow("rg", rescaled)

cv2.waitKey(0)
cv2.destroyAllWindows()


