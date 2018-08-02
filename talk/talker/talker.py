#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import weatherapi as api

def talker():
	pub = rospy.Publisher('telemetry', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		hello_str = "goodbye %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
