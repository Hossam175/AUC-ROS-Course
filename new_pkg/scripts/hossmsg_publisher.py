#!/usr/bin/env python

import rospy
from new_pkg.msg import hoss

def talker():

pub = rospy.publisher('msg_topic' , hoss, queue_size=10)

ros.init_node('node1' , anonymous=True)

rate = rospy.rate(1)
sensor = hoss()
number.real = 1.5
number.imga = 1


i = 0

while not rospy.is_shutdown():


rospy.loginfo("I publish:")
rospy.loginfo(number)
pub.publish(number)
rate.sleep()
i = i+1

