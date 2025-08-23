# calling for library or modulecv2 (opencv)
import cv2
# cap=variable
# videocapture=function
cap = cv2.VideoCapture(0)
# if webcam isnt opened say its not open
if not cap.isOpened():
    raise IOError("its not open")
# while a function is true keep the video capture
while True:
    ret, frame = cap.read()
    # if cant find webcam close the program
    if not ret:
        break
    # if webcam wont work then close in 10 sec
    # if web cam work let it cook
    cv2.imshow("Webcam is available",frame)
    if cv2.waitKey(10) & 0xff == ord("q"):
        break
# if q pressed then close program
cap.release()
cv2. destroyAllwindows()
