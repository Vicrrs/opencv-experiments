import cv2

# espscificando o caminho das duas imagens que seram somadas
img1 = cv2.imread(
    r"C:\Users\rozas\Projects\opencv-experiments\imgs\004_messi.jpg")
img2 = cv2.imread(
    r"C:\Users\rozas\Projects\opencv-experiments\imgs\007_estrada.jpg")

# Para as imagens serem somadas elas precisam ter o mesmo tamanho
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# cv2.addWeighted é aplciado sobre as entradas de imagem com paramentros
soma = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# a janela mostra a imagem de saida com a soma ponderada
cv2.imshow("Imagem Ponderada", soma)

# Deslocar qualquer uso de memoria associado
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
