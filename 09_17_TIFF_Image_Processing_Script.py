# 09/17/21 - Jose Mayorga
# 
# This script is designed to analyze combine/merge TIFF images.
#
# input_image - should be of '.tiff' format'

import numpy
from PIL import Image
import matplotlib.pyplot as plt

#### 1) Infiltrated_substrate ####

# Generating File List
filenames = ('Infiltrated_NL1.2_V_luminiscence001.tif', 'Infiltrated_NL1.2_V_luminiscence002.tif', 'Infiltrated_NL1.2_V_luminiscence003.tif',
 'Infiltrated_NL1.2_V_luminiscence004.tif', 'Infiltrated_NL1.2_V_luminiscence005.tif', 'Infiltrated_NL1.2_V_luminiscence006.tif',
 'Infiltrated_NL1.2_V_luminiscence007.tif', 'Infiltrated_NL1.2_V_luminiscence008.tif', 'Infiltrated_NL1.2_V_luminiscence009.tif',
 'Infiltrated_NL1.2_V_luminiscence010.tif', 'Infiltrated_NL1.2_V_luminiscence011.tif', 'Infiltrated_NL1.2_V_luminiscence012.tif',
 'Infiltrated_NL1.2_V_luminiscence013.tif', 'Infiltrated_NL1.2_V_luminiscence014.tif', 'Infiltrated_NL1.2_V_luminiscence015.tif',
 'Infiltrated_NL1.2_V_luminiscence016.tif', 'Infiltrated_NL1.2_V_luminiscence017.tif', 'Infiltrated_NL1.2_V_luminiscence018.tif',
 'Infiltrated_NL1.2_V_luminiscence019.tif', 'Infiltrated_NL1.2_V_luminiscence020.tif')

file1Data = {}

iteration = 1

for file in filenames:
    file1Data[iteration] = numpy.array(Image.open('1) Infiltrated_substrate/' + file).convert('L')).sum()
    iteration += 1

## 2) No infiltration_No substrate

# Generating File List
filenames = ('1.tif', '2.tif', '3.tif', '4.tif', '5.tif', '6.tif', '7.tif', '8.tif', '9.tif', '10.tif',
             '11.tif', '12.tif', '13.tif', '14.tif', '15.tif', '16.tif', '17.tif', '18.tif', '19.tif', '20.tif')

file2Data = {}

iteration = 1

for file in filenames:
    file2Data[iteration] = numpy.array(Image.open('2) No infiltration_No substrate/' + file).convert('L')).sum()
    iteration += 1

## 3) Infiltrated_no substrate

# Generating File List
filenames = ('Infiltrated_no substrate001.tif', 'Infiltrated_no substrate002.tif', 'Infiltrated_no substrate003.tif',
             'Infiltrated_no substrate004.tif', 'Infiltrated_no substrate005.tif', 'Infiltrated_no substrate006.tif',
             'Infiltrated_no substrate007.tif', 'Infiltrated_no substrate008.tif', 'Infiltrated_no substrate009.tif',
             'Infiltrated_no substrate010.tif', 'Infiltrated_no substrate011.tif', 'Infiltrated_no substrate012.tif',
             'Infiltrated_no substrate013.tif', 'Infiltrated_no substrate014.tif', 'Infiltrated_no substrate015.tif',
             'Infiltrated_no substrate016.tif', 'Infiltrated_no substrate017.tif', 'Infiltrated_no substrate018.tif',
             'Infiltrated_no substrate019.tif', 'Infiltrated_no substrate020.tif')

file3Data = {}

iteration = 1

for file in filenames:
    file3Data[iteration] = numpy.array(Image.open('3) Infiltrated_no substrate/' + file).convert('L')).sum()
    iteration += 1

## 4) No infiltrated with substrate

# Generating File List
filenames = ('no Infiltrated_with substrate001.tif', 'no Infiltrated_with substrate002.tif', 'no Infiltrated_with substrate003.tif',
             'no Infiltrated_with substrate004.tif', 'no Infiltrated_with substrate005.tif', 'no Infiltrated_with substrate006.tif',
             'no Infiltrated_with substrate007.tif', 'no Infiltrated_with substrate008.tif', 'no Infiltrated_with substrate009.tif',
             'no Infiltrated_with substrate010.tif', 'no Infiltrated_with substrate011.tif', 'no Infiltrated_with substrate012.tif',
             'no Infiltrated_with substrate013.tif', 'no Infiltrated_with substrate014.tif', 'no Infiltrated_with substrate015.tif',
             'no Infiltrated_with substrate016.tif', 'no Infiltrated_with substrate017.tif', 'no Infiltrated_with substrate018.tif',
             'no Infiltrated_with substrate019.tif', 'no Infiltrated_with substrate020.tif')

file4Data = {}

iteration = 1

for file in filenames:
    file4Data[iteration] = numpy.array(Image.open('4) No infiltrated with substrate/' + file).convert('L')).sum()
    iteration += 1

## Generating Figures

# Plot 1
plt.bar(list(file1Data.keys()), list(file1Data.values()), tick_label = list(file1Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 1')
plt.ylim(7500000, 7850000)
plt.ticklabel_format(style = 'plain', axis = 'y')

# Plot 2
plt.bar(list(file2Data.keys()), list(file2Data.values()), tick_label = list(file2Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 2')
plt.ylim(9000000, 9600000)
plt.ticklabel_format(style = 'plain', axis = 'y')

# Plot 3
plt.bar(list(file3Data.keys()), list(file3Data.values()), tick_label = list(file3Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 3')
plt.ylim(7500000, 7700000)
plt.ticklabel_format(style = 'plain', axis = 'y')

# Plot 4
plt.bar(list(file4Data.keys()), list(file4Data.values()), tick_label = list(file4Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 4')
plt.ylim(7500000, 7800000)
plt.ticklabel_format(style = 'plain', axis = 'y')

#

### Multiplying Images and in an atempt to increase Signal


## Image 1
imageArray = numpy.array(Image.open('../Image_Combination/1/BW/Stacked_Image_1_20.png').convert('L')) 

multDict = {
    2 : imageArray*imageArray,
    3 : imageArray*imageArray*imageArray,
    4 : imageArray*imageArray*imageArray*imageArray,
    5 : imageArray*imageArray*imageArray*imageArray*imageArray,
    6 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    7 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    8 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    9 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    10: imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray
    }

for index in range(2, 11):
    # Multiplied by a constant
    Image.fromarray(imageArray * index).save('../Image_Combination/1/Multiplied_Images/1_20_Image_Multiplication_' + str(index) + '.png')
    # Self Multiply
    Image.fromarray(multDict[index]).save('../Image_Combination/1/Power_Images/1_20_Image_Power_' + str(index) + '.png')


## Image 2
imageArray = numpy.array(Image.open('../Image_Combination/2/BW/Stacked_Image_2_20.png').convert('L')) 

multDict = {
    2 : imageArray*imageArray,
    3 : imageArray*imageArray*imageArray,
    4 : imageArray*imageArray*imageArray*imageArray,
    5 : imageArray*imageArray*imageArray*imageArray*imageArray,
    6 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    7 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    8 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    9 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    10: imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray
    }

for index in range(2, 11):
    # Multiplied by a constant
    Image.fromarray(imageArray * index).save('../Image_Combination/2/Multiplied_Images/2_20_Image_Multiplication_' + str(index) + '.png')
    # Self Multiply
    Image.fromarray(multDict[index]).save('../Image_Combination/2/Power_Images/2_20_Image_Power_' + str(index) + '.png')


## Image 3
imageArray = numpy.array(Image.open('../Image_Combination/3/BW/Stacked_Image_3_20.png').convert('L')) 

multDict = {
    2 : imageArray*imageArray,
    3 : imageArray*imageArray*imageArray,
    4 : imageArray*imageArray*imageArray*imageArray,
    5 : imageArray*imageArray*imageArray*imageArray*imageArray,
    6 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    7 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    8 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    9 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    10: imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray
    }

for index in range(2, 11):
    # Multiplied by a constant
    Image.fromarray(imageArray * index).save('../Image_Combination/3/Multiplied_Images/3_20_Image_Multiplication_' + str(index) + '.png')
    # Self Multiply
    Image.fromarray(multDict[index]).save('../Image_Combination/3/Power_Images/3_20_Image_Power_' + str(index) + '.png')

## Image 4
imageArray = numpy.array(Image.open('../Image_Combination/4/BW/Stacked_Image_4_20.png').convert('L')) 

multDict = {
    2 : imageArray*imageArray,
    3 : imageArray*imageArray*imageArray,
    4 : imageArray*imageArray*imageArray*imageArray,
    5 : imageArray*imageArray*imageArray*imageArray*imageArray,
    6 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    7 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    8 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    9 : imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray,
    10: imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray*imageArray
    }

for index in range(2, 11):
    # Multiplied by a constant
    Image.fromarray(imageArray * index).save('../Image_Combination/4/Multiplied_Images/4_20_Image_Multiplication_' + str(index) + '.png')
    # Self Multiply
    Image.fromarray(multDict[index]).save('../Image_Combination/4/Power_Images/4_20_Image_Power_' + str(index) + '.png')












#
