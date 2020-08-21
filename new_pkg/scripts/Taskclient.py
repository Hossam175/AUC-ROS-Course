#!/usr/bin/env python  
import sys
import rospy
from new_pkg.srv import hoss
from new_pkg.srv import hossRequest
from new_pkg.srv import hossResponse

def Task_client(STR):
    rospy.wait_for_service('Task')
    try:
        Task = rospy.ServiceProxy('Task', hoss)
        resp1 = Task(STR)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return " {} "%(sys.argv[0])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        str = sys.argv[1]
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s"%(STR)
    count = Task_client(STR)
    print "%s + %s = %s"%(STR, count)
