#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:41:17 2020

@author: nsourlos
"""
#Usage
#python massive_resizer.py --image /home/nsourlos/Desktop/original/trainA --size /home/nsourlos/Desktop/original/trainB/f1-001-01.jpg --destination /home/nsourlos/Desktop/new

from PIL import Image
from resizeimage import resizeimage
import os
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--image", required=True,
	help="path to images folder that we want to change size")
ap.add_argument("-i", "--size", required=True,
	help="path to image that we want to get its size")
ap.add_argument("-d", "--destination", required=True,
	help="path to output folder")
args = vars(ap.parse_args())

#original 1024*768 to 414*582
#path = '/home/nsourlos/Desktop/human2sketch/trainA'

image1 = cv2.imread(args["size"])
sh=image1.shape

os.chdir(args["image"]) 
for filename in os.listdir(args["image"]):
    a=filename
    with open(a, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [sh[1],sh[0]])
            os.chdir(args["destination"]) 
            cover.save(a, image.format)
            os.chdir(args["image"]) 
