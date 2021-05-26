<h1>Self Supervised Robotic Grasping</h1>
<h4>Repository containing files and folders for our implementation of a Self Supervised Robot, capable of learning robotic grasping on its own.</h4>

<h2>Abstract</h2>
<h4>Learning Based Robot Grasping currently involves the use of labeled data. This approach has two major disadvantages. Firstly, labeling data for grasp points and angles is a strenuous process, so the dataset remains limited. Secondly, human labeling is prone to bias due to semantics.</h4>
<h4>In order to solve these problems we propose a simpler self-supervised robotic setup, that will train a Convolutional Neural Network (CNN). The robot will label and collect the data
during the training process. The idea is to make a robot that is less costly, small and easily maintainable in a lab setup. The robot will be trained on a large data set for several hundred hours and then the trained Neural Network can be mapped onto a larger grasping robot.</h4>
