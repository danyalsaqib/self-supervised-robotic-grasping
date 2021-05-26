<h1>Self Supervised Robotic Grasping</h1>
<h4>Repository containing files and folders for our implementation of a Self Supervised Robot, capable of learning robotic grasping on its own.</h4>

<h2>Abstract</h2>
Learning Based Robot Grasping currently involves the use of labeled data. This approach has two major disadvantages. Firstly, labeling data for grasp points and angles is a strenuous process, so the dataset remains limited. Secondly, human labeling is prone to bias due to semantics.
In order to solve these problems we propose a simpler self-supervised robotic setup, that will train a Convolutional Neural Network (CNN). The robot will label and collect the data
during the training process. The idea is to make a robot that is less costly, small and easily maintainable in a lab setup. The robot will be trained on a large data set for several hundred hours and then the trained Neural Network can be mapped onto a larger grasping robot.

<h2>Introduction</h2>
The basic problem our project is trying to solve is dynamic robot grasping. Currently, solving this particular problem is a critical challenge in robotics. Robots are already very good at working in tightly monitored, closed, and predictable environments such as assembly lines in factories. This is because in such environments, the robotic hand has to pick up the same object, with the same geometric shape, from the same position over and over again. As such, the problem is very much static in that the robotic hand can be built and programmed for that specific task.  

The idea to use robot hand-eye coordination and visual servoing dates back to 1979. However, building or programming a robotic hand that can successfully grasp different objects with
a variety of shapes and sizes still remains a challenge in both the industry, and academia. This is an unmet need, especially in industries where robots are required to grasp numerous
geometrically different objects in a dynamic environment. Several different approaches have been tried and tested for this problem, with varying degrees of success. However, the recent
boom in Deep Learning and Artificial Intelligence in general has allowed for a new avenue to be pursued in academia. The idea is to train the robot to grasp objects by training a Neural
Network, that will learn the optimum strategy – gripper angle, gripper height, angle of the arm, etc – to grasp an object of that particular shape and size.  

A research paper recently proposed the idea of a self-supervised robot which labels and marks successful attempts of grasping in the process of training the CNN. However, the problem
of limited datasets persists, as larger sets of training for a robot means better performance in the testing phase where an unidentified new object is presented to the robot for grasping. The probability of successful grasping increases with more training. The setup for this robot however is expensive, large and power hungry. We propose a much smaller hand-eye
coordination based self-supervised robot which can train a CNN for several hundred hours on multiple objects in a lab setup. Then this CNN can be scaled onto the larger robots or
integrated with their present CNN. This way we will not only save resources but also recreate a setup otherwise too expensive and power-intensive for direct training
