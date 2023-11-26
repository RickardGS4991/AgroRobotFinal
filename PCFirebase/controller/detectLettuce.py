import torch
import cv2
import numpy as np

def detectObjects(imagePath):
    modelHealth = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/labra/Desktop/LettuceDetect/model/lettuce.pt')

    frame = cv2.imread(imagePath)
    lettuceBoolean = False
    detectLettuce = modelHealth(frame)

    if detectLettuce.pred[0] is not None:
        for detection in detectLettuce.pred[0]:
            if detection[4] >= 0.70:
                lettuceBoolean = True
                break

    return lettuceBoolean

