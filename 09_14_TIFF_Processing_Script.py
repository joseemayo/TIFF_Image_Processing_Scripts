# 09/14/21 - Jose Mayorga
# 
# This script is designed to analyze combine/merge TIFF images.
#
# input_image - should be of '.tiff' format'

import numpy
from PIL import Image

#### 1) Infiltrated_substrate ####

# Generating File List
filenames = ('Infiltrated_NL1.2_V_luminiscence001.tif', 'Infiltrated_NL1.2_V_luminiscence002.tif', 'Infiltrated_NL1.2_V_luminiscence003.tif',
 'Infiltrated_NL1.2_V_luminiscence004.tif', 'Infiltrated_NL1.2_V_luminiscence005.tif', 'Infiltrated_NL1.2_V_luminiscence006.tif',
 'Infiltrated_NL1.2_V_luminiscence007.tif', 'Infiltrated_NL1.2_V_luminiscence008.tif', 'Infiltrated_NL1.2_V_luminiscence009.tif',
 'Infiltrated_NL1.2_V_luminiscence010.tif', 'Infiltrated_NL1.2_V_luminiscence011.tif', 'Infiltrated_NL1.2_V_luminiscence012.tif',
 'Infiltrated_NL1.2_V_luminiscence013.tif', 'Infiltrated_NL1.2_V_luminiscence014.tif', 'Infiltrated_NL1.2_V_luminiscence015.tif',
 'Infiltrated_NL1.2_V_luminiscence016.tif', 'Infiltrated_NL1.2_V_luminiscence017.tif', 'Infiltrated_NL1.2_V_luminiscence018.tif',
 'Infiltrated_NL1.2_V_luminiscence019.tif', 'Infiltrated_NL1.2_V_luminiscence020.tif')

# Creating First Working Image
# Open the Image
firstImage = Image.open('1) Infiltrated_substrate/' + filenames[0])
    
# Convert the image to black and white
firstImageBW = firstImage.convert('L')
    
# Convert Image into Array
firstImageArray = numpy.array(firstImageBW)
#firstImageArray = numpy.array(firstImage)

# Saving First Image
Image.fromarray(firstImageArray).save('../Image_Combination/1/BW/Stacked_Image_1_1.png')
#Image.fromarray(firstImageArray).save('../Image_Combination/1/Color/Stacked_Image_1_1.png')

workingImage = firstImageArray
iteration = 1

for file in filenames[1:20]:
    
    # Open the Image
    newImage = Image.open('1) Infiltrated_substrate/' + file)
    
    # Convert the image to black and white
    newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    newImageArray = numpy.array(newImageBW)
    #newImageArray = numpy.array(newImage)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    Image.fromarray(workingImage).save('../Image_Combination/1/BW/Stacked_Image_1_' + str(iteration) + '.png')
    #Image.fromarray(workingImage).save('../Image_Combination/1/Color/Stacked_Image_1_' + str(iteration) + '.png')


## 2) No infiltration_No substrate

# Generating File List
filenames = ('1.tif', '2.tif', '3.tif', '4.tif', '5.tif', '6.tif', '7.tif', '8.tif', '9.tif', '10.tif',
             '11.tif', '12.tif', '13.tif', '14.tif', '15.tif', '16.tif', '17.tif', '18.tif', '19.tif', '20.tif')

# Creating First Working Image
# Open the Image
firstImage = Image.open('2) No infiltration_No substrate/' + filenames[0])
    
# Convert the image to black and white
firstImageBW = firstImage.convert('L')
    
# Convert Image into Array
firstImageArray = numpy.array(firstImageBW)
#firstImageArray = numpy.array(firstImage)

# Saving First Image
Image.fromarray(firstImageArray).save('../Image_Combination/2/BW/Stacked_Image_2_1.png')
#Image.fromarray(firstImageArray).save('../Image_Combination/2/Color/Stacked_Image_2_1.png')

workingImage = firstImageArray
iteration = 1

for file in filenames[1:20]:
    
    # Open the Image
    newImage = Image.open('2) No infiltration_No substrate/' + file)
    
    # Convert the image to black and white
    newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    newImageArray = numpy.array(newImageBW)
    #newImageArray = numpy.array(newImage)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    Image.fromarray(workingImage).save('../Image_Combination/2/BW/Stacked_Image_2_' + str(iteration) + '.png')
    #Image.fromarray(workingImage).save('../Image_Combination/2/Color/Stacked_Image_2_' + str(iteration) + '.png')

## 3) Infiltrated_no substrate

# Generating File List
filenames = ('Infiltrated_no substrate001.tif', 'Infiltrated_no substrate002.tif', 'Infiltrated_no substrate003.tif',
             'Infiltrated_no substrate004.tif', 'Infiltrated_no substrate005.tif', 'Infiltrated_no substrate006.tif',
             'Infiltrated_no substrate007.tif', 'Infiltrated_no substrate008.tif', 'Infiltrated_no substrate009.tif',
             'Infiltrated_no substrate010.tif', 'Infiltrated_no substrate011.tif', 'Infiltrated_no substrate012.tif',
             'Infiltrated_no substrate013.tif', 'Infiltrated_no substrate014.tif', 'Infiltrated_no substrate015.tif',
             'Infiltrated_no substrate016.tif', 'Infiltrated_no substrate017.tif', 'Infiltrated_no substrate018.tif',
             'Infiltrated_no substrate019.tif', 'Infiltrated_no substrate020.tif')

# Creating First Working Image
# Open the Image
firstImage = Image.open('3) Infiltrated_no substrate/' + filenames[0])
    
# Convert the image to black and white
#firstImageBW = firstImage.convert('L')
    
# Convert Image into Array
#firstImageArray = numpy.array(firstImageBW)
firstImageArray = numpy.array(firstImage)

# Saving First Image
#Image.fromarray(firstImageArray).save('../Image_Combination/3/BW/Stacked_Image_3_1.png')
Image.fromarray(firstImageArray).save('../Image_Combination/3/Color/Stacked_Image_3_1.png')

workingImage = firstImageArray
iteration = 1

for file in filenames[1:20]:
    
    # Open the Image
    newImage = Image.open('3) Infiltrated_no substrate/' + file)
    
    # Convert the image to black and white
    #newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    #newImageArray = numpy.array(newImageBW)
    newImageArray = numpy.array(newImage)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    #Image.fromarray(workingImage).save('../Image_Combination/3/BW/Stacked_Image_3_' + str(iteration) + '.png')
    Image.fromarray(workingImage).save('../Image_Combination/3/Color/Stacked_Image_3_' + str(iteration) + '.png')

## 4) No infiltrated with substrate

# Generating File List
filenames = ('no Infiltrated_with substrate001.tif', 'no Infiltrated_with substrate002.tif', 'no Infiltrated_with substrate003.tif',
             'no Infiltrated_with substrate004.tif', 'no Infiltrated_with substrate005.tif', 'no Infiltrated_with substrate006.tif',
             'no Infiltrated_with substrate007.tif', 'no Infiltrated_with substrate008.tif', 'no Infiltrated_with substrate009.tif',
             'no Infiltrated_with substrate010.tif', 'no Infiltrated_with substrate011.tif', 'no Infiltrated_with substrate012.tif',
             'no Infiltrated_with substrate013.tif', 'no Infiltrated_with substrate014.tif', 'no Infiltrated_with substrate015.tif',
             'no Infiltrated_with substrate016.tif', 'no Infiltrated_with substrate017.tif', 'no Infiltrated_with substrate018.tif',
             'no Infiltrated_with substrate019.tif', 'no Infiltrated_with substrate020.tif')

# Creating First Working Image
# Open the Image
firstImage = Image.open('4) No infiltrated with substrate/' + filenames[0])
    
# Convert the image to black and white
firstImageBW = firstImage.convert('L')
    
# Convert Image into Array
firstImageArray = numpy.array(firstImageBW)
#firstImageArray = numpy.array(firstImage)

# Saving First Image
Image.fromarray(firstImageArray).save('../Image_Combination/4/BW/Stacked_Image_4_1.png')
#Image.fromarray(firstImageArray).save('../Image_Combination/4/Color/Stacked_Image_4_1.png')

workingImage = firstImageArray
iteration = 1

for file in filenames[1:20]:
    
    # Open the Image
    newImage = Image.open('4) No infiltrated with substrate/' + file)
    
    # Convert the image to black and white
    newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    newImageArray = numpy.array(newImageBW)
    #newImageArray = numpy.array(newImage)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    Image.fromarray(workingImage).save('../Image_Combination/4/BW/Stacked_Image_4_' + str(iteration) + '.png')
    #Image.fromarray(workingImage).save('../Image_Combination/4/Color/Stacked_Image_4_' + str(iteration) + '.png')


#

