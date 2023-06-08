import cv2

PATH_IMG = r"C:\Users\rozas\Projects\opencv-experiments\imgs\004_messi.jpg"

# Lê a imagem do disco
img = cv2.imread(PATH_IMG)

# Forma da imagem em termos de pixel
(rows, cols) = img.shape[:2]

# getRotationMatrix2D cria uma matriz necessária para transformação.
# Queremos matriz para rotação w.r.t center a 45 graus sem escala.
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('modificado.jpg', res)
