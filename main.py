import os
from readpicture import readpictures

folder = r"C:\Users\DELL\OneDrive\Desktop\picture"

image_paths = [
    os.path.join(folder, filename)
    for filename in os.listdir(folder)
]

for i in image_paths:
    readpictures(i)
