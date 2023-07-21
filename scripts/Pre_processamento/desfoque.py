import cv2

# Carregando a imagem
img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/004_messi.jpg")

# Aplicando um desfoque gaussiano na imagem
blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

# Exibindo a imagem com desfoque
cv2.imshow("Imagem com Desfoque", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
