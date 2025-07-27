import cv2
image=cv2.imread("download.jpg")
cv2.imshow('show',image)
cv2.imwrite('photo.png',image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
