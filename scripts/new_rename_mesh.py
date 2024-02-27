import os
from shutil import copy2


source_dir = r"E:\OPENCV_preprocess\astronauta\test002\nitido" 

dest_dir = r'E:\OPENCV_preprocess\astronauta\test002\rename_mesh'  

os.makedirs(dest_dir, exist_ok=True)

file_list = sorted(os.listdir(source_dir), key=lambda x: int(x.split('.')[0]))

# Renomear arquivos em ordem crescente começando de 1
for new_index, filename in enumerate(file_list, start=1):
    new_filename = f"{new_index}.png"
    source_path = os.path.join(source_dir, filename)
    dest_path = os.path.join(dest_dir, new_filename)
    copy2(source_path, dest_path)
