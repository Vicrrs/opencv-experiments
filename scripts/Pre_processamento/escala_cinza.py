import cv2

# Carregando a imagem em escala de cinza
gray_img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/004_messi.jpg", cv2.IMREAD_GRAYSCALE)

# Exibindo a imagem
cv2.imshow("Teste", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
