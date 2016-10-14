#!/usr/bin/env python

import sys
import rospy
from romeo_srv.srv import *

def comment_HRP2_client(phase):
    rospy.wait_for_service('speech_by_phase')
    try:
        add_two_ints = rospy.ServiceProxy('speech_by_phase', Launch_speech)
        resp1 = add_two_ints(phase)
        if resp1.acquit==0:
           print usage()
        return resp1.acquit
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return """usage : number of the phase (int)
0 : presentation
1 : going upstairs 10cm
2 : walking on beam
3 : Mujoko
4 : going downstairs 15cm
5 : stepping stones
6 : multicontact
7 : remote
8 : heidelberg
9 : pick up the floor
10 : falling/error""" 

if __name__ == "__main__":
    if len(sys.argv) == 2:
        rospy.init_node('romeo_speech_client', anonymous=True)
        try: 
	    phase = int(sys.argv[1])
	except:
	    print usage()
	    sys.exit(2)
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s"%(phase)
    print "acquit : %s"%(comment_HRP2_client(phase))
