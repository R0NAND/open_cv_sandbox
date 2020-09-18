import cv2
import numpy

cap = cv2.VideoCapture(0)

pedestrian_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_fullbody.xml')

while(True):
  ret, frame = cap.read()
  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  pedestrians = pedestrian_cascade.detectMultiScale(gray_frame, 1.3, 5)
  for (x,y,w,h) in pedestrians:
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


  cv2.imshow('webcam_feed', frame)

  if cv2.waitKey(16) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()
