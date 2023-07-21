import cv2

# Carregando a imgaem em escala de cinza
gray_img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/012_hospital2.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicando o algoritmo de detecção de bordas
edges = cv2.Canny(gray_img, 100, 200)

# Exibindo as bordas detectadas
cv2.imshow("Bordas detectadas", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
