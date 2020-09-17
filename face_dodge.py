import numpy as np
import cv2
import math

class Bullet:
  def __init__(self, location, velocity, radius):
    self.location = location
    self.velocity = velocity
    self.radius = radius

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_defaulT.xml')


dodge_circle = [100,100,100] #x, y, radius, defaults to something big, so one must show their face

spawn_radius = 500
bullet_radius = 10
bullets = [Bullet()]

game_over = False


while(True):
  ret, frame = cap.read()
  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
  for (x,y,w,h) in faces:
    dodge_circle = [int(x + w/2),int(y + h/2), int(min(w/2, h/2))]
  
  frame = cv2.circle(frame,(dodge_circle[0], dodge_circle[1]),dodge_circle[2],(255,0,0),-1)

  for bullet in bullets:
    bullet.position[0] += bullet.velocity[0]
    bullet.position[1] += bullet.velocity[1]
    if math.sqrt((bullet.position[0] - dodge_circle[0])**2 + (bullet.position[1] - dodge_circle[1])**2) < dodge_circle[2] + bullet.radius:
      game_over = True

  if game_over == True:
    frame[:][:][:] = 0

  cv2.imshow('webcam_feed', frame)

  if cv2.waitKey(16) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()

  