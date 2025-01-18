import cv2
import time

# Ask user for preferred behavior
print("Choose your option:")
print("1. Take one photo and stop.")
print("2. Take photos with a cooldown period.")
user_choice = input("Enter 1 or 2: ")

# Initialize webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Initialize the first frame for motion comparison
ret, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_frame = cv2.GaussianBlur(prev_frame, (21, 21), 0)

# Variable to track time for cooldown (if user chooses cooldown option)
last_capture_time = time.time()

# Variable to track whether we've taken a photo already (if user chooses one-time photo)
photo_taken = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame.")
        break
    
    # Convert the current frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute the absolute difference between the current frame and previous frame
    delta_frame = cv2.absdiff(prev_frame, gray)

    # Threshold the delta image to highlight regions with significant changes
    thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill in holes and make contours clearer
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours (outlines) in the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If any contour is large enough, consider it significant motion
    for contour in contours:
        if cv2.contourArea(contour) < 500:  # Adjust the area threshold to detect large objects
            continue

        # Check user choice
        if user_choice == "1" and not photo_taken:
            # Take one photo and stop
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"motion_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Motion detected! Photo saved as {filename}")
            photo_taken = True  # Ensure only one photo is taken
            break

        elif user_choice == "2":
            # For cooldown, check if enough time has passed since the last photo
            current_time = time.time()
            if current_time - last_capture_time > 5:  # Cooldown of 5 seconds (adjust as needed)
                # Save the image
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = f"motion_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Motion detected! Photo saved as {filename}")
                
                # Update the last capture time
                last_capture_time = current_time

            # Draw a rectangle around the moving object
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the current frame with motion detection rectangles
    cv2.imshow("Motion Detection", frame)

    # Set the previous frame for the next iteration
    prev_frame = gray

    # Exit on pressing space bar
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # Space bar key
        print("Space bar pressed! Exiting...")
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
