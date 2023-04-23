import cv2
import mediapipe as mp

# Create a VideoCapture object to capture video from the camera
cap = cv2.VideoCapture(0)

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Use MediaPipe hands to detect hands in the frame
    results = hands.process(frame_rgb)

    # Check if a hand was detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
        # Get the landmarks of the first detected hand
            if not hand_landmarks:
                print('False')
            if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x or hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x or hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x:
                print('False')
            else:
                print('True')

    # Check for the 'q' key to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
