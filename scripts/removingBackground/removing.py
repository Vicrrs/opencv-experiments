import cv2
import numpy as np

# Carregue a imagem em OpenCV
image = cv2.imread(r'C:\Users\Inovacao\Documents\github\opencv-experiments\imgs\anumara(1).png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray_image, 50, 150)
dilated_edges = cv2.dilate(edges, np.ones((3,3), np.uint8), iterations=1)
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
mask = np.zeros_like(gray_image)
cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)
_, mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)
output = np.zeros_like(image_rgb, dtype=np.uint8)
output[mask == 255] = image_rgb[mask == 255]
mask_three_channel = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
result = np.hstack((image_rgb, mask_three_channel, output))
output_file_path = 'image_with_background_removed.png'

cv2.imwrite(output_file_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
