#!/usr/bin/env python

import rospy
from hossam_hoss.msg import auc
import random

def talker():

#create a new publisher. we specify the topic name, then type of message then the queue size
pub = rospy.Publisher('sensor_topic', auc, queue_size=10)
rate = rospy.Rate(1) # 1hz

def sensor_callback(sensor_message):
    rospy.loginfo("new data received: (%d, %.2f ,%.2f)", 
        sensor_message.real,sensor_message.imag,
        sensor_message.comp)

def listener():    
rospy.init_node('subscriber_node', anonymous=True)

rospy.Subscriber("sensor_topic", auc, sensor_callback)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()

#we need to initialize the node
rospy.init_node('publisher_node', anonymous=True)

#set the loop rate


while not rospy.is_shutdown():
    sensor = auc()
    sensor.imag = 1
    sensor.real= 1.5
    sensor.comp = 1 + 1.5
    rospy.loginfo("I publish:")
    rospy.loginfo(sensor)
    pub.publish(sensor)
    rate.sleep()

if __name__ == '__main__':
    listener()
    
