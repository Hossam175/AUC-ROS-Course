#!/usr/bin/env python 

from new_pkg.srv import hoss
from new_pkg.srv import hossRequest
from new_pkg.srv import hossResponse

import rospy

def handle_Task(req):
    print "Returning [%s = %d]"%(req.STR, (req.STR))
    return TaskResponse(req.STR)

def Task_server():
    rospy.init_node('Task_server')
    s = rospy.Service('count', count, handle_Task)
    print " counting the strings"
    rospy.spin()
    
if __name__ == "__main__":
Task_server()
