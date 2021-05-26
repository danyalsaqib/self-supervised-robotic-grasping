import cv2
import numpy as np
import functs as ft
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import PIL
import os
import time

import torch
import torch.nn as nn
import torchvision
import torchvision.models as models
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pylab as plt
from collections import OrderedDict
from torch.optim import lr_scheduler

data_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

model_ft = models.resnet18()
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 18)
model_ft.load_state_dict(torch.load('fyp_cnn.pt'))
model_ft.eval()

f = open("gc_file.txt", "r")
gc = int(f.read())
print("Initial gc: ", gc)

cap = cv2.VideoCapture(0)

whT = 416

classesFile = 'coco_names.txt'
classNames = []

with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
    
# print(classNames)
# print(len(classNames))

modelConfiguration = 'yolov4.cfg'
modelWeights = 'yolov4.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

wind = ft.objWin(0, 0, '0', '0')

def Lolv1():
    img = cv2.imread('object-detection-load.png')

    x = 0
    y = 0
    a = "NONE"
    b = "0"

    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    im = PIL.Image.fromarray(cv2image)
    imTk = ImageTk.PhotoImage(im)
    wind.lmain.imTk = imTk
    wind.lmain.configure(image = imTk)
    wind.newVar(x, y, a, b)
    if wind.controlVar:
        wind.lmain.after(1, Lol)
    else:
        wind.lmain.after(1, Lolv1)

def Lol():
    success, img = cap.read()
    img = cv2.flip(img, 1)
    obj_stat = open("objectstatus.txt", "r")
    os_var = int(obj_stat.read())
    if os_var == 1:
    	wind.controlVar2 = True

    if wind.controlVar2:
        global gc
        # Change Directory to where you want your images saved
        #path = 'Downloads\Object Detection\object-detection\CNN Training\Training Images'
        #print(cv2.imwrite(os.path.join(path , 'train_img_'+str(gc)+'.png'), img))
        os.chdir('/home/dani/catkin_ws/src/tutorials/CNN Training/Training Images')
        print("Image Write Success: ", cv2.imwrite(os.path.join('train_img_'+str(gc)+'.png'), img))
        os.chdir('/home/dani/catkin_ws/src/tutorials')
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        im = PIL.Image.fromarray(cv2image) 
        im1 = im.convert('RGB')		# Image converted to RGB
        img_nn_mod = data_transforms(im1)	# Appropriate transforms applied to image
        img_nn_mod = img_nn_mod.unsqueeze(0)  # if torch tensor
        outputs = model_ft(img_nn_mod)	# Image being passed through CNN
        _, preds = torch.max(outputs, 1)	# Obtained Predicted Class
        angle = int(preds) * 10
        angle = angle - 90
        angle = angle / 90
        angle = angle * 0.25
        print("Prediction Class:", int(preds) * 10)
        print("Mapped Output: ", angle)
        f = open("cnnoutput.txt", "w")
        f.write(str(0.5) + "\n")
        f.write(str(angle))
        f = open("gc_file.txt", "w")
        f.write(str(gc))
        obj_stat = open("objectstatus.txt", "r")
        os_var = int(obj_stat.read())
        while os_var == 1:
        	obj_stat = open("objectstatus.txt", "r")
        	os_var = int(obj_stat.read())
        	obj_stat.close
        	time.sleep(3)
        	
        f = open("graspfeedback.txt", "r")
        rnm_var = int(f.read())
        os.chdir('/home/dani/catkin_ws/src/tutorials/CNN Training/Training Images')
        os.rename(os.path.join('train_img_' + str(gc) + '.png'), os.path.join(str(rnm_var) + '_' + str(int(preds))+ '_train_img_' + str(gc) + '.png'))
        os.chdir('/home/dani/catkin_ws/src/tutorials')

        gc = gc + 1
        print("controlVar2 exiting")
        wind.controlVar2 = False
    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0,0,0], 1, crop = False)
    net.setInput(blob)
    
    layerNames = net.getLayerNames()
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    # print(outputNames)
    
    outputs = net.forward(outputNames)
    
    x = 0
    y = 0
    a = "NONE"
    b = "0"
    x, y, a, b = ft.findObjects(outputs, img, classNames)

    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    im = PIL.Image.fromarray(cv2image)
    imTk = ImageTk.PhotoImage(im)
    wind.lmain.imTk = imTk
    wind.lmain.configure(image = imTk)
    wind.newVar(x, y, a, b)
    if wind.controlVar:
        wind.lmain.after(1, Lol)
    else:
        wind.lmain.after(1, Lolv1)
        

Lolv1()
wind.root.mainloop()
