import cv2
from matplotlib import pyplot as plt


def mostra_img(PATH_IMG):
    img = cv2.imread(PATH_IMG)
    cv2.imshow("Imagem", img)
    key = cv2.waitKey(0)
    if key == ord("s"):
        cv2.imwrite('Cinza.jpg', img)
    cv2.destroyAllWindows()
    return img


def plot_histogram(img_path):
    img = cv2.imread(img_path, 0)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


if __name__ == "__main__":
    img_path = r"C:\Users\rozas\Projects\opencv-experiments\imgs\004_messi.jpg"
    mostra_img(img_path)
    plot_histogram(img_path)
