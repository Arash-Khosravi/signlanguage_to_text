import os
import splitfolders

path = os.getcwd()
print(path)
all_images_path = f"{os.path.abspath(os.path.join(path)) + '/images/colletedimages'}"
print(all_images_path)
new_data = f"{os.path.abspath(os.path.join(path)) + '/new_data'}"
print(new_data)
splitfolders.ratio(
    all_images_path, output=new_data, ratio=(0.7, 0.2, 0.1)
)
