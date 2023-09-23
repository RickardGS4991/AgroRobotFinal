import math
import random
from interbotix_xs_modules.locobot import InterbotixLocobotXS

import cv2
print("Package imported")
videoSource = 2
cap = cv2.VideoCapture(videoSource)

while True:
    #cap.open(videoSource)  # necesario para apertura de cámara ip
    read, img = cap.read()
    number = random.randint(0,100)
    name = "webcam"+str(number)+".jpg"
    cv2.imwrite(name, img)
    if read == True:
    	cv2.imshow("webcam.jpg", img)
    	print("Take photo sucessfully")
    else:
    	print("error")
    if cv2.waitKey(1) & 0xFF == 27:   # ESC ?
        break
