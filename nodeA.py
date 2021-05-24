#!/usr/bin/env python3
import rospy
import random
import time
from std_msgs.msg import String
from geometry_msgs.msg import Twist


reset = 0

def callback(feedback):
    objectstatus=feedback.linear.x
    graspfeedback=feedback.linear.y
    rospy.loginfo(rospy.get_caller_id() + " received data from robot Object status==> %f",objectstatus)
    #if objectstatus: #i.e if it is true that there is an object
    fh=open('graspfeedback.txt','w')
    fh.write('%d' % graspfeedback)
    fh.close
    fh=open('objectstatus.txt','w')
    fh.write('%d' % objectstatus)
    fh.close
    print("Text file has been written for CNN file to read and then execute itself")
    
    #Danial needs to have a text file named objectstatus.txt with dummy variable and keep checking it

    #fh=open('graspfeedback.txt','w')
    #fh.write('%d' % graspfeedback)
    #fh.close
    #fh=open('objectstatus.txt','w')
    #fh.write('%d' % reset)
    #fh.close
      #here danial needs to label the last pic of object that CNN saved and label it
def nodeA():
    pub = rospy.Publisher('rot', Twist, queue_size=1)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(1) # 1hz <---Change this value for EV3 use
    rotate_gripper=Twist()
    rospy.Subscriber('feed', Twist, callback)

    while not rospy.is_shutdown():
#added here the condition that keeps checking the output file of CNN        
#assuming the file that danial has created is named cnnoutput.txt        
        fh=open('cnnoutput.txt','r')
        height=float(fh.readline())
        angle=float(fh.readline())	
        fh.close
        obj_stat_1 = open("objectstatus.txt", "r")
        os_var_1 = int(obj_stat_1.read())
        obj_stat_1.close
        if ((angle>=-0.25) and (angle<=0.25) and (os_var_1 == 1)):
           print("Valid CNN output")
           rotate_gripper.linear.x=height #descend gripper
           rotate_gripper.linear.y=angle #rotate gripper
           string="Publishing CNN output to the robot"
           rospy.loginfo(string)
           pub.publish(rotate_gripper)
           obj_stat = open("objectstatus.txt", "r")
           os_var = int(obj_stat.read())
           obj_stat.close
           while os_var == 1:
              obj_stat = open("objectstatus.txt", "r")
              os_var = int(obj_stat.read())
              obj_stat.close
              time.sleep(8)

        else: 
             hello_str = "Nothing Received from test.py"
             rospy.loginfo(hello_str)
             #pub.publish(rotate_gripper)#publish something dumb
             #print("Published - Though nothing received")
             rate.sleep()
             time.sleep(1)

if __name__ == '__main__':
    try:
        nodeA()
    except rospy.ROSInterruptException:
        pass
