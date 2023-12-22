# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png all 
# the way till n.png where n is the number of png files in that folder. 
# Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os
path = "E:\Demo"

png_list = []

def png_finder():
    for file in os.listdir(path):
        if file.endswith(".png"):
            png_list.append(file)
            
png_finder()

if png_list:
    print(f"Found .png files at {path}")
    print(png_list)

    i=1
    for file in png_list:
        os.rename(os.path.join(path, file), os.path.join(path, f"{str(i)}.png"))
        i += 1
    print(f"Renamed all .png files from {path} successfully.")
else:
    print(f"No PNG files found at {path}.")


# import os

# path = "E:\\Demo"
# png_list = []

# def png_finder():
#     for file in os.listdir(path):
#         if file.endswith(".png"):
#             png_list.append(file)

# # Call the function to populate the list
# png_finder()

# # Check if there are any PNG files before attempting to rename
# if png_list:
#     print("Found PNG files:")
#     print(png_list)

#     # Rename the files using enumerate
#     for i, file in enumerate(png_list, start=1):
#         os.rename(os.path.join(path, file), os.path.join(path, f"{i}.png"))

#     print(f"Renamed all .png files from {path} successfully")
# else:
#     print("No PNG files found in the specified directory.")



# import os

# path = "E:\\Demo"

# def png_finder():
#     return [file for file in os.listdir(path) if file.endswith(".png")]

# # Call the function to get the list
# png_list = png_finder()

# # Check if there are any PNG files before attempting to rename
# if png_list:
#     print("Found PNG files:")
#     print(png_list)

#     # Rename the files using a list comprehension
#     [os.rename(os.path.join(path, file), os.path.join(path, f"{i}.png")) for i, file in enumerate(png_list, start=1)]

#     print(f"Renamed all .png files from {path} successfully")
# else:
#     print("No PNG files found in the specified directory.")


      

                