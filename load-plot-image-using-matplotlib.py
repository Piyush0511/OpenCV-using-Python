
from __future__ import print_function
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "path to the image")
args = vars(ap.parse_args())
image = mpimg.imread(args["image"])
plt.axis("off")

plt.imshow(image)
plt.show()


