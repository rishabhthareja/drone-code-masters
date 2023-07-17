import cv2
from djitellopy import Tello
from time import sleep

# Global variable for battery threshold
BATTERY_THRESHOLD = 30

# Create a Tello object
drone = Tello()

# Connect to the Tello drone
drone.connect()

# Check the battery percentage
battery_percentage = drone.get_battery()

# Check if the battery percentage is above the threshold
if battery_percentage > BATTERY_THRESHOLD:

    # battery status
    print("The battery percentage is: ", str(battery_percentage))
    # Take off the drone
    #drone.takeoff()

    # Start video stream
    drone.streamon()

    # Create a VideoCapture object to capture the video stream
    cap = cv2.VideoCapture('udp://0.0.0.0:11111')

    # Check if video capture is successful
    if not cap.isOpened():
        print("Failed to open video stream")
        drone.streamoff()
        drone.land()
        sleep(3)
        drone.end()
        exit()

    # Create a new window to display the video feed
    cv2.namedWindow("Tello Live Video Feed", cv2.WINDOW_NORMAL)

    # Read and display video frames until 'q' is pressed
    while True:
        ret, frame = cap.read()

        if not ret:
            break
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #edges = cv2.Canny(gray_image, 100, 200)

        # Display the frame in the window
        cv2.imshow("Tello Live Video Feed", gray_image)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()

    # Stop video stream, land the drone, and disconnect from the drone
    drone.streamoff()
    sleep(5)
    drone.land()
    sleep(5)
    drone.end()
else:
    print(f"Battery percentage is below {BATTERY_THRESHOLD}. Cannot start video feed.")