import cv2
import mediapipe as mp
import pyautogui as pg
import time
import numpy as np #not used
# live video capture
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
                      
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
    if(results.multi_hand_landmarks == None):
        if(prev != "None"):
            print("No hands detected")
            # print no hand detected on image
            prev = "None"

        cv2.putText(image, "No hands detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    else:
        # print("Hands detected")
        # detected_hand = results.multi_handedness[0].label
        # if (detected_hand == "left"):
        #     print("Left hand detected")
        # else :
        #     print("Right hand detected")
        # print(results.multi_handedness)
        # print the right or left hand
        for hand in results.multi_handedness:
            # print(hand.classification[0].label)
            if(hand.classification[0].label == "Right"):
                cv2.putText(image, "Right hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, ( 0,255, 0), 2)
                if(prev != "Right"):
                    print("right hand detected")
                    prev = "Right"
                    # show hand detected on image
            else:
                cv2.putText(image, "Left hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
                if(prev != "Left"):
                    print("left hand detected")
                    # show hand detected on image
                    prev = "Left"
    # print which hand is detected on the image. 


    if results.multi_hand_landmarks:    
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8 : #marking the tip of fore finger
                    cv2.circle(image, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                    # print the corrdinates of the tip of fore finger
                    print(cx, cy)
                    # move the mouse to the tip of fore finger
                    # problem here - invert camera
                    # pg.moveTo(cx, cy)
                    

                    # pointer movement
                    # pg.moveTo(cx, cy)
                    # x, y = pg.position()
                    # move the pointer in the x direction
                    # horizontalMoveDistance  = 0
                    # if x > 200:
                    #     horizontalMoveDistance = x - 200
                    #     pg.moveTo(horizontalMoveDistance , y, duration=0.2)
                    # elif x < 100:
                    #     horizontalMoveDistance  = x - 100
                    # pg.moveTo(horizontalMoveDistance , y,duration=0.2)
                    # else:


                    verticalScrollDistance =0
                    
                    if cy > 300:
                        verticalScrollDistance = cy - 300
                        # cy scroll speed increases with distance
                        pg.vscroll(verticalScrollDistance)
                    elif cy < 200:
                        verticalScrollDistance = cy - 200
                        pg.vscroll(verticalScrollDistance)
                    
                    
                    # else:
                        # no scroll
                    
                    # for youtube shorts
                    # if cy > 300:
                    #     verticalScrollDistance = cy - 300
                    #     # cy scroll speed increases with distance
                    #     pg.vscroll(20)
                    # elif cy < 200:
                    #     verticalScrollDistance = cy - 200
                    #     pg.vscroll(-20)
                    
                    

                    # click the mouse
                    # if cx < 100 and cy < 100:
                        # pg.click()
                        # time.sleep(0.5)

        mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Output", image)
    
    cv2.waitKey(1)
    


