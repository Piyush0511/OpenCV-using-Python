# USAGE
# python order_coordinates.py

# import the necessary packages
from __future__ import print_function
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
cv2.imshow("original",image)

#shifted=imutils.translate(image,0,100)

#rotated = imutils.rotate(image, 45 )

resized = imutils.resize(image, height = 110)
print(resized.shape[1])
#flipped = cv2.flip(image, -1)

#cropped = image[30:120 , 240:335]

#cv2.imshow("rotated", rotated)
#cv2.imshow("resized", resized)
#cv2.imshow("Shifted Up and Left", shifted)
#cv2.imshow("Flipped Vertically", flipped)
#cv2.imshow("cropped", cropped)
cv2.waitKey(0)
