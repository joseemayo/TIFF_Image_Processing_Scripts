# 09/08/21 - Jose Mayorga
# 
# This script is designed to analyze combine/merge TIFF images.
# usage: python <script.py> <input_image.tiff>
#
# input_image - should be of '.tiff' format'

import numpy
from PIL import Image
#import sys
#import skimage.io
#import numpy as np
#from scipy import ndimage

# from matplotlib import pyplot as plt # Uncomment plot statements to visualize process.

#targetFile = sys.argv[1]

targetFile1 = 'Seed001.tif'
targetFile2 = 'Seed002.tif'
targetFile3 = 'Seed003.tif'

# Open Images
im1 = Image.open(targetFile1)
im2 = Image.open(targetFile2)
im3 = Image.open(targetFile3)

im1BW = im1.convert('L') # convert image to black and white
#im1BW.show()
im2BW = im2.convert('L') # convert image to black and white
im3BW = im3.convert('L') # convert image to black and white

im1BW.save('Seed001_BW.png')
im2BW.save('Seed002_BW.png')
im3BW.save('Seed003_BW.png')

# Convert Images into Arrays
imarray1BW = numpy.array(im1BW)
imarray2BW = numpy.array(im2BW)
imarray3BW = numpy.array(im3BW)

# Perform Combinatorial arithmatic
revImArray = imarray3BW * imarray3BW

# Convert array pack into image
finalImage = Image.fromarray(revImArray)

finalImage.save('Mult_Combined_S3_S3_BW.png')

# View Images
#im1.show()
#im2.show()

# Convert Images into Arrays
imarray1 = numpy.array(im1)
imarray2 = numpy.array(im2)

# Perform Combinatorial arithmatic
revImArray = imarray1 + imarray2

# Convert array pack into image
Image.fromarray(revImArray)


#image = skimage.io.imread(fname = targetFile)

# Copy image for final luminescence caluclation
#cleanImage = image.copy()