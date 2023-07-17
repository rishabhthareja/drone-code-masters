import cv2
from djitellopy import Tello
from time import sleep
import numpy as np

# Global variable for battery threshold
BATTERY_THRESHOLD = 20

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
        img = cv2.resize(frame, (640, 480))
        # Make a copy to draw contour outline
        input_image_cpy = img.copy()

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of red color in HSV
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])

        # define range of green color in HSV
        lower_green = np.array([40, 20, 50])
        upper_green = np.array([90, 255, 255])

        # define range of blue color in HSV
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # create a mask for red color
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        # create a mask for green color
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        # create a mask for blue color
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

        # find contours in the red mask
        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # find contours in the green mask
        contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # find contours in the blue mask
        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # loop through the red contours and draw a rectangle around them
        for cnt in contours_red:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img, 'Red', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # loop through the green contours and draw a rectangle around them
        for cnt in contours_green:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, 'Green', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # loop through the blue contours and draw a rectangle around them
        for cnt in contours_blue:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, 'Blue', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('Color Recognition Output', img)

        # Close video window by pressing 'x'
        if cv2.waitKey(1) & 0xFF == ord('x'):
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