# opencv is used for remembering  a face or an object
import cv2 
# numpy is for math deep drive(vectors,)
import numpy as np
# it will load in the image then project it
img=cv2.imread('week04/download-removebg-preview.png')
# if the image cant be found the code will dissmiss the code and say "image not found please check the file path"
if img is None:
    print("image not found please check the file path")
    exit()
# include kernel 3x3 to adjust the image to blur and brightness
kernel = np.array([[0, -1,0],
                  [-1 ,5 ,-1],
                  [0, -1, 0]])
# it will make it so that it doesnt lose quality
sharpened = cv2.filter2D(img, -1 ,kernel)

# it will show the sharpened image
cv2.imshow('Sharpened Image',sharpened)
# it waits for you to press a key
cv2.waitKey(0)
# if you press a key it will destraoy all windows
cv2.destroyAllWindows()


