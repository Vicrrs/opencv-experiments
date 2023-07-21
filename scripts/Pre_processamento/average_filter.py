import cv2

img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/008_tomates.jpeg")

# Aplicando o filtro de média com a janela de 5x5
blurred_img = cv2.blur(img, (5, 5))

cv2.imshow("Imagem suavizada", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
