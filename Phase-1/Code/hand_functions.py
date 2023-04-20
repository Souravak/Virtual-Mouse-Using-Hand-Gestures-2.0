import cv2
import mediapipe as mp
import pyautogui as pg
import time
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
def is_forefinger_open(hand_landmarks):
    if not hand_landmarks:
        return False
    index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    if index_finger.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y and \
       thumb.x > index_finger.x and \
       abs(thumb.y - index_finger.y) < abs(index_finger.x - thumb.x):
        return True
    else:
        return False