import cv2
import numpy as np

# Define the range of skin color in HSV space
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

# Create a VideoCapture object to capture video from the camera
cap = cv2.VideoCapture(0)

# Loop over the frames of the video
while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply the skin color mask to the frame
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    masked = cv2.bitwise_and(frame, frame, mask=mask)

    # Find the contours of the hand region
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        # Get the largest contour (the hand)
        hand_contour = max(contours, key=cv2.contourArea)

        # Draw a bounding box around the hand
        x, y, w, h = cv2.boundingRect(hand_contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Determine whose hand it is based on skin color
        skin_color = hsv[y:y+h, x:x+w, :]
        mean_skin = np.mean(skin_color, axis=(0, 1))
        print(mean_skin[0])
        if mean_skin[0] < 10:
            # Hand belongs to person A
            cv2.putText(frame, "Person A", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        elif mean_skin[0] > 30:
            # Hand belongs to person B
            cv2.putText(frame, "Person B", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            # Hand color is ambiguous or unknown
            cv2.putText(frame, "Access Denied", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release the resources and close the windows
cap.release()
cv2.destroyAllWindows()
