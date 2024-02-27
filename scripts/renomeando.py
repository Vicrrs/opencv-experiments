import os
import re
import shutil

dir_path = r"E:\OPENCV_preprocess\astronauta\test002\nitido"

new_dir_path = r"E:\OPENCV_preprocess\astronauta\test002\rename_nitido"

os.makedirs(new_dir_path, exist_ok=True)

files = os.listdir(dir_path)
png_files = [f for f in files if f.endswith('.png')]
png_files.sort(key=lambda x: int(re.search(r'(\d+)', x).group()))

for i, file in enumerate(png_files, start=1):
    new_file_name = f"{i}.png"
    old_file_path = os.path.join(dir_path, file)
    new_file_path = os.path.join(new_dir_path, new_file_name)
    
    shutil.copy(old_file_path, new_file_path)
