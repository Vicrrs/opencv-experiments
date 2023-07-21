import cv2

img_gray = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/004_messi.jpg", cv2.IMREAD_GRAYSCALE)

# Binarização com metodo de
_, binary_img = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Imagem Binarizada", binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()