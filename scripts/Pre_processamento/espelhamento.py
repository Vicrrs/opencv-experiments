import cv2

img = cv2.imread("/home/tkroza/Projects_python/opencv-experiments/imgs/Anumara_Vision.png")

# Espelhando imagem horizontalmente
flipped_img = cv2.flip(img, 1)

cv2.imshow("Imagem Espelhada", flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
