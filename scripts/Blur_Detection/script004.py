import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def calc_variance_laplacian(images_dir):
    variancias = []
    for filename in os.listdir(images_dir):
        img_path = os.path.join(images_dir, filename)
        if os.path.isfile(img_path):
            frame = cv2.imread(img_path)
            variancias.append(cv2.Laplacian(frame, cv2.CV_64F).var())
    return variancias

def calcular_limiares_adaptativos(variancias):
    limiar_inferior = np.percentile(variancias, 25)
    limiar_superior = np.percentile(variancias, 75)
    return limiar_inferior, limiar_superior

def salvar_frame_e_log(frame, frame_count, categoria, laplacian_var, categorias_dirs, logs_files):
    filename = f"{frame_count}.png"
    filepath = os.path.join(categorias_dirs[categoria], filename)
    cv2.imwrite(filepath, frame)
    with open(logs_files[categoria], 'a') as f:
        f.write(f"{filename}, Variância de Laplaciano: {laplacian_var}\n")

def processar_imagens_e_gerar_grafico(images_dir, limiar_inferior, limiar_superior, categorias_dirs, logs_files):
    frame_count = 0
    variancias_por_categoria = {'desfocado': [], 'nitido': [], 'intermediario': []}
    for filename in os.listdir(images_dir):
        img_path = os.path.join(images_dir, filename)
        if os.path.isfile(img_path):
            frame = cv2.imread(img_path)
            laplacian_var = cv2.Laplacian(frame, cv2.CV_64F).var()
            if laplacian_var < limiar_inferior:
                categoria = 'desfocado'
            elif laplacian_var > limiar_superior:
                categoria = 'nitido'
            else:
                categoria = 'intermediario'

            variancias_por_categoria[categoria].append(laplacian_var)
            salvar_frame_e_log(frame, frame_count, categoria, laplacian_var, categorias_dirs, logs_files)
            frame_count += 1

    # Gerando gráficos
    for categoria, variancias in variancias_por_categoria.items():
        plt.figure()
        plt.hist(variancias, bins=20, alpha=0.7, label=categoria)
        plt.title(f"Distribuição de Variância de Laplaciano - {categoria.capitalize()}")
        plt.xlabel('Variância de Laplaciano')
        plt.ylabel('Frequência')
        plt.legend()
    plt.show()


images_dir = r'C:\\Users\\rozas\\Videos\\Drive\\astronauta.mp4'  
base_dir = r'E:\OPENCV_preprocess\astronauta'  
categorias_dirs = {
    'desfocado': os.path.join(base_dir, 'desfocado'),
    'nitido': os.path.join(base_dir, 'nitido'),
    'intermediario': os.path.join(base_dir, 'intermediario'),
}
logs_files = {
    'desfocado': os.path.join(base_dir, 'log_desfocado.txt'),
    'nitido': os.path.join(base_dir, 'log_nitido.txt'),
    'intermediario': os.path.join(base_dir, 'log_intermediario.txt'),
}

for dir in categorias_dirs.values():
    os.makedirs(dir, exist_ok=True)


for log_file in logs_files.values():
    if os.path.exists(log_file):
        os.remove(log_file)

# Processamento/geração de gráfico
variancias = calc_variance_laplacian(images_dir)
limiar_inferior, limiar_superior = calcular_limiares_adaptativos(variancias)
processar_imagens_e_gerar_grafico(images_dir, limiar_inferior, limiar_superior, categorias_dirs, logs_files)
