#!/usr/bin/env python
import rospy
from new_pkg.msg import hoss

def callback(data):
    rospy.loginfo("%d" % (data.real, data.imag))

def listener():
    rospy.init_node('node1', anonymous=True)
    rospy.Subscriber("sensor_msg", hoss, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
