# tungtungtralalelobombordilobananinipororodogamaradundunmateocelesteicusdicusbambiniorangutiniassasinipuchinosahur
# 
import cv2

# name of library
img = cv2.imread("week 01/download-removebg-preview.png")
# 
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# show an imagge
cv2.imshow("Show an image", gray)
# wait key is waiting for u to press button to do action
#destroy all windows is deleting the window
cv2.waitKey(0)
cv2.destroyAllWindows()
