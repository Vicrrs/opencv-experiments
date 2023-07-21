import cv2

# Carregando a imagem
img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/007_estrada.jpg")

# Definindo a nova largura
new_width = 200

# Calculando a proporcao de redimensionamento
ratio = float(new_width) / img.shape[1]

# Calculando a nova altura matendo a proporcao
new_height = int(img.shape[0] * ratio)

# Redimensionando a imagem
resized_img = cv2.resize(img, (new_width, new_height))

# Exibindo a imagem redimensionada
cv2.imshow("Imagem redimensionada", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
