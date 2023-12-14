

import os
import shutil
import csv
import sys

#Open ZZZZAllImages.csv. The four columns are Filename,Original Label,Final Label
#We use the Filename (which is the path of the image) to move the image to the Final Label
#the new directory of the image is C:\Users\Brandon\Desktop\Classes\E208\Homework\E208_Final\Relabel1\Final Label

#Open the csv file
with open('Relabelling2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #Skip the header
    next(reader)
    #Make a copy of the images in Cropped_Data_400 in Relabel1
    #Loop through C:\Users\Brandon\Desktop\Classes\E208\Homework\E208_Final\Cropped_Data_400\Algae, C:\Users\Brandon\Desktop\Classes\E208\Homework\E208_Final\Cropped_Data_400\Hard Coral, 
    #and C:\Users\Brandon\Desktop\Classes\E208\Homework\E208_Final\Cropped_Data_400\Soft Coral, and make a dictionary containing each image path as the key and the label as the value

    image_dict = {}

    #Loop through each directory
    for directory in ['Algae', 'Hard Coral', 'Soft Coral']:
        #Get the directory path
        directory_path = os.path.join('C:\\Users\\Brandon\\Desktop\\Classes\\E208\\Homework\\E208_Final\\Relabel1', directory)
        #Loop through each image in the directory
        for filename in os.listdir(directory_path):
            #Get the path of the image
            path = os.path.join(directory_path, filename)
            #Extract the specific filename from the path. For example, C:\Users\Brandon\Desktop\Classes\E208\Homework\E208_Final\Cropped_Data_400\Hard Coral\42004146701355876.jpg is the path, 
            #and 42004146701355876.jpg is the filename.
            filename = os.path.basename(path)
            #Get the label of the image
            label = directory
            #Add the image path and label to the dictionary
            image_dict[path] = [filename, label]

    #Loop through each row in the csv, and then modify the image_dict values to the final label
    for row in reader:
        #Get the path of the image
        path = row[0]
        #Get the final label of the image
        final_label = row[2]
        #Change the label of the image
        image_dict[path][1] = final_label

    #Now, loop through each directory and write it to C:\\Users\\Brandon\\Desktop\\Classes\\E208\\Homework\\E208_Final\\Relabel1'
    for key, value in image_dict.items():
        #Get the new directory path, only do if the value isn't Remove!!!
        if value[1] != "remove":
            new_directory_path = os.path.join('C:\\Users\\Brandon\\Desktop\\Classes\\E208\\Homework\\E208_Final\\Relabel2', value[1])
            #Copy the image to the new directory IF the label is NOT remove
            shutil.copy(key, new_directory_path)






