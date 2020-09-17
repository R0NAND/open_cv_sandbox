import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)


# Create a black image, a window
cv2.namedWindow('frame')

# create trackbars for color change
cv2.createTrackbar('threshold','frame',195, 255,nothing)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 


    # threshold image
    t = cv2.getTrackbarPos('threshold','frame')
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray_frame, t, 255, cv2.THRESH_OTSU)

    # split into different colored frames
    red_green = np.zeros(frame.shape)
    red_green[np.where((mask==[0]))] = [0,1,0]
    red_green[np.where((mask==[255]))] = [0,0,1]
    purple_yellow = np.zeros(frame.shape)
    purple_yellow[np.where((mask==[0]))] = [1,0,1]
    purple_yellow[np.where((mask==[255]))] = [0,1,1]
    blue_orange = np.zeros(frame.shape)
    blue_orange[np.where((mask==[0]))] = [0,0.5,1]
    blue_orange[np.where((mask==[255]))] = [1,0,0]
    green_red = np.zeros(frame.shape)
    green_red[np.where((mask==[255]))] = [0,1,0]
    green_red[np.where((mask==[0]))] = [0,0,1]
    yellow_purple = np.zeros(frame.shape)
    yellow_purple[np.where((mask==[255]))] = [1,0,1]
    yellow_purple[np.where((mask==[0]))] = [0,1,1]
    orange_blue = np.zeros(frame.shape)
    orange_blue[np.where((mask==[255]))] = [0,0.5,1]
    orange_blue[np.where((mask==[0]))] = [1,0,0]

    # combine colored frames into 1
    frame = np.vstack((np.hstack((red_green, purple_yellow, blue_orange)), np.hstack((yellow_purple, orange_blue, green_red)))) 

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()