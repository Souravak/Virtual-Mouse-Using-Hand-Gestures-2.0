import cv2
import mediapipe as mp
# import pyautogui as pg
import PIL
import time
import itertools
# import numpy as np #not used
from datetime import datetime
import math
# import screen_brightness_control as sbc
# import wmi
# screen_width, screen_height = pg.size()
# brightness = int(sbc.get_brightness()[0])
# brightnessController = wmi.WMI(namespace='wmi')
# brightnessMethod = brightnessController.WmiMonitorBrightnessMethods()[0]
# currentBrightness = wmi.WMI(namespace='wmi').WmiMonitorBrightness()[0]
# global cursor_pos
# global prev_cursor_pos
# prev_cursor_pos = pg.position()
# cursor_pos = pg.position()
# prev_cursor_pos = cursor_pos
 
# wrist_pos = None

# pg.FAILSAFE = False #disable fail safe
# from hand_functions import is_forefinger_open
# live video capture

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode = False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)

mpDraw = mp.solutions.drawing_utils
prev = "None"
isFlipped = False
booting = True
# screenWidth, screenHeight = pg.size()
# print("width is", screenWidth, screenHeight)
global prev_cursor_pos
# prev_cursor_pos = pg.position()
prev_finger_status = [False, False, False, False, False]
while True:
    success, image = cap.read()
    print("Image shape", image.shape)
    # flip correction
    image = cv2.flip(image, 1)    # <--- comment this to flip the image

    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    # checking whether a hand is detected
    if not results.multi_hand_landmarks:
        if(prev != "None"):
            print("No hands detected")
            # print no hand detected on image
            prev = "None"

        cv2.putText(image, "No hands detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    else:
        for (hand, handLms) in itertools.zip_longest(results.multi_handedness, results.multi_hand_landmarks):
            ############################################################################
            
            x1,y1, = handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].x, handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y
            x2,y2 = handLms.landmark[mpHands.HandLandmark.WRIST].x ,handLms.landmark[mpHands.HandLandmark.WRIST].y
            z1 = math.sqrt((y2-y1)**2 + (x2-x1)**2)

            x11,y11 = handLms.landmark[mpHands.HandLandmark.THUMB_TIP].x, handLms.landmark[mpHands.HandLandmark.THUMB_TIP].y
            x22,y22 = handLms.landmark[mpHands.HandLandmark.WRIST].x ,handLms.landmark[mpHands.HandLandmark.WRIST].y
            z11 = math.sqrt((y22-y11)**2 + (x22-x11)**2)

            print(z1/z11)

            # print(math.sqrt((y2-y1)**2 + (x2-x1)**2)) 
            ############################################################################
            if(hand.classification[0].label == "Right"):
                cv2.putText(image, "Right hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, ( 0,255, 0), 2)
                if(prev != "Right"):
                    print("right hand detected")
                    prev = "Right"
            else:
                cv2.putText(image, "Left hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
                if(prev != "Left"):
                    print("left hand detected")
                    prev = "Left"
    cv2.imshow("Output", image)
    
    cv2.waitKey(1)
    
