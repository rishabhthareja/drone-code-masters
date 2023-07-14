from time import sleep
from djitellopy import Tello

# Create a Tello object
drone = Tello()

# Connect to the Tello drone
drone.connect()

# Check the battery percentage
battery_percentage = drone.get_battery()

# Check if the battery percentage is above 80
if battery_percentage > 80:
    # Take off the drone
    drone.takeoff()

    # Hover for 2 seconds
    sleep(2)

    # Land the drone
    drone.land()
else:
    print("Battery percentage is below 80. Cannot execute the program.")

# Disconnect from the drone
drone.end()