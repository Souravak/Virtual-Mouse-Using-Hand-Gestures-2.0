import cv2
import mediapipe as mp
import pyautogui as pg
import time
import itertools
import numpy as np #not used
# from hand_functions import is_forefinger_open
# live video capture

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
                      
def is_index_finger_open(hand_landmarks):
    
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y:
        print("INDEX OPEN")
        # print("INDEX TIP:",hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y)
        # print("INDEX DIP:",hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y)
        return True
    else:
        print("INDEX CLOSED")
        return False
    
def is_middle_finger_open(hand_landmarks):
    
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y:
        print("MIDDLE OPEN")
        # print("MIDDLE TIP:",hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y)
        # print("MIDDLE DIP:",hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y)
        return True
    
    else:
        print("MIDDLE CLOSED")
        return False
    

mpDraw = mp.solutions.drawing_utils
prev = "None"
isFlipped = False
booting = True
screenWidth, screenHeight = pg.size()
print("width is",screenWidth, screenHeight)
while True:
    success, image = cap.read()

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
            # print(hand)
            # print(handLms)
            # print(hand.classification[0].label)
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
                    
            is_index_open = is_index_finger_open(handLms)
            print('Index finger:', is_index_open)
            is_middle_open = is_middle_finger_open(handLms)
            print('Middle finger:', is_middle_open)


            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)



    '''
    if results.multi_hand_landmarks:    
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8 : #marking the tip of fore finger
                    cv2.circle(image, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                    print(cx, cy)

                    # scroll control
                    verticalScrollDistance =0
                    
                    if cy > 300:
                        verticalScrollDistance = cy - 300
                        # cy scroll speed increases with distance
                        pg.vscroll(verticalScrollDistance)
                    elif cy < 200:
                        verticalScrollDistance = cy - 200
                        pg.vscroll(verticalScrollDistance)
    
            
    '''


    

    cv2.imshow("Output", image)
    
    cv2.waitKey(1)
    


