<h1>Self Supervised Robotic Grasping</h1>
<h4>Repository containing files and folders for our implementation of a Self Supervised Robot, capable of learning robotic grasping on its own.</h4>

<h2>Abstract</h2>
<p>Learning Based Robot Grasping currently involves the use of labeled data. This approach has two major disadvantages. Firstly, labeling data for grasp points and angles is a strenuous process, so the dataset remains limited. Secondly, human labeling is prone to bias due to semantics.</p>
<p>In order to solve these problems we propose a simpler self-supervised robotic setup, that will train a Convolutional Neural Network (CNN). The robot will label and collect the data
during the training process. The idea is to make a robot that is less costly, small and easily maintainable in a lab setup. The robot will be trained on a large data set for several hundred hours and then the trained Neural Network can be mapped onto a larger grasping robot.</p>

<h2>Introduction</h2>
<p>The basic problem our project is trying to solve is dynamic robot grasping. Currently, solving this particular problem is a critical challenge in robotics. Robots are already very good at working in tightly monitored, closed, and predictable environments such as assembly lines in factories. This is because in such environments, the robotic hand has to pick up the same object, with the same geometric shape, from the same position over and over again. As such, the problem is very much static in that the robotic hand can be built and programmed for that specific task.</p>
<p>The idea to use robot hand-eye coordination and visual servoing dates back to 1979. However, building or programming a robotic hand that can successfully grasp different objects with a variety of shapes and sizes still remains a challenge in both the industry, and academia. This is an unmet need, especially in industries where robots are required to grasp numerous geometrically different objects in a dynamic environment. Several different approaches have been tried and tested for this problem, with varying degrees of success. However, the recent boom in Deep Learning and Artificial Intelligence in general has allowed for a new avenue to be pursued in academia. The idea is to train the robot to grasp objects by training a Neural Network, that will learn the optimum strategy – gripper angle, gripper height, angle of the arm, etc – to grasp an object of that particular shape and size.</p>

<p>A research paper recently proposed the idea of a self-supervised robot which labels and marks successful attempts of grasping in the process of training the CNN. However, the problem of limited datasets persists, as larger sets of training for a robot means better performance in the testing phase where an unidentified new object is presented to the robot for grasping. The probability of successful grasping increases with more training. The setup for this robot however is expensive, large and power hungry. We propose a much smaller hand-eye coordination based self-supervised robot which can train a CNN for several hundred hours on multiple objects in a lab setup. Then this CNN can be scaled onto the larger robots or integrated with their present CNN. This way we will not only save resources but also recreate a setup otherwise too expensive and power-intensive for direct training.</p>

<h2>Problem Statement</h2>
<p>Many approaches traditionally used human-labeled data to train the Neural Network in question. However, all of them faced problems during the training mechanism, as the data
acted as a bottleneck in this approach. Labeling will always be biased due to semantics involved, and there can be multiple approaches to grasp a certain object. Human labeling is
also a tedious and time consuming work. All of these reasons mean that ‘human generated data’ is not a scalable solution.</p>

<p>Hence, the problem this project aims to solve, is the <strong>elimination of human involvement – data labeling and human bias – from the training process of robotic grasping</strong>. This means that the main objective of this project is to <strong>create ‘Self Supervised Robots’, that can effectively solve the robotic grasping problem using minimal amount of human involvement</strong>, while also keeping in mind the usual engineering problem of minimizing energy consumption and reducing equipment costs.</p>

<p>A successful and scalable solution to the robotics grasping problem will have a huge amount of potential both in academia and in industry. In academia, the solution would mean a push towards research in areas such as automated industrial processes control, system design for material processing, and human motor control etc. However, it is the industry that will perhaps be the biggest benefactor of the solution of this problem. Fast growing industries such as E-Commerce have a huge demand of robots that are able to grasp a variety of objects in order to fully automate the process. Robots are providing far greater flexibility and dramatically expediting the Return on Investment (ROI) of warehouse automation. Other
industries that will greatly benefit from a solution to this problem include the food industry (automating food packaging and processing), toy industry (grasping and classifying plastic parts), storage and logistics applications (automated stocking and transportation of products), and automotive manufacturing (robotic assemblies). Other indigenous projects that will benefit from such a robot include automating systems such as litter-picking robots, and automated robots in the service industry to name a few.</p>

<h2>Project Overview</h2>
<p>The goal of this project, as mentioned earlier, is to minimize and eliminate the need for human interaction with the robots and super-size the idea of ‘self-supervised robots’. Previous works have shown a promising future towards Robot-Object interaction with advent of DL and AI but none of the approaches is scalable and up-for-grabs for industries. Our proposed method involves using ROS (Robot Operating System) on numerous LEGO kits in a closed lab environment where the real time interaction of the robotic kits with the objects would train the CNN if a grasp was successful or not. The data points generated out of these hours of robot-object interaction would then be made available for large industrial-scale robots with extended accuracy and lower failure risks.</p>

<p>The breaking down of learning process to numerous trainer robots curtails the input (energy consumption, equipment cost, time investment) and maximizes the output labeled data set. The hardware components include LEGO EV3 trainer robot kits that can work in a lab environment and can be trained on concerned objects to create novel data points. This expanding cloud of AI labelled data set would then be used by the end-effector robots that actually perform the automation tasks. The packaged software includes ROS as it is becoming increasingly popular to program robots. In a nutshell, the proposed project promises a complete package for industrial automation, probably the first time where the concept of what started with robot grasping now shakes hands with the industry in a much more scalable way.</p>

<h2>Setup and Installation</h2>
<p>The project involves 2 nodes - the PC and the LEGO EV3 Robot. Both of them require ROS to be installed on them. Our particular setup had Debian Linux installed on the EV3 LEGO Brick, and ROS Noetic on our Ubuntu Linux Machine. We will assume in this walkthrough that ROS is installed on both the EV3 Lego kit and on your PC. You can follow the links below for thorough guidance:
<ul>
<li>Installing ROS on a LEGO EV3 Brick: http://wiki.ros.org/Robots/EV3</li>
<li>Ubuntu install of ROS Noetic: http://wiki.ros.org/noetic/Installation/Ubuntu</li>
<li>Installing Catkin: http://wiki.ros.org/catkin</li>
</ul>
After ROS has been installed on both the machines, the next step is to make a new catkin workspace. On your PC, open up the terminal and run the following commands line by line:
</p>
```
function test() {
  console.log("notice the blank line before this function?");
}
```
