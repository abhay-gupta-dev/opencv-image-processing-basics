import cv2
img=cv2.imread("abhi.jpeg")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(grey,100,200)
cv2.imshow("Original",img)
cv2.imshow("Gray",grey)
cv2.imshow("Edges",edges)
cv2.waitKey(0)  
cv2.destroyAllWindows()
