# import means calling libraries or modules as cv2
import cv2

print(cv2.__version__)
# the name of library [cv2] | . the name of function ()

img = cv2.imread("week 01/download-removebg-preview.png")

# .imwrite() is used in images
# include 2 argument (1 the name of new file ["new.png"],2 image [variable name])
cv2.imwrite("new.png" , img)

#.imshow()show images
cv2.imshow("show an image" , img)
# waitkey(0)press any button for ...
#  .destroyAllWindows() Close a window ()
cv2.waitKey(0)
cv2.destroyAllWindows