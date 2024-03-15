import cv2
import numpy as np

def find_largest_contour(image):
    if image.shape[2] == 4:
        alpha_channel = image[:, :, 3]
        _, thresh = cv2.threshold(alpha_channel, 0, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(contours, key=cv2.contourArea)
    return largest_contour

def crop_largest_contour(image, contour):
    x, y, w, h = cv2.boundingRect(contour)
    cropped_image = image[y:y+h, x:x+w]
    return cropped_image

def load_image(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def save_image(image, file_path):
    if image.shape[2] == 4:
        image_bgra = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
    else:
        image_bgra = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, image_bgra)

image_path = r'C:\Users\Inovacao\Documents\github\opencv-experiments\imgs\produtos\deline.png'
output_path = 'cropped_image.png'

image = load_image(image_path)
largest_contour = find_largest_contour(image)
cropped_product = crop_largest_contour(image, largest_contour)
save_image(cropped_product, output_path)
