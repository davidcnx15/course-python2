# opencv is used for recognising or remembering a face of an object
import cv2
# numpy is used for math deep drives (vectors)
import numpy as np
# math is for calculating using basic signs like + , - , x , /
import math
# memorises the image we downloaded
img = cv2.imread("week04/download-removebg-preview.png")
# it will preprocess the variable image
def preprocess(img):
# turns the imgae in to gray scale or a black an white picture
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# it will blur the black and white image 
    blur = cv2.GuassianBLur(gray,(15,15),0)
# it will remove the black spots on the image and leave the white spots to recognise the images shape
    ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY)

    k = cv2.getStructureingElement(cv2.MORPH_ELLIPSE,(3, 3))

    opened = cv2.morphologyEx(th, cv2.MORPH_OPEN, k, interactions=1)

    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, k, interactions=1 )    
    return closed


