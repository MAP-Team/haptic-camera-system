import numpy as np
import cv2

cap1 = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop) 
ret,frame = cap1.read(1) # return a single frame in variable `frame`

cv2.imwrite('./media/c3.png',frame) # writes photos to media directory 

# cap2 = cv2.VideoCapture(2) # video capture source camera (Here webcam of laptop) 
# ret,frame = cap2.read(2) # return a single frame in variable `frame`

# cv2.imwrite('./media/c2.png',frame) # writes photos to media directory 
