"""
Project: DJI Tello Drone - Takeoff, Hover, and Land
Author: Rishabh Thareja

Description:
This Python code controls a DJI Tello drone using the djitellopy library. The code instructs the drone to take off, hover in the air for 2 seconds, and then land gracefully.

Please make sure to connect the drone to a Wi-Fi network before executing the code. Ensure that you have enough open space and follow all safety guidelines while operating the drone.

Note: This code assumes you have already installed the djitellopy library.

"""

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
