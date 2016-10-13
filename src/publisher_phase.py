#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8

def talker():
    pub = rospy.Publisher('phase', Int8, queue_size=5)
    rospy.init_node('phase_HRP2_demonstration', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(0)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
