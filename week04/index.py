# opencv is used for remembering  a face or an object
import cv2 
# numpy is for math deep drive(vectors,)
import numpy as np

img=cv2.imread('week04/download-removebg-preview.png')

if img is None:
    print("image not found please check the file path")
    exit()

kernel = np.array([[0, -1,0],
                  [-1 ,5 ,-1],
                  [0, -1, 0]])

sharpened = cv2.filter2D(img, -1 ,kernel)


cv2.imshow('Sharpened Image',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()


