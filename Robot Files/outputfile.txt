#!usr/bin/env python
from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_A, OUTPUT_C, OUTPUT_B, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
import time

#us = UltrasonicSensor(INPUT_4)
#height_motor = LargeMotor(OUTPUT_A)
#angle_motor=LargeMotor(OUTPUT_B)
#grip_motor=MediumMotor(OUTPUT_C)
UN=LargeMotor(OUTPUT_A) #UPARNEECHE 
OC=MediumMotor(OUTPUT_B) #Rotating the Gripper
GW=MediumMotor(OUTPUT_C) #Open and Close Jaw
us = UltrasonicSensor()
a=5
number1=1
number2=0
dummy_variable=1000
while a==5:
    #read the outputfile.txt and store in corresponding variables
    fh=open('outputfile.txt','r')
    height=float(fh.readline())
    angle=float(fh.readline())
    fh.close
    time.sleep(2)
    ###
      #do the mapping of cnnoutput to corresponding on_for_rotations here 
    ###
    if us.distance_centimeters<10:
       fh=open('objectdetected.txt','w')
       fh.write(str(number1))
       fh.close
       print("Object detected and status 1 written to objectdetected.txt file")  
       #time.sleep(1)
    if angle!=dummy_variable:
       GW.on_for_rotations(SpeedPercent(10), -0.2) #open jaw
       GW.wait_until_not_moving()
       time.sleep(1)
       OC.on_for_rotations(SpeedPercent(10), angle) #rotate motor
       OC.wait_until_not_moving()
       time.sleep(1)
       UN.on_for_rotations(SpeedPercent(10), height) #decend
       UN.wait_until_not_moving()
       time.sleep(1)
       GW.on_for_rotations(SpeedPercent(10), 0.2) #close jaw(i.e. pickup the object)
       GW.wait_until_not_moving()
       time.sleep(1)
       UN.on_for_rotations(SpeedPercent(10), -height) #ascend with the object grasped
       UN.wait_until_not_moving()
       time.sleep(1)
       #now check if grasp successful using ultrasonic sensor
       if us.distance_centimeters>10:
          #if this is true this means grasp successful i.e. write this to a txt file graspfeed.txt     
          fh=open('graspfeed.txt','w')
          fh.write(str(number1))
          fh.close
          print("written successful grasp i.e. 1 to corresponding txt file")
       else: 
             #grasp not successful i.e. write this to a txt file graspfeed.txt     
             fh=open('graspfeed.txt','w')
             fh.write(str(number2))
             fh.close
             print("written unsuccessful grasp i.e. 0 to corresponding txt file")

       UN.on_for_rotations(SpeedPercent(10), height) #descend with the object
       UN.wait_until_not_moving()
       time.sleep(1)
       GW.on_for_rotations(SpeedPercent(10), -0.2) #open jaw and release object
       GW.wait_until_not_moving()
       time.sleep(1)
       UN.on_for_rotations(SpeedPercent(10), -height) #ascend without the object
       UN.wait_until_not_moving()
       time.sleep(1)
       GW.on_for_rotations(SpeedPercent(10), 0.2) #return to original jaw closed status
       GW.wait_until_not_moving()
       time.sleep(1)
       OC.on_for_rotations(SpeedPercent(10), -angle) #return to original angle
       OC.wait_until_not_moving()
       time.sleep(1)
       fh=open('outputfile.txt','w')
       #fh.write('%d' % dummy_variable + '\n' +'%d' % dummy_variable)
       fh.write(str(0.4) + "\n")
       fh.write(str(dummy_variable))
       fh.close
       print("About to make objectdetected.txt 0 again")
       fh=open('objectdetected.txt','r')
       print("objectdetected.txt - Before writing", fh.read())
       fh.close
       fh=open('objectdetected.txt','w')
       fh.write(str(number2))
       fh.close
       fh=open('objectdetected.txt','r')
       print("objectdetected.txt - After writing", fh.read())
       fh.close
       time.sleep(10)

       print("Successfully reset objectdetected.txt and outputfile.txt")
    elif angle == dummy_variable:   
          print("no object detected")
    #time.sleep (1) # Give the CPU a rest
