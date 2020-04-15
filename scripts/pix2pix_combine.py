"""
Created on Wed Mar 18 12:44:00 2020
@author: nsourlos
"""

#Usage
#python pix2pix_combine.py --image /home/nsourlos/Desktop/Train/Pictures --sketch /home/nsourlos/Desktop/Train/Sketches --destination /home/nsourlos/Desktop/new


import cv2
import os
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--image", required=True,
	help="path to real images folder")
ap.add_argument("-i", "--sketch", required=True,
	help="path to sketch images folder")
ap.add_argument("-d", "--destination", required=True,
	help="path to output folder")
args = vars(ap.parse_args())

#We have already both real images and their sketches have the same dimension (see massive_resizer file) and same name in their folders
#Below are three path examples

#path = '/home/nsourlos/Desktop/train/photos' #Assuming that real images are in this folder
#path2 = '/home/nsourlos/Desktop/train/sketches' #Assuming sketches are in this folder
#path3 = '/home/nsourlos/Desktop/train/new' #Combined photos+sketches images will be created here

os.chdir(args["image"]) 

for filename in os.listdir(args["image"]):
    a=filename 
    print(a)
    image1 = cv2.imread(a)
    print(image1.shape)
    os.chdir(args["sketch"]) 
    image2 = cv2.imread(a)
    print(image2.shape)
    os.chdir(args["destination"]) 
    comb = 255 * np.ones((image1.shape[0], image1.shape[1]+image2.shape[1], 3), dtype=np.uint8)
    print(comb.shape)
    comb[:image1.shape[0],image1.shape[1]:,:]=image1
    comb[:image1.shape[0],:image1.shape[1],:]=image2
    #cv2.imshow("Output", comb)
    cv2.imwrite(a[:-4]+"_AB"+a[-4:], comb) 
    os.chdir(args["image"])
    

    
