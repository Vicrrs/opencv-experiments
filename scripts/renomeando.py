import os
import re
import shutil

dir_path = r"E:\OPENCV_preprocess\astronauta\test002\nitido"

new_dir_path = r"E:\OPENCV_preprocess\astronauta\test002\rename_nitido"

os.makedirs(new_dir_path, exist_ok=True)

# Lista todos os arquivos no diretório de imagens
files = os.listdir(dir_path)

# Filtra apenas os arquivos .png e extrai o número do nome do arquivo
png_files = [f for f in files if f.endswith('.png')]
# Ordena os arquivos numericamente baseado nos números extraídos dos nomes
png_files.sort(key=lambda x: int(re.search(r'(\d+)', x).group()))

# Faz uma cópia de cada arquivo com um novo nome em ordem crescente
for i, file in enumerate(png_files, start=1):
    # Define o novo nome do arquivo
    new_file_name = f"{i}.png"
    # Caminho completo para o arquivo atual
    old_file_path = os.path.join(dir_path, file)
    # Caminho completo para o novo arquivo
    new_file_path = os.path.join(new_dir_path, new_file_name)
    
    # Copia o arquivo para o novo diretório com o novo nome
    shutil.copy(old_file_path, new_file_path)
