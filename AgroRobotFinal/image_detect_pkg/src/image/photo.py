#!/usr/bin/env python3
from __future__ import print_function
import math
import random
from interbotix_xs_modules.locobot import InterbotixLocobotXS
 
import sys
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 
class image_converter:
   def __init__(self):
 
     self.bridge = CvBridge()
     self.image_sub = rospy.Subscriber("/locobot/camera/color/image_raw",Image,self.callback)

   
   def callback(self,data):
     p = 0
     number = 0

     kernel = np.ones((5,5), np.uint8)

     try:
       cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
       running = True
     except CvBridgeError as e:
       print(e)
       running = False
 
     (rows,cols,channels) = cv_image.shape

     imgHSV = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
     imgGray = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
     nameRandom = random.randint(0,5)

     if running == True:
        while number<10:
           name = "webcam"+str(nameRandom)+".jpg"
           cv2.imwrite(name, imgGray)
           print("Take photo sucessfully")
           number+=1
     else:
        print("error")
     
     cv2.imshow("Image normal", cv_image)
     cv2.imshow("Image Gray", imgGray)
     cv2.imshow("Image HSV", imgHSV)
     cv2.waitKey(3)
 
def main(args):
   ic = image_converter()
   rospy.init_node('image_converter', anonymous=True)
   try:
     rospy.spin()
   except KeyboardInterrupt:
    print("Shutting down")
   cv2.destroyAllWindows()
if __name__ == '__main__':
       main(sys.argv)
