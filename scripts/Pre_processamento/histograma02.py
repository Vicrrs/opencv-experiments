# Importando as bibliotecas
import cv2
from matplotlib import pyplot as plt


def mostrar_img(PATH_IMG):
    img = cv2.imread(PATH_IMG)
    plt.imshow(img)
    plt.show()
    return img


def plot_histogram(img_path):
    img = cv2.imread(img_path)  # caminho da imagem
    azul, verde, vermelho = cv2.split(img)
    fig = plt.figure(figsize=(20, 5))
    # uma linha, 3 colunas, referente a primeira imagem
    ax1 = fig.add_subplot(131)
    ax1.hist(azul.ravel(), 256, [0, 256])
    plt.title("Histograma com canal azul")
    ########################################
    ax2 = fig.add_subplot(132)
    ax2.hist(verde.ravel(), 256, [0, 256])
    plt.title("Histograma com canal verde")
    ########################################
    ax3 = fig.add_subplot(133)
    ax3.hist(vermelho.ravel(), 256, [0, 256])
    plt.title("Histograma com canal vermelho")
    plt.show()


if __name__ == "__main__":
    img_path = r"C:\Users\rozas\Projects\opencv-experiments\imgs\004_messi.jpg"
    mostrar_img(img_path)
    plot_histogram(img_path)
