#!/usr/bin/env python3
from __future__ import print_function
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
     count=0
     try:
       cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
     except CvBridgeError as e:
       print(e)
       
     while count <= 0: 
       cv2.imwrite("/home/locobot/interbotix_ws/src/image_detect_pkg/src/image/locobotFirebase/photos/lettuce.jpg", cv_image)
       cv2.waitKey(5)
       count=10
       
     
     return
       
     
def takePhoto():
   ic = image_converter()
   rospy.init_node('image_converter', anonymous=True)
   

