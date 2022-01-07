# 09/21/21 - Jose Mayorga
# 
# This script is designed to analyze combine/merge TIFF images.
#
# input_image - should be of '.tiff' format'

import numpy
from PIL import Image
import matplotlib.pyplot as plt

#### 1) Pst_NL1.2_V_glass slide ####

file1Data = {}

iteration = 1

#NL_1.2_V_40x_dark_1.tif

for file in range(1,340):
    #print('NL_1.2_V_40x_dark_' + str(file) + '.tif')
    
    if(file >= 120 and file < 140):
        print(file)
        continue
    
    if(file >= 201 and file < 220):
        print(file)
        continue
    
    if(file >= 230 and file < 330):
        print(file)
        continue
    
    file1Data[iteration] = numpy.array(Image.open('1) Pst_NL1.2_V_glass slide/' + 'NL_1.2_V_40x_dark_' + str(file) + '.tif').convert('L')).sum()
    iteration += 1

# Combining Images by Sum
for file in range(1, 340):
    
    if(file == 1):
        # Creating First Working Image
        # Open the Image
        firstImage = Image.open('1) Pst_NL1.2_V_glass slide/' + 'NL_1.2_V_40x_dark_' + str(file) + '.tif')
            
        # Convert the image to black and white
        firstImageBW = firstImage.convert('L')
            
        # Convert Image into Array
        firstImageArray = numpy.array(firstImageBW)
        
        # Saving First Image
        Image.fromarray(firstImageArray).save('../09_27_Image_Combination/Set1/Stacked_Image_1_1.png')
        
        workingImage = firstImageArray
        iteration = 1
        
        continue
    
    if(file >= 120 and file < 140):
         continue
    if(file >= 201 and file < 220):
         continue
    if(file >= 230 and file < 330):
         continue

    # Open the Image
    newImage = Image.open('1) Pst_NL1.2_V_glass slide/' + 'NL_1.2_V_40x_dark_' + str(file) + '.tif')
    
    # Convert the image to black and white
    newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    newImageArray = numpy.array(newImageBW)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    Image.fromarray(workingImage).save('../09_27_Image_Combination/Set1/' + str(iteration) + '.png')


## 2) Pst_lux_glass slide

file2Data = {}

iteration = 1

# pst_lux_40x_Re001.tif
for file in range(1, 201):
    
    if(file < 10):
        fileName = ('pst_lux_40x_Re00' + str(file) + '.tif')
    
    if(file >= 10 and file < 100):
        fileName = ('pst_lux_40x_Re0' + str(file) + '.tif')
    
    if(file >= 100):
        fileName = ('pst_lux_40x_Re' + str(file) + '.tif')
    
    file2Data[iteration] = numpy.array(Image.open('2) Pst_lux_glass slide/' + fileName).convert('L')).sum()
    iteration += 1

# Combining Images by Sum
for file in range(1, 201):
    
    if(file == 1):
        # Creating First Working Image
        # Open the Image
        firstImage = Image.open('2) Pst_lux_glass slide/' + 'pst_lux_40x_Re00' + str(file) + '.tif')
            
        # Convert the image to black and white
        firstImageBW = firstImage.convert('L')
            
        # Convert Image into Array
        firstImageArray = numpy.array(firstImageBW)
        
        # Saving First Image
        Image.fromarray(firstImageArray).save('../09_27_Image_Combination/Set2/Stacked_Image_2_1.png')
        
        workingImage = firstImageArray
        iteration = 1
        
        continue
    
    if(file < 10):
        fileName = ('pst_lux_40x_Re00' + str(file) + '.tif')
    
    if(file >= 10 and file < 100):
        fileName = ('pst_lux_40x_Re0' + str(file) + '.tif')
    
    if(file >= 100):
        fileName = ('pst_lux_40x_Re' + str(file) + '.tif')

    # Open the Image
    newImage = Image.open('2) Pst_lux_glass slide/' + fileName)
    
    # Convert the image to black and white
    newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    newImageArray = numpy.array(newImageBW)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    Image.fromarray(workingImage).save('../09_27_Image_Combination/Set2/' + str(iteration) + '.png')

## 3)Infiltrated_Sprayed

file3Data = {}

iteration = 1

# Infiltrated_Sprayed_Col-0_40x001.tif
for file in range(1, 201):
    
    if(file < 10):
        fileName = ('Infiltrated_Sprayed_Col-0_40x00' + str(file) + '.tif')
    
    if(file >= 10 and file < 100):
        fileName = ('Infiltrated_Sprayed_Col-0_40x0' + str(file) + '.tif')
    
    if(file >= 100):
        fileName = ('Infiltrated_Sprayed_Col-0_40x' + str(file) + '.tif')
    
    
    file3Data[iteration] = numpy.array(Image.open('3)Infiltrated_Sprayed/' + fileName).convert('L')).sum()
    iteration += 1

# Combining Images by Sum
for file in range(1, 201):
    
    if(file == 1):
        # Creating First Working Image
        # Open the Image
        firstImage = Image.open('3)Infiltrated_Sprayed/' + 'Infiltrated_Sprayed_Col-0_40x00' + str(file) + '.tif')
            
        # Convert the image to black and white
        firstImageBW = firstImage.convert('L')
            
        # Convert Image into Array
        firstImageArray = numpy.array(firstImageBW)
        
        # Saving First Image
        Image.fromarray(firstImageArray).save('../09_27_Image_Combination/Set3/Stacked_Image_3_1.png')
        
        workingImage = firstImageArray
        iteration = 1
        
        continue
    
    if(file < 10):
        fileName = ('Infiltrated_Sprayed_Col-0_40x00' + str(file) + '.tif')
    
    if(file >= 10 and file < 100):
        fileName = ('Infiltrated_Sprayed_Col-0_40x0' + str(file) + '.tif')
    
    if(file >= 100):
        fileName = ('Infiltrated_Sprayed_Col-0_40x' + str(file) + '.tif')

    # Open the Image
    newImage = Image.open('3)Infiltrated_Sprayed/' + fileName)
    
    # Convert the image to black and white
    newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    newImageArray = numpy.array(newImageBW)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    Image.fromarray(workingImage).save('../09_27_Image_Combination/Set3/' + str(iteration) + '.png')

## 4) Non-infiltrated_Sprayed

file4Data = {}

iteration = 1

# Non-Infiltrated_Sprayed_Col-0_40x001.tif
for file in range(1, 201):
    
    if(file < 10):
        fileName = ('Non-Infiltrated_Sprayed_Col-0_40x00' + str(file) + '.tif')
    
    if(file >= 10 and file < 100):
        fileName = ('Non-Infiltrated_Sprayed_Col-0_40x0' + str(file) + '.tif')
    
    if(file >= 100):
        fileName = ('Non-Infiltrated_Sprayed_Col-0_40x' + str(file) + '.tif')
    
    file4Data[iteration] = numpy.array(Image.open('4) Non-infiltrated_Sprayed/' + fileName).convert('L')).sum()
    iteration += 1

# Combining Images by Sum
for file in range(1, 201):
    
    if(file == 1):
        # Creating First Working Image
        # Open the Image
        firstImage = Image.open('4) Non-infiltrated_Sprayed/' + 'Non-Infiltrated_Sprayed_Col-0_40x00' + str(file) + '.tif')
            
        # Convert the image to black and white
        firstImageBW = firstImage.convert('L')
            
        # Convert Image into Array
        firstImageArray = numpy.array(firstImageBW)
        
        # Saving First Image
        Image.fromarray(firstImageArray).save('../09_27_Image_Combination/Set4/Stacked_Image_4_1.png')
        
        workingImage = firstImageArray
        iteration = 1
        
        continue
    
    if(file < 10):
        fileName = ('Non-Infiltrated_Sprayed_Col-0_40x00' + str(file) + '.tif')
    
    if(file >= 10 and file < 100):
        fileName = ('Non-Infiltrated_Sprayed_Col-0_40x0' + str(file) + '.tif')
    
    if(file >= 100):
        fileName = ('Non-Infiltrated_Sprayed_Col-0_40x' + str(file) + '.tif')

    # Open the Image
    newImage = Image.open('4) Non-infiltrated_Sprayed/' + fileName)
    
    # Convert the image to black and white
    newImageBW = newImage.convert('L')
    
    # Convert Image into Array
    newImageArray = numpy.array(newImageBW)
    
    # Combining with Working Image
    workingImage = workingImage + newImageArray
        
    # Saving Current Iteration
    iteration += 1
    Image.fromarray(workingImage).save('../09_27_Image_Combination/Set4/' + str(iteration) + '.png')


## Generating Figures

# Plot 1
plt.figure(figsize=(30, 6))
plt.bar(list(file1Data.keys()), list(file1Data.values()), tick_label = list(file1Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 1')
plt.ylim(9600000, 9850000)
plt.xticks(rotation = 90)
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.savefig('../09_27_Stat_Plots/09_27_Set1_Data.png')


# Plot 2
plt.figure(figsize=(30, 6))
plt.bar(list(file2Data.keys()), list(file2Data.values()), tick_label = list(file2Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 2')
#plt.ylim(9000000, 9600000)
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.ylim(9000000, 9200000)
plt.xticks(rotation = 90)
plt.savefig('../09_27_Stat_Plots/09_27_Set2_Data.png')

# Plot 3
plt.figure(figsize=(30, 6))
plt.bar(list(file3Data.keys()), list(file3Data.values()), tick_label = list(file3Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 3')
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.ylim(9000000, 9200000)
plt.xticks(rotation = 90)
plt.savefig('../09_27_Stat_Plots/09_27_Set3_Data.png')


# Plot 4
plt.figure(figsize=(30, 6))
plt.bar(list(file4Data.keys()), list(file4Data.values()), tick_label = list(file4Data.keys()))
plt.ylabel('Total Signal')
plt.xlabel('Image Number')
plt.title('Image Set 4')
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.ylim(9000000, 9200000)
plt.xticks(rotation = 90)
plt.savefig('../09_27_Stat_Plots/09_27_Set4_Data.png')

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
