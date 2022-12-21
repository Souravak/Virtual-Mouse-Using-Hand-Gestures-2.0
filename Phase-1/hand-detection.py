# Load the essential libraries
import cv2
import mediapipe as mp
import time

# live video capture
cap = cv2.VideoCapture(0)
# 180 degree the visuals





mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)


mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

# prev = None
prev = "None"
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if(results.multi_hand_landmarks == None):
        if(prev != "None"):
            print("No hands detected")
            # print no hand detected on image
            prev = "None"

        cv2.putText(img, "No hands detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
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
                if(prev != "Right"):
                    print("left hand detected")
                    prev = "Right"
            else:
                if(prev != "Left"):
                    print("right hand detected")
                    prev = "Left"

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                #if id ==0:
                cv2.circle(img, (cx,cy), 1, (0,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #display fps
    # cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 4, (0,0,0), 1)
    # print the right or left hand

    cv2.imshow("Image", img)
    cv2.waitKey(1)