# ATRV-JR Gazebo
This repository is a ROS2 Package for using the virtual model of the ATRV-JR robot in custom simulation worlds.

This package was made for use in the University of Massachusetts Lowell HRI Lab, and its authors are Logan Sehr and Ted Boswell.

## Prerequisites
This package uses ROS2 Humble and its functionality has not been tested across other ROS versions.

To spawn ATRV-JR, a gazebo world must be launched before the spawn_junior.launch.py file for the robot to appear inside the simulation.

## Collaborative Package
This package extensively uses URDF files from the atrvjr_description package which can be found [`here`](https://github.com/logansehr11/atrvjr_description).