import cv2

# Para ler a imagem do disco, usamos função cv2.imread, no método abaixo
img = cv2.imread(
    r"C:\Users\rozas\Projects\opencv-experiments\imgs\Anumara_Vision.png")

# Criando janela GUI para exibir uma imagem na tela
# Primeiro parâmetro é o título da janela (deve estar no formato string)
# Segundo parâmetro é array da imagem
cv2.imshow("AnumaraVision", img)

"""
Para manter a janela na tela, usamos o método cv2.waitKey
Uma vez detectado a entrada de fechamento, ele liberará o controle
para a próxima linha
O primeiro parâmetro é para segurar a tela por milissegundos especificados
Deve ser um número inteiro positivo. Se 0 passar um parâmetro, então ele irá
segure a tela até o usuário fechá-la.
"""
cv2.waitKey(0)

# É para remover/excluir a janela GUI criada da tela e memória
cv2.destroyAllWindows()
