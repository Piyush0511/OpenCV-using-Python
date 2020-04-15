

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

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 254
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)


M = np.ones(image.shape, dtype = "uint8") * 100
added = np.add(image, M)
cv2.imshow("npAdded", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = np.subtract(image, M)
cv2.imshow("npSubtracted", subtracted)
cv2.imshow("m",M)
print(image.shape)
cv2.waitKey(0)

