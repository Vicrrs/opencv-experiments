import cv2
import os

# Caminho para o vídeo de entrada
video_path = r'C:\Users\rozas\Videos\Drive\astronauta.mp4'

# Salvando as imagens
img_dir = r'E:\OPENCV_preprocess\astronauta\test001'
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

cap = cv2.VideoCapture(video_path)    

frame_count = 0
while True:
    success, frame = cap.read()
    if success:
        cv2.imwrite(os.path.join(img_dir, f'frame_{frame_count}.png'), frame)
        frame_count += 1
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
