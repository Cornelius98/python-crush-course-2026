import cv2

# Example
motion_sensor = 0
rediation_sensor = 0

while motion_sensor <= 10 and rediation_sensor <= 25:
    # Increment detection radius
    motion_sensor = motion_sensor + 1
    rediation_sensor = rediation_sensor + 1

    print("No intrusion")

    # Opening camera and alarm
    if (motion_sensor == 5 or rediation_sensor == 20):
        print("Intrusion detected, initializing camera and alarms....")
        print("Initializing.......")
        print("..................")

        # Open the default camera (usually index 0)
        cap = cv2.VideoCapture(0)

        # Check if camera opened successfully
        if not cap.isOpened():
            print("Error: Could not open camera")
            exit()

        # Loop to capture and display frames
        while True:
            # Read frame from camera
            ret, frame = cap.read()

            if not ret:
                print("Error: Can't receive frame")
                break

            # Display the frame
            cv2.imshow('Camera Feed', frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        cap.release()
        cv2.destroyAllWindows()
