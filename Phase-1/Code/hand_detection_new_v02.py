import cv2
import mediapipe as mp
import pyautogui as pg
import PIL
import time
import itertools
import numpy as np #not used
from datetime import datetime
screen_width, screen_height = pg.size()
# global cursor_pos
# global prev_cursor_pos
# prev_cursor_pos = pg.position()
# cursor_pos = pg.position()
# prev_cursor_pos = cursor_pos

# wrist_pos = None

pg.FAILSAFE = False #disable fail safe
# from hand_functions import is_forefinger_open
# live video capture

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
                      


# Index finger open or close check
def is_index_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y:
        # print("INDEX OPEN")
        # print("INDEX TIP:",hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y)
        # print("INDEX DIP:",hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y)
        return True
    else:
        # print("INDEX CLOSED")
        return False
    
# Middle finger open or close check
def is_middle_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y:
        # print("MIDDLE OPEN")
        # print("MIDDLE TIP:",hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y)
        # print("MIDDLE DIP:",hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y)
        return True
    else:
        # print("MIDDLE CLOSED")
        return False

# Ring finger open or close check
def is_ring_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y:
        # print("RING OPEN")
        # print("RING TIP:",hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y)
        # print("RING DIP:",hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y)
        return True
    else:
        # print("RING CLOSED")
        return False
    
# pinky finger open or close
def is_pinky_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.PINKY_DIP].y:
        # print("PINKY OPEN")
        # print("PINKY TIP:",hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y)
        # print("PINKY DIP:",hand_landmarks.landmark[mpHands.HandLandmark.PINKY_DIP].y)
        return True
    else:
        # print("PINKY CLOSED")
        return False
        
# Thumb open or close check
def is_thumb_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].y:
        # print("THUMB OPEN")
        # print("THUMB TIP:",hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].y)
        # print("THUMB IP:",hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].y)
        return True
    else:
        # print("THUMB CLOSED")
        return False

def cursor_move_with_wrist(hand_landmarks, prev_cursor_pos):
    cursor_pos = pg.position()
    x, y = int(hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x * screen_width), \
            int(hand_landmarks.landmark[mpHands.HandLandmark.WRIST].y * screen_height)
    wrist_pos = (x, y)
        # Move the cursor based on the wrist position
    if wrist_pos is not None:
        # Calculate the difference in position since the last frame
        dx = (wrist_pos[0] - prev_cursor_pos[0]) * 1.5
        dy = (wrist_pos[1] - prev_cursor_pos[1]) * 1.5
        print("dx : ", dx)
        print("dy: ", dy)
        # Update the cursor position
        
        cursor_pos = (cursor_pos[0] + dx, cursor_pos[1] + dy)

        # Move the cursor
        pg.moveTo(*cursor_pos)

        # Save the current cursor position
        # prev_cursor_pos = cursor_pos
    # return prev_cursor_pos
    
mpDraw = mp.solutions.drawing_utils
prev = "None"
isFlipped = False
booting = True
screenWidth, screenHeight = pg.size()
print("width is", screenWidth, screenHeight)
global prev_cursor_pos
prev_cursor_pos = pg.position()

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
        
        now = datetime.now()
        if now.second%2 == 0:
            print("########################################")
            is_index_open = is_index_finger_open(handLms)
            print('Index finger:', is_index_open)

            is_middle_open = is_middle_finger_open(handLms)
            print('Middle finger:', is_middle_open)

            is_ring_open = is_ring_finger_open(handLms)
            print('Ring finger:', is_ring_open)

            is_pinky_open = is_pinky_finger_open(handLms)
            print('Pinky finger:', is_pinky_open)

            # is_thumb_open = is_thumb_finger_open(handLms)
            # print('Thumb finger:', is_thumb_open)
            print("\n")

            # wrist = handLms.landmark[mpHands.HandLandmark.WRIST]

            # # Move the cursor using PyAutoGUI
            # cursor_x = int(wrist.x * screen_width)
            # cursor_y = int(wrist.y * screen_height)
            # pg.moveTo(cursor_x, cursor_y)

        cursor_move_with_wrist(handLms, prev_cursor_pos)
        prev_cursor_pos = pg.position()

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
    


# current state : tracking wrist and moving cursor with it. But not moving to the top of the screen