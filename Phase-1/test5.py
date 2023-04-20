import cv2
import numpy as np

# Load the hand shape templates for person A and person B
template_a = cv2.imread("1-removebg-preview.png", 0)
template_b = cv2.imread("2-removebg-preview.png", 0)
template_a = cv2.resize(template_a, (0, 0), fx=0.5, fy=0.5)
template_b = cv2.resize(template_b, (0, 0), fx=0.5, fy=0.5)

# Define the shape matching threshold
threshold = 0.7

# Create a VideoCapture object to capture video from the camera
cap = cv2.VideoCapture(0)

# Loop over the frames of the video
while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Match the hand shape templates to the frame
    result_a = cv2.matchTemplate(gray, template_a, cv2.TM_CCOEFF_NORMED)
    result_b = cv2.matchTemplate(gray, template_b, cv2.TM_CCOEFF_NORMED)

    # Determine whose hand it is based on the best match
    min_val_a, max_val_a, _, _ = cv2.minMaxLoc(result_a)
    min_val_b, max_val_b, _, _ = cv2.minMaxLoc(result_b)
    if max_val_a > threshold and max_val_a > max_val_b:
        # Hand belongs to person A
        x, y = cv2.minMaxLoc(result_a)[3]
        w, h = template_a.shape[::-1]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Person A", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    elif max_val_b > threshold and max_val_b > max_val_a:
        # Hand belongs to person B
        x, y = cv2.minMaxLoc(result_b)[3]
        w, h = template_b.shape[::-1]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Person B", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    else:
        # Hand shape is ambiguous or unknown
        cv2.putText(frame, "Access Denied", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release the resources and close the windows
cap.release()
cv2.destroyAllWindows()
