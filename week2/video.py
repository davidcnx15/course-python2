# library name
import cv2
# cap = variable name
#  .videocapture()=function

cap = cv2.VideoCapture("week2/cat-f1.mp4")
# if while program is true (conditiolnal)
while True:
    # define a variable ret frame to keep the videocapture
    ret, frame = cap.read()
    if not ret:
        # show the vid
        break
    cv2.imshow("cat driving f1",frame)
    # ina  10 secondsnothing happends close
    if cv2.waitKey(30) & 0xff == ord("q"):
        break

cap.release()
cv2. destroyAllWindows()