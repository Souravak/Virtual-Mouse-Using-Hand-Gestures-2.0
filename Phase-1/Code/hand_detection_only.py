import cv2
import mediapipe as mp
import pyautogui as pg
import PIL
import time
import itertools
import numpy as np #not used
import math
import wmi
from datetime import datetime


pg.FAILSAFE = False #disable fail safe from hand_functions import is_forefinger_open live video capture

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
screenWidth, screenHeight = pg.size()
print("width is", screenWidth, screenHeight)
def dist(handLms):
    if handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y < handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y:
        print('true')
    else:
        print("false")

prev_finger_status = [False, False, False, False, False]
while True:
    success, image = cap.read()
    # flip correction
    image = cv2.flip(image, 1)    # <--- comment this to flip the image

    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    # checking whether a hand is detected
    if not results.multi_hand_landmarks:
        if(prev != "None"):
            # print no hand detected on image
            prev = "None"
        cv2.putText(image, "No hands detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    else:
        if prev=="None":
            pass
        for (hand, handLms) in itertools.zip_longest(results.multi_handedness, results.multi_hand_landmarks):
            
            if(hand.classification[0].label == "Right"):
                cv2.putText(image, "Right hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, ( 0,255, 0), 2)
                if(prev != "Right"):
                    prev = "Right"
            else:
                cv2.putText(image, "Left hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
                if(prev != "Left"):
                    prev = "Left"
            distance = dist(handLms)


        mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Output", image)
    
    cv2.waitKey(1)


# Description
'''
    current state : tracking wrist and moving cursor with it. 
    able to identify all gestures
    capable of right and left click
    adjest the volume_control funtion
    brightness control implemented(bug)
    scrolling completed
    Zooming completed
    brightness function bug fixed
    cursor movement bug fixing stage 2(boundary fixed)
    scroll function not scrolling up(fixed)
    added more gestures

    next state : add more gestures and add the thumb finger identification and functionalities
    add a timer to the gestures - if the gesture is not completed within a certain time, it is not registered(optional)

    current state : brightness control stuck (solution : set brightness after completing the gesture. ie if prev = cur = brightness condition then update brightness var else set brightness)

    scroll function contributed by Adithyan S P
'''