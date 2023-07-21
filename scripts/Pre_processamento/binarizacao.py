import cv2

img_gray = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/003_Lenna.png", cv2.IMREAD_GRAYSCALE)

# Aplicando a binarização usando um limiar fixo de 127
_, binary_img = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Imagem Binarizada", binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
