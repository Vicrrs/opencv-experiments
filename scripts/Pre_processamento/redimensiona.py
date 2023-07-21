import cv2

# Carregando a imagem
img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/004_messi.jpg")

# Redimensionando a imagem para uma largura e altura específicas
width, height = 500, 300
resized_image = cv2.resize(img, (width, height))

# Exibindo a imagem
cv2.imshow("Imagem redimensionada", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
