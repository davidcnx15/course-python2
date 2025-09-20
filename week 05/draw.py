import cv2

import numpy as np

img = np.ones((600, 800, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (50, 50), (250, 200), (255, 0, 0), -1)
cv2.circle(img, (40,150), 70, (0, 0, 255))
pts = np.array([[550, 220], [700, 60], [750, 220]], np.int32)
cv2.fillPoly(img, [pts], (0, 0, 255))
for x in range(100, 750, 120):
    cv2.circle(img, (x, 200), 30 , (0, 0, 0), -1)

cv2.putText(img, "testing shapes and pictures", (50, 420),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (50, 50, 50,), 2)
cv2.imwrite("shapes_test.png",img)
