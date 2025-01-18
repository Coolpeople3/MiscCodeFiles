import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize MediaPipe drawing utils for visualization
mp_drawing = mp.solutions.drawing_utils

# Start the webcam capture
cap = cv2.VideoCapture(0)

# Wait for a moment before starting
time.sleep(2)

# Get screen width and height
screen_width, screen_height = pyautogui.size()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB (MediaPipe works with RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get the hand landmarks
    results = hands.process(rgb_frame)

    # If hand landmarks are found
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw the hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the positions of specific landmarks (e.g., thumb, index finger, and middle finger)
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Convert landmark positions to pixel values
            h, w, _ = frame.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)

            # Draw circles on the thumb, index finger, and middle finger tips
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), -1)
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (middle_x, middle_y), 10, (0, 0, 255), -1)

            # Move the mouse cursor to the index finger position
            # Map the x, y coordinates to the screen size
            cursor_x = int(index_x * screen_width / w)
            cursor_y = int(index_y * screen_height / h)

            # Move the mouse cursor smoothly to the new position
            pyautogui.moveTo(cursor_x, cursor_y, duration=0.1)

            # Check if the thumb and middle finger are close enough to detect a snap (click)
            distance = math.sqrt((thumb_x - middle_x) ** 2 + (thumb_y - middle_y) ** 2)

            # If thumb and middle finger are close enough, simulate a click (snap)
            if distance < 40:  # You can adjust this threshold value
                pyautogui.click()
                print("Snap detected! Mouse clicked.")

    # Show the current frame with hand landmarks
    cv2.imshow("Finger Tracking and Snap Click", frame)

    # Exit on pressing the 'esc' key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
