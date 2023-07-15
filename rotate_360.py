"""
Project: DJI Tello Drone - Takeoff, Rotate, and Land
Author: Rishabh Thareja

Description:
This Python code controls a DJI Tello drone using the djitellopy library. The code instructs the drone to take off, perform a 360-degree rotation, hover in the air for 2 seconds, and then land gracefully.

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
if battery_percentage > 30:
    print("The battery percentage is: ", battery_percentage)
    # Take off the drone
    drone.takeoff()
    print("Drone is taking off...")
    # The delay of 5 seconds is added to avoid any
    # failed communication between laptop/PC and tello drone
    sleep(5)

    # Rotate the drone 360 degrees
    drone.rotate_clockwise(360)
    print("Drone is rotating 360 degrees...")

    # Hover for 2 seconds
    sleep(2)
    print("Drone is hovering...")

    # Land the drone
    drone.land()
    print("Drone is landing...")
else:
    print("Battery percentage is below 80. Cannot execute the program.")

# Disconnect from the drone
drone.end()
print("Program execution completed.")