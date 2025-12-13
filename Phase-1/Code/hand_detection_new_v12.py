import cv2
import mediapipe as mp
import pyautogui as pg
import wmi

screen_height, screen_width = pg.size()
screen_width = screen_width * 2
screen_height = screen_height * 0.6
c = wmi.WMI(namespace='wmi')
methods = c.WmiMonitorBrightnessMethods()[0]
current_brightness = 50
# print("Current brightness", current_brightness)
# initial position of the cursor
# global prev_cursor_pos
prev_cursor_pos = pg.position()

pg.FAILSAFE = False #disable fail safe from hand_functions import is_forefinger_open live video capture

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode = False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
                      
# FINGER SECTION START
# Index finger open or close check
def is_index_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y:
        return True
    else:
        return False
    
# Middle finger open or close check
def is_middle_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y:
        return True
    else:
        return False

# Ring finger open or close check
def is_ring_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y:
        return True
    else:
        return False
    
# pinky finger open or close
def is_pinky_finger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.PINKY_DIP].y:
        return True
    else:
        return False
        
# Thumb finger open or close
def is_thumb_finger_open(hand_landmarks):
    if not hand_landmarks:
        # print('False')
        return False
    if hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].x or hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mpHands.HandLandmark.THUMB_MCP].x or hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mpHands.HandLandmark.THUMB_CMC].x:
        # print('False')
        return True
    else:
        # print('True')
        return False

# FINGER SECTION END

# Gesture Identifier
def identify_gesture(finger_status, prev_finger_status, hand_landmarks): # fix this funtion
    global prev_cursor_pos
    # sound, scroll, brightness, zoom, mouse
    if (prev_finger_status == finger_status and finger_status !=  [True, False, True, True, True] \
        and finger_status !=  [True, True, True, True, False] and finger_status !=  [True, False, False, True, True] \
            and finger_status != [True, False, False, False, True] and finger_status != [True, True, True, False, False] and finger_status != [True, False, True, False, False]) :
        # what is this? 
        return prev_finger_status
    if prev_finger_status != finger_status:
        if prev_finger_status == [True, True, False, False, False]:
            print("Right Click Release")
            pg.mouseUp(button='right')
        elif prev_finger_status == [True, False, True, False, False]:
            print("Left Click Release")
            pg.mouseUp(button='left')
            
    if finger_status == [True, True, True, False, False]:
        print("Normal Mouse Mode")
        prev_cursor_pos = cursor_control(hand_landmarks, prev_cursor_pos)
    elif finger_status == [True, True, False, False, False]:
        if prev_finger_status != [True, True, False, False, False]: 
            print("Right Click")
            pg.mouseDown(button='right')
    elif finger_status == [True, False, True, False, False]:
        prev_cursor_pos = cursor_control(hand_landmarks, prev_cursor_pos)
        if prev_finger_status != [True, False, True, False, False]:
            print("Left Click")
            pg.mouseDown(button='left')
    elif finger_status == [True, False, True, True, True]:
        print("Volume Controls")
        volume_control(hand_landmarks)
    elif finger_status == [True, False, False, True, True]:
        print("Brightness Controls")
        brightness_control(hand_landmarks)
    elif finger_status == [True, True, True, True, False]:
        print("Scroll Controls")
        scroll_control(hand_landmarks)
    elif finger_status == [True, False, False, False, True]:
        print("Zoom Controls")
        zoom_control(hand_landmarks)
    elif finger_status == [False, False, False, False, False]:
        print("Closing app")
        close_app()
    elif finger_status == [False, True, True, False, False]:
        print("Press enter")
        press_enter()
    elif finger_status == [True, True, True, False, True]:
        print("Go back")
        press_back()
    else:
        print("Not assigned")
    prev_finger_status = finger_status
    return prev_finger_status
    
# CONTROL SECTION START
# Cursor movement controller
def cursor_control(hand_landmarks, prev_cursor_pos):
    # cursor_pos = pg.position() #bug
    # global screen_width, screen_height
    # screen_width = screen_width * 2
    # screen_height = screen_height * 2
    print("Height : ", screen_height, "Width : ", screen_width)
    cursor_pos = pg.position()
    '''x, y = int(hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x * screen_width), \
            int(hand_landmarks.landmark[mpHands.HandLandmark.WRIST].y * screen_height)'''
    x, y = int(hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].x * screen_width), \
            int(hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].y * screen_height)
    new_pos = (x, y)
        # Move the cursor based on the wrist position
    if new_pos is not None:
        # Calculate the difference in position since the last frame
        dx = (new_pos[0] - prev_cursor_pos[0]) 
        dy = (new_pos[1] - prev_cursor_pos[1]) 
        
        # Update the cursor position
        cursor_pos = (cursor_pos[0] + dx, cursor_pos[1] + dy)

        # Check if the cursor position is within the screen boundaries
        # cursor_pos = (
        #     min(max(cursor_pos[0], 0), screen_width - 1),
        #     min(max(cursor_pos[1], 0), screen_height - 1),
        # )

        # Move the cursor
        pg.moveTo(*cursor_pos)

        # Save the current cursor position
        prev_cursor_pos = cursor_pos
    return prev_cursor_pos

# Volume controller
def volume_control(hand_landmarks):
    '''
    pointer = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].y * screen_height
    if pointer < screen_height / 2 - 200:
        print("p<s => pointer: ", pointer, "screen_height/2: ", screen_height/2)
        pg.press('volumeup')
    elif pointer > screen_height / 2 + 200:
        print("p>s => pointer: ", pointer, "screen_height/2: ", screen_height/2)
        pg.press('volumedown')
    '''
    knob = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y
    if knob < 0.4:
        print("Volume Up")
        pg.press('volumeup')
    elif knob > 0.5:
        print("Volume Down")
        pg.press('volumedown')

    # increase volume based on the distance from the center of the screen

# Brightness controller
def brightness_control(hand_landmarks):
    global current_brightness
    bright = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y
    print("Current Brightness: ", current_brightness)
    if bright < 0.4:
        print("bright Increase")
        current_brightness += 10
        current_brightness = min(100, current_brightness)
        methods.WmiSetBrightness(current_brightness, 0)
    elif bright > 0.5:
        print("bright decrease")
        current_brightness -= 10
        current_brightness = max(0, current_brightness)
        methods.WmiSetBrightness(current_brightness, 0)
        
# Scroll controller
def scroll_control(hand_landmarks):
    scroll_wheel = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_PIP].y

    height, width, _ = image.shape
    # calculate the distance between the middle finger pip and the center of the camera
    distance = int((0.5 - scroll_wheel) * height)

    # scroll up or down based on the position of the middle finger pip
    if scroll_wheel < 0.4:
        pg.scroll(distance)
    elif scroll_wheel > 0.5:
        pg.scroll(distance)

# Zoom controller
def zoom_control(hand_landmarks):
    # print("Zoom")
    zoomer = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y
    if zoomer < 0.4:
        print("Zoom In")
        pg.hotkey('ctrl', '+')
    elif zoomer > 0.5:
        print("Zoom out")
        pg.hotkey('ctrl', '-')

# CONTROL SECTION END

# ADDITIONAL CONTROLS START

# Closing appication
def close_app():

    print("Closing app")
    pg.hotkey('alt', 'f4')

# Press 'enter'
def press_enter():
    print("Pressing enter")
    pg.press('enter')

# Press back

def press_back():
    print("Pressing back")
    # pg.press('backspace')
    pg.hotkey('alt', 'left')
# ADDITIONAL CONTROLS END

mpDraw = mp.solutions.drawing_utils
prev = "None"
isFlipped = False
booting = True
screenWidth, screenHeight = pg.size()
print("width is", screenWidth, screenHeight)

prev_finger_status = [False, False, False, False, False]

print("Starting Hand Detection")
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
        # for (hand, handLms) in itertools.zip_longest(results.multi_handedness, results.multi_hand_landmarks):
        #     print("hand : ", hand)
        #     print("handLms : ", handLms)
            
        if(results.multi_handedness[0].classification[0].label == "Right"):
            cv2.putText(image, "Right hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, ( 0,255, 0), 2)
            if(prev != "Right"):
                prev = "Right"
        else:
            cv2.putText(image, "Left hand detected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
            if(prev != "Left"):
                prev = "Left"
        
        # handLms = results.multi_handedness[0].landmark[0]
        handLms = results.multi_hand_landmarks[0]
        # print("handLms : ", handLms.landmark[0])

        
        is_index_open = is_index_finger_open(handLms)
        # print('Index finger:', is_index_open) 

        is_middle_open = is_middle_finger_open(handLms)
        # print('Middle finger:', is_middle_open)

        is_ring_open = is_ring_finger_open(handLms)
        # print('Ring finger:', is_ring_open)

        is_pinky_open = is_pinky_finger_open(handLms)
        # print('Pinky finger:', is_pinky_open)

        # is_thumb_open = is_thumb_finger_open(handLms)
        # print('Thumb finger:', is_thumb_open)
        # is_thumb_open = False
        is_thumb_open = is_thumb_finger_open(handLms)
        # print("thumb finger:", is_thumb_open)
        # print("\n")

        # cursor_move_with_wrist(handLms, prev_cursor_pos)
        finger_status = [is_thumb_open, is_index_open, is_middle_open, is_ring_open, is_pinky_open]
        prev_finger_status = identify_gesture(finger_status, prev_finger_status, handLms)

        prev_cursor_pos = pg.position()

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