# Criar uma classe para representar uma imagem em escala de cinza.
class ImagemEscalaCinza:
    def __init__(self, matriz_pixels):
        self.matriz_pixels = matriz_pixels

    def mostrar_imagem(self):
        for linha in self.matriz_pixels:
            print(" ".join(str(pixel) for pixel in linha))


# Exemplo de uso:
imagem = ImagemEscalaCinza([[0, 0, 0], [255, 255, 255], [128, 128, 128]])
imagem.mostrar_imagem()
