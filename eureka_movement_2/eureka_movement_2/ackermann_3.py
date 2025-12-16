#!/usr/bin/env python3

#Developed by Andrei Smirnov. 2024
#MSU Rover Team. Voltbro. NIIMech 

from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8MultiArray
from sensor_msgs.msg import JointState
import numpy as np
from math import atan, sqrt, pi
import rclpy
from rclpy.node import Node
#import pandas as pd
import math 


import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from eureka_movement_lib import *



wheel_diameter = 0.3
wheelbase = 0.76
track_width = 0.94


def main(args=None):
    rclpy.init()
    ack = ackermann(wheel_diameter, wheelbase, track_width)
    rclpy.spin(ack)

    
    ack.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
