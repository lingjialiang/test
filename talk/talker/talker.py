#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String
import kddiapi as kd
import os,sys

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.001) # 10hz
    while not rospy.is_shutdown():            
        kddi=kd.k()
        title='[日時,湿度,温度,明るさ,紫外線,気圧,音量,不快指数,熱中症危険度,CO2濃度]'
        for i in range(len(kddi)):
            del kddi[i][0:2]
            rospy.loginfo(title)
            pub.publish(title)
            rospy.loginfo(kddi[i])
            pub.publish(kddi[i])
        rate.sleep()  

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
