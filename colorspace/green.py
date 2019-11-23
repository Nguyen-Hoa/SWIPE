import cv2
import numpy as np

#get image
image = cv2.imread('temp.jpg')

#convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#define range of green in HSV
#!! play with this to get better results!
lower_green = np.array([30,10,10])
upper_green = np.array([80,255,255])

#threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_green, upper_green)

#bitwise-AND mask and orginal image
res = cv2.bitwise_and(image, image, mask= mask)

cv2.imwrite('temp_result.jpg' ,res)