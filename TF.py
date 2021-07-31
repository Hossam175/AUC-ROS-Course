#!/usr/bin/env python

import rospy
import math
import tf
from geometry_msgs.msg import Twist
from nav_msgs.mag import Odometry



print("roll-pitch-yaw conversation to quaternions")

roll = math.radians(30)
pitch = math.radians(40)
yaw = math.radians(50)

print('roll = ',math.degrees(roll),'pitch = ',math.degrees(pitch),'yaw = ',math.degrees(yaw))

quaternion = tf.transformations.quaternion_from_euler(roll,pitch,yaw)

for i in range(4):
	print(quaternion[i])




    
    


