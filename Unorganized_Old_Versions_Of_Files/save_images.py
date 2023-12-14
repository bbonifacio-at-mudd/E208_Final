import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import os


#Look up the name of the file in the quadratid column on annotations_PAC_TWN.csv
#The coordinates are in the columns y, x, and the height and width are 244 x 244
#Crop the image using the coordinates and height and width
# Save the cropped image as panda_cropped.jpg
# Import Image from PIL module



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
    if count > 4000: #load the first 4000 images
        break
    #Get the quadratid
    quadratid = row['quadratid']
    img = Image.open('Original_Data/PAC_TWN/' + str(quadratid) + '.jpg')
    bigger_group = row['func_group']
    label = row['label']

    if index % 100 == 0:
        print(index)
    #plt.imshow(img)
    #Get the coordinates
    y = row['y']
    x = row['x']
    #Crop the image using the coordinates and height and width
    img_cropped = img.crop((x-122, y-122, x+122, y+122))

    #Check if the folder exists. If it doesn't exist, make the folder for All_Labels_4000/label
    if not os.path.exists('All_Labels_4000/'+bigger_group):
        os.makedirs('All_Labels_4000/'+bigger_group)
    if not os.path.exists('All_Labels_4000/'+bigger_group+"/"+label):
        os.makedirs('All_Labels_4000/'+bigger_group+"/"+label)
    #Save the cropped image as panda_cropped.jpg
    img_cropped.save('All_Labels_4000/'+bigger_group+"/"+label+'/'+str(quadratid)+str(x)+str(y)+'.jpg')
    #Display the cropped image
    #plt.imshow(img_cropped)
    #plt.show()








