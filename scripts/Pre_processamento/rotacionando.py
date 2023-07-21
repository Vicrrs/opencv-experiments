import cv2

img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/007_estrada.jpg")

# Definindo o angulo de rotacao
angle = 45

# Obtendo o centro da imagem
center = (img.shape[1] // 2, img.shape[0] // 2)

# Definindo a matriz de rotacao
M = cv2.getRotationMatrix2D(center, angle, 1.0)

# Aplicando a rotacao na imagem
rotated_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Exibindo a imagem rotacionada
cv2.imshow("Imagem Rotacionada", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
