#We have a list of images in /Data. First, let's open 42003020401.jpg
#In annotations_PAC_TWN.csv, we have the coordinate of the image where a crop of size 244 x 244 will be taken.
#We will save the crop in /Cropped_Data

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Load the image into an array: img
img = plt.imread('Data/PAC_TWN/42003020401.jpg')

#Look up the name of the file in the quadratid column on annotations_PAC_TWN.csv
#The coordinates are in the columns y, x, and the height and width are 244 x 244
#Crop the image using the coordinates and height and width
# Save the cropped image as panda_cropped.jpg
# Import Image from PIL module
from PIL import Image

# Open the image
img = Image.open('Data/PAC_TWN/42003020401.jpg')

import pandas as pd
#Load the csv annotations_PAC_TWN.csv
df = pd.read_csv('annotations_PAC_TWN.csv')
#df is of the shape: 
# quadratid,y,x,label_name,label,func_group,method,data_set
#42004146101,217,389,"Other soft-corals no common Alcyoniidae and erects","SINV_SFC_O","Soft Coral","random","test"
#42004146101,280,190,"Other soft-corals no common Alcyoniidae and erects","SINV_SFC_O","Soft Coral","random","test"
#We will go through each row in df and crop the image using the coordinates and height and width

#Initialize for loop to go through each row
count = 0
for index, row in df.iterrows():
    count +=1
    if count >400:
        break
    #Get the quadratid
    quadratid = row['quadratid']
    img = Image.open('Data/PAC_TWN/' + str(quadratid) + '.jpg')
    label = row['func_group']
    print(label)
    plt.imshow(img)
    #Get the coordinates
    y = row['y']
    x = row['x']
    #Crop the image using the coordinates and height and width
    img_cropped = img.crop((x-122, y-122, x+122, y+122))
    #Save the cropped image as panda_cropped.jpg
    img_cropped.save('Cropped_Data/'+label+'/'+str(quadratid)+str(x)+str(y)+'.jpg')
    #Display the cropped image
    #plt.imshow(img_cropped)
    #plt.show()






