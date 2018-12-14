import cv2

img = cv2.imread('bill.jpg')
print img.shape
# img = cv2.resize(img, (360,420))
# img = img[50:1000,20:420]
# cv2.imwrite("bill.jpg", img)
while True:
	cv2.imshow("bill", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()