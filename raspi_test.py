import cv2
import numpy

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  cv2.imshow('webcam_feed', frame)
  if cv2.waitKey(16) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()