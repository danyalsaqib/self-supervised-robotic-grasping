#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(rotate_gripper):
    print('received CNN output')
    fh=open('outputfile.txt','w')
    fh.write(str(rotate_gripper.linear.x) + "\n")
    fh.write(str(rotate_gripper.linear.y))
    fh.close
    print("Height Received: ", rotate_gripper.linear.x)
    print("Angle Received: ", rotate_gripper.linear.y)
    #fh.write('%d' % rotate_gripper.linear.x + '\n' +'%d' % rotate_gripper.linear.y)
    print("Exiting Callback")

def test():

    pub = rospy.Publisher('feed', Twist, queue_size=1)
    rospy.init_node('test', anonymous=True)
    rospy.Subscriber('rot', Twist, callback)
    #pub2 = rospy.Publisher('feed', Twist, queue_size=1)
    rate = rospy.Rate(1) # 1hz <---Change this value for EV3 use
    #rospy.Subscriber('rot', Twist, callback)
    feedback=Twist()
    feedback.linear.x=0
    feedback.linear.y=0
    status_OBJECT=0
    rospy.Subscriber('rot', Twist, callback)

    while not rospy.is_shutdown():

        time.sleep(5)
        print("Test Node Running")
        fh=open('objectdetected.txt','r')
        status_OBJECT=int(float(fh.read()))
        fh.close
        print("Object status ==> %d" % status_OBJECT + "read by robot") 

        #read the feedback file and communicate to the PC
        fh=open('graspfeed.txt','r')
        graspfeed=int(fh.read())
        fh.close
        if status_OBJECT==1:
           feedback.linear.x=1
           feedback.linear.y=graspfeed
           string="Object Detected - Initiating Publication Sequence"
           rospy.loginfo(string)
           pub.publish(feedback)
           print("Published on Topic Successfully")
           time.sleep(8)
           obj_stat = open("objectdetected.txt", "r")
           print("objectdetected.txt string: ", obj_stat.read())
           os_var = obj_stat.read()
           obj_stat.close

           while os_var != '0':
              time.sleep(8)
              obj_stat = open("objectdetected.txt", "r")
              #print("objectdetected.txt string: ", obj_stat.read())
              os_var = str(obj_stat.read())
              obj_stat.close
              print("os_var value: ", os_var)
              print("time.sleep executed")

           fh=open('graspfeed.txt','r')
           graspfeed=int(fh.readline())
           fh.close
           feedback.linear.x=0
           feedback.linear.y=graspfeed
           string="Publishing valid graspfeedback to nodeA"
           rospy.loginfo(string)
           pub.publish(feedback)

        else:
              hello_str = "No object detected...nothing has been published to pc"
              rospy.loginfo(hello_str)
              #rate=rospy.Rate(1)
              rate.sleep()
# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        test()

