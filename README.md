# self-supervised-robotic-grasping
Repository containing files and folders for our implementation of a Self Supervised Robot, capable of learning robotic grasping on its own. We used the ev3 robot for grasping, and we used ROS to control the robot's various motors for several distinct motions. ROS allowed the use of 'nodes' for ease of communication between several modules of the project. The Software part of the project was coded using Pytorch and OpenCV. Ultimately our goal was to generate datasets for robotic grasping autonomously. Each data point consists of one image of the object being grasped, the angle at which the grasp was performed, and the success of the grasp. These datapoints will train the CNN, which in this case, is a modified resnet18 architecture. This project is being done as part of our Bachelors Thesis.