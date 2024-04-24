import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def calc_variance_laplacian(video_path):
    cap = cv2.VideoCapture(video_path)
    variancias = []
    while True:
        success, frame = cap.read()
        if not success:
            break
        variancias.append(cv2.Laplacian(frame, cv2.CV_64F).var())
    cap.release()
    return variancias

def calcular_limiares_adaptativos(variancias):
    limiar_inferior = np.percentile(variancias, 25)
    limiar_superior = np.percentile(variancias, 75)
    return limiar_inferior, limiar_superior

def salvar_frame_e_log(frame, frame_count, categoria, laplacia_var, categorias_dirs, logs_files):
    filename = f"{frame_count}.png"
    filepath = os.path.join(categorias_dirs[categoria], filename)
    cv2.imwrite(filepath, frame)
    with open(logs_files[categoria], 'a') as f:
        f.write(f"{filename}, Variância de Laplaciano: {laplacia_var}\n")

def processar_video_e_gerar_grafico(video_path, limiar_inferior, limiar_superior, categorias_dirs, logs_files):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    variancias_por_categoria = {'desfocado': [], 'nitido': [], 'intermediario': []}
    while True:
        success, frame = cap.read()
        if not success:
            break
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
    cap.release()
    
    # Gerando gráficos
    for categoria, variancias in variancias_por_categoria.items():
        plt.figure()
        plt.hist(variancias, bins=20, alpha=0.7, label=categoria)
        plt.title(f"Distribuição de Variância de Laplaciano - {categoria.capitalize()}")
        plt.xlabel('Variância de Laplaciano')
        plt.ylabel('Frequência')
        plt.legend()
    plt.show()

# Configurações iniciais
video_path = r'C:\\Users\\rozas\\Videos\\Drive\\astronauta.mp4' # Atualize para o caminho do seu vídeo
base_dir = r'E:\OPENCV_preprocess\astronauta'   # Atualize para o seu diretório base
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

# Cria os diretórios se não existirem
for dir in categorias_dirs.values():
    os.makedirs(dir, exist_ok=True)

# Limpa arquivos de log antigos
for log_file in logs_files.values():
    if os.path.exists(log_file):
        os.remove(log_file)

# Processamento e geração de gráfico
variancias = calc_variance_laplacian(video_path)
limiar_inferior, limiar_superior = calcular_limiares_adaptativos(variancias)
processar_video_e_gerar_grafico(video_path, limiar_inferior, limiar_superior, categorias_dirs, logs_files)
