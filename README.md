# Self Supervised Robotic Grasping
This is a repository containing files and folders for our implementation of a Self Supervised Robot, capable of learning robotic grasping on its own.

## Abstract
Learning Based Robot Grasping currently involves the use of labeled data. This approach has two major disadvantages. Firstly, labeling data for grasp points and angles is a strenuous process, so the dataset remains limited. Secondly, human labeling is prone to bias due to semantics.
In order to solve these problems we propose a simpler self-supervised robotic setup, that will train a Convolutional Neural Network (CNN). The robot will label and collect the data
during the training process. The idea is to make a robot that is less costly, small and easily maintainable in a lab setup. The robot will be trained on a large data set for several hundred hours and then the trained Neural Network can be mapped onto a larger grasping robot.

## Introduction
The basic problem our project is trying to solve is dynamic robot grasping. Currently, solving this particular problem is a critical challenge in robotics. Robots are already very good at working in tightly monitored, closed, and predictable environments such as assembly lines in factories. This is because in such environments, the robotic hand has to pick up the same object, with the same geometric shape, from the same position over and over again. As such, the problem is very much static in that the robotic hand can be built and programmed for that specific task.

The idea to use robot hand-eye coordination and visual servoing dates back to 1979. However, building or programming a robotic hand that can successfully grasp different objects with a variety of shapes and sizes still remains a challenge in both the industry, and academia. This is an unmet need, especially in industries where robots are required to grasp numerous geometrically different objects in a dynamic environment. Several different approaches have been tried and tested for this problem, with varying degrees of success. However, the recent boom in Deep Learning and Artificial Intelligence in general has allowed for a new avenue to be pursued in academia. The idea is to train the robot to grasp objects by training a Neural Network, that will learn the optimum strategy – gripper angle, gripper height, angle of the arm, etc – to grasp an object of that particular shape and size

A research paper recently proposed the idea of a self-supervised robot which labels and marks successful attempts of grasping in the process of training the CNN. However, the problem of limited datasets persists, as larger sets of training for a robot means better performance in the testing phase where an unidentified new object is presented to the robot for grasping. The probability of successful grasping increases with more training. The setup for this robot however is expensive, large and power hungry. We propose a much smaller hand-eye coordination based self-supervised robot which can train a CNN for several hundred hours on multiple objects in a lab setup. Then this CNN can be scaled onto the larger robots or integrated with their present CNN. This way we will not only save resources but also recreate a setup otherwise too expensive and power-intensive for direct training.

## Problem Statement
Many approaches traditionally used human-labeled data to train the Neural Network in question. However, all of them faced problems during the training mechanism, as the data
acted as a bottleneck in this approach. Labeling will always be biased due to semantics involved, and there can be multiple approaches to grasp a certain object. Human labeling is
also a tedious and time consuming work. All of these reasons mean that ‘human generated data’ is not a scalable solution.

Hence, the problem this project aims to solve, is the **elimination of human involvement – data labeling and human bias – from the training process of robotic grasping**. This means that the main objective of this project is to **create ‘Self Supervised Robots’, that can effectively solve the robotic grasping problem using minimal amount of human involvement**, while also keeping in mind the usual engineering problem of minimizing energy consumption and reducing equipment costs.

A successful and scalable solution to the robotics grasping problem will have a huge amount of potential both in academia and in industry. In academia, the solution would mean a push towards research in areas such as automated industrial processes control, system design for material processing, and human motor control etc. However, it is the industry that will perhaps be the biggest benefactor of the solution of this problem. Fast growing industries such as E-Commerce have a huge demand of robots that are able to grasp a variety of objects in order to fully automate the process. Robots are providing far greater flexibility and dramatically expediting the Return on Investment (ROI) of warehouse automation. Other
industries that will greatly benefit from a solution to this problem include the food industry (automating food packaging and processing), toy industry (grasping and classifying plastic parts), storage and logistics applications (automated stocking and transportation of products), and automotive manufacturing (robotic assemblies). Other indigenous projects that will benefit from such a robot include automating systems such as litter-picking robots, and automated robots in the service industry to name a few.

## Project Overview
The goal of this project, as mentioned earlier, is to minimize and eliminate the need for human interaction with the robots and super-size the idea of ‘self-supervised robots’. Previous works have shown a promising future towards Robot-Object interaction with advent of DL and AI but none of the approaches is scalable and up-for-grabs for industries. Our proposed method involves using ROS (Robot Operating System) on numerous LEGO kits in a closed lab environment where the real time interaction of the robotic kits with the objects would train the CNN if a grasp was successful or not. The data points generated out of these hours of robot-object interaction would then be made available for large industrial-scale robots with extended accuracy and lower failure risks.

The breaking down of learning process to numerous trainer robots curtails the input (energy consumption, equipment cost, time investment) and maximizes the output labeled data set. The hardware components include LEGO EV3 trainer robot kits that can work in a lab environment and can be trained on concerned objects to create novel data points. This expanding cloud of AI labelled data set would then be used by the end-effector robots that actually perform the automation tasks. The packaged software includes ROS as it is becoming increasingly popular to program robots. In a nutshell, the proposed project promises a complete package for industrial automation, probably the first time where the concept of what started with robot grasping now shakes hands with the industry in a much more scalable way.

## Hardware Setup
The LEGO EV3 kits are set up in such a way that we work with 3 motors, each connected to a port of the EV3 brick. One port of the EV3 is also connected with an ultrasonic sensor. The following mapping outlines how each of these components are connected.
- EV3 Brick Port A ---> Motor for moving claw up and down
- EV3 Brick Port B ---> Motor for rotating claw
- EV3 Brick Port A ---> Motor for opening and closing jaws
- EV3 Brick Port 1 ---> Ultrasonic sensor for object detection

Apart from the robot itself, a webcam is needed to act as the **robot's eyes**. While a laptop's built in webcam may theoretically work, we recommend working with a USB webcam, that can be set up appropriately so as to be able to clearly view the object.

![setup](https://user-images.githubusercontent.com/60542092/119741202-ab1f5680-be9e-11eb-91bb-c7b68414094a.jpeg "The Hardware Setup")

## Software Setup and Installation
The project involves 2 nodes - the PC and the LEGO EV3 Robot. Both of them require ROS to be installed on them. Our particular setup had Debian Linux installed on the EV3 LEGO Brick, and ROS Noetic on our Ubuntu Linux Machine. We will assume in this walkthrough that ROS is installed on both the EV3 Lego kit and on your PC. You can follow the links below for thorough guidance:
- Installing ROS on a LEGO EV3 Brick: http://wiki.ros.org/Robots/EV3
- Ubuntu install of ROS Noetic: http://wiki.ros.org/noetic/Installation/Ubuntu
- Installing Catkin: http://wiki.ros.org/catkin
After ROS has been installed on both the machines, the next step is to make a new catkin workspace. On your PC, open up the terminal and run the following commands line by line:
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
After running these commands, you should have a new catkin workspace that has various subdirectories. To set the files up on PC, copy all of the files from the 'PC Files' folder of this repository, and copy them into the directory 'catkin_ws/src/tutorials'. Create this directory if it hasn't already been created using the following commands:
```
$ cd catkin_ws/src
$ mkdir tutorials
```
After all of the files have been copied to this directory, run the following lines on the terminal again:
```
cd ~catkin_ws
catkin_make
```
Hopefully, we should be all set up now on the PC. We will now move on to setting stuff up on the robot.

Firstly, to access the robot via any one of your PC terminals, connect the LEGO EV3 brick to your PC via the USB cable, and run the following command from your Ubuntu machine:
```
ssh robot@ev3dev.local
```
You will now be asked to enter a password. This password is **maker** by default, but you may have changed it for your particular setup. Enter the password, and you will be able to access the robot's files. Here, again run the following commands:
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
Now, you will have to either copy the 'Robot Files' folder of this repository, and copy them into the directory 'catkin_ws/src/tutorials/scripts'. If you cannot directly copy these files into the robot, simple create these files manually in the directory using the `nano` command, for example `nano reset.py`, and copy the text from this github repository's files into these manually created files. Create this directory if it hasn't already been created using the following commands:
```
$ cd catkin_ws/src
$ mkdir tutorials
$ cd tutorials
$ mkdir scripts
```
After all of the files are successfully copied onto the robot, run the following command:
```
cd ~catkin_ws
catkin_make
```
Wait for the `catkin_make` to complete. After that has been complete, we are ready to run our complete setup for self supervised robotic grasping.

## Running the Setup
To run the complete setup, 5 separate terminals are needed. We will be running 4 different python files on 4 different terminals, and the 5th terminal will be running the roscore.

### Terminal 1
On the first terminal run the following command:
```
$ roscore
```
On this terminal, the roscore will start running. The roscore is what enables communication between the robot and the PC. Leave the roscore running on this terminal.

### Terminal 2
On this terminal, run the following commands
```
$ cd ~catkin_ws/src/tutorials
$ python3 OD_Script.py
```
A GUI window will popup. Click the 'Click to start Object Detection' button on the GUI, which will open your webcam and start running the **YOLOv4 object detector** on your webcam. This will also initiate the CNN prediction for objects that will be grasped. Again, leave this terminal running up.

### Terminal 3
On this terminal, run the following commands:
```
$ cd ~catkin_ws/src/tutorials
$ rosrun tutorials nodeA.py
```
This will start up the ROS node on your PC for communication with your EV3 robot setup. Leave this terminal running as well.

### Terminal 4
On this terminal, you will have to enter the robot using the following command:
```
$ ssh robot@ev3dev.local
```
Enter the password to access the robot. After the robot has been successfully accessed, run the following commands:
```
$ cd ~catkin_ws/src/tutorials/scripts
$ python3 sample.py
```
This will run the 'Robot Control Center' on this terminal. What this means is that all of the robot's instructions and movements will be regulated via this terminal or node. Leave this terminal running again.


### Terminal 5
On this terminal, you will once again have to enter the robot using the following command:
```
$ ssh robot@ev3dev.local
```
Enter the password to access the robot. After the robot has been successfully accessed, run the following commands:
```
$ cd ~catkin_ws/src/tutorials/scripts
$ rosrun tutorials test.py
```
This will run the ROS Node on the LEGO EV3 Robot to communicate with the PC.

After all 5 nodes are running, the setup will look something like this:

![Interfacing](https://user-images.githubusercontent.com/60542092/119740963-3ea45780-be9e-11eb-9e03-9c90eb2fbf6f.PNG "All 5 terminals running - Complete Setup")

## Data Collection
If you have successfully completed all of the previous steps, your setup is complete and ready to run the complete setup and initiate data collection. To initiate, simply place an object below the grasping claw of the robot. The Ultrasonic sensor will detect the object and signal the PC that an object has been detected. The webcam will take a picture of the object, run the CNN on it, obtain a prediction of the optimal grasping angle, and send it back to the robot. The robot will then attempt a grasp with that particular angle, and determine whether it was a success or not. This grasp feedback will then be sent back to the PC, and the image will be saved in the directory 'CNN Training/Training Images'. The image names will encode all of the relevant information about that particular image. The first number in the name of the image  will be either a 0 or a 1. This signals whether this particular grasp was successful or not. The next number is the angle of grasp divided by 10. For example, if the image is named '0_11_train_img_10.png', this means that this particular grasp was unsuccessful, and the grasp angle was 11 * 10 = 110 degrees. Hence, the image name in itself encodes information about the grasp. Some example images have been saved in this github repository under the 'CNN Training/ Training Images' folder.

![Dataset Multiplication](https://user-images.githubusercontent.com/60542092/119741267-cdb16f80-be9e-11eb-80a8-5531a4560cf9.PNG "Dataset Generation and Multiplication")
 
> ## FAQs and Troubleshooting
> - **When I click the 'Click to start Object Detection' button, I get an error.**
> On the PC, open the file 'catkin_ws/src/tutorials/OD_Script.py'. Here on line 41, notice the code `cap = cv2.VideoCapture(0)`. Try changing this value from 0 to 1,2,3.. etc.
