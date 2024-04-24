import cv2

def find_largest_contour(image):
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
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def save_image(image, file_path):
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, image_bgr)


image_path = r'C:\Users\rozas\Documents\Projetos_GITHUB\opencv-experiments\imgs\produtos\activia.jpg'
output_path = 'bare_cropped.png'
image = load_image(image_path)
largest_contour = find_largest_contour(image)
cropped_product = crop_largest_contour(image, largest_contour)
save_image(cropped_product, output_path)
