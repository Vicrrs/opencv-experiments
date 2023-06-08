import cv2

# caminho da imagem
IMG_PATH = r"caminho da imagem"

img = cv2.imread(IMG_PATH)

# cria a janela
cv2.imshow("Janela", img)

# mostra a janela criada e aguarda o evento de uma tecla
k = cv2.waitKey(0)

# se s for pressionado salva a imagem
if k == ord("s"):
    cv2.imwrite("modificado.jpg", img)

cv2.destroyAllWindows()
