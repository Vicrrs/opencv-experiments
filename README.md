# opencv-experiments
Transferring to the repository an updated version of the experiments I performed with opencv

# Introdução

OpenCV -> Visão computacional com Python e OpenCV

* Ciência que estuda e desenvolve tecnologias que permitem que as máquinas enxerguem e extraem características de um meio/cena.
* Captação por sensores e/ou dispositivos
* Reconhecer, manipular e processar.

![vc](https://github.com/Vicrrs/opencv-experiments/assets/87845548/d74622e7-f682-4b44-816f-0c0245895b84)


### Sistema da Visão Computacional

![sistema_VC](https://github.com/Vicrrs/opencv-experiments/assets/87845548/fd8313a9-b656-45be-8926-dae00cd5ca1c)


## Lendo_img.py
Para ler as imagens é usado o método cv2.imread(). Este método carrega uma imagem do arquivo especificado.
Se a imagem não puder ser lida (por causa de arquivo ausente, permissões impróprias, formato não suportado ou inválido),
esse método retornará uma matriz vazia.

Sintaxe: ```cv2.imread(caminho, sinalizador)```

Parâmetros:

    path: Uma string representando o caminho da imagem a ser lida.

    flag: Especifica a forma como a imagem deve ser lida. Seu valor padrão é cv2.IMREAD_COLOR

Valor de retorno: este método retorna uma imagem que é carregada do arquivo especificado.

A imagem deve estar no diretório de trabalho ou um caminho completo da imagem deve ser fornecido.

* cv2.IMREAD_COLOR: Especifica para carregar uma imagem colorida. Qualquer transparência de imagem será negligenciada.
É a bandeira padrão. Alternativamente, podemos passar o valor inteiro 1 para este sinalizador.
* cv2.IMREAD_GRAYSCALE: Especifica para carregar uma imagem em modo de escala de cinza. Alternativamente,
podemos passar o valor inteiro 0 para este sinalizador.
* cv2.IMREAD_UNCHANGED: Especifica para carregar uma imagem como tal incluindo o canal alfa. Alternativamente,
podemos passar o valor inteiro -1 para este sinalizador.

## Lendo e salvando a imagem
Caso você faça alguma modificação pode usar a função
```cv2.imwrite()```
para poder salvar a modificação!


# Pré-processamento

## Histograma de cores

O histograma de uma imagem é a distribuição da frequência dos níveis de cinza em relação ao número de amostras. Essa distribuição nos fornece informação sobre a qualidade da imagem, principalmente no que diz respeito a intensidade luminosa

Função: ```Hist(img, num1, intervalo)```

    1. img - imagem que vamos trabalhar
    2. num1 - numero de elementos distintos que podem ser representados
    3. intervalo - intervalo entre os elementos

Função: ```Ravel()```

    Img = Matriz de entrada, no caso a imagem. Os elementos em um são lidos na ordem específicada e empacotados com matriz 1D
    Saída: retorna uma matriz plana contínua (Matriz 1D com todos os elemntos da matriz de entrada e com o mesmo tipo que ela)

## Girando imagem
Processamento de imagens em Python (escalonamento, rotação, deslocamento e detecção de bordas)

As imagens podem ser giradas em qualquer grau no sentido horário ou não. Só precisamos definir a matriz de rotação listando o ponto de rotação, o grau de rotação e o fator de escala.

## Adição de imagens

Podemos adicionar duas imagens usando a função cv2.add() . Isso adiciona diretamente pixels de imagem
nas duas imagens.

Sintaxe: cv2.add(img1, img2)

Mas adicionar os pixels não é uma situação ideal. Então, usamos cv2.addweighted(). Lembre-se, ambas as imagens devem ter o mesmo tamanho e profundidade.

Por isso foi aplicado a função ```cv2.resize```, para caso as imagens não tenham o mesmo tamanho, seja feito um redimensionamento.

A sintaxe da função ```cv2.resize``` é a seguinte:

```
resized_image = cv2.resize(image, (new_width, new_height))
```
    - image: É a imagem de entrada que será redimensionada.
    - new_width: É a largura desejada para a imagem redimensionada.
    - new_height: É a altura desejada para a imagem redimensionada.

No código fornecido, img2.shape[1] retorna a largura da imagem img2 e img2.shape[0] retorna a altura da imagem img2. Esses valores são passados para a função cv2.resize() como o novo tamanho desejado para a imagem img1.


Sintaxe : ```cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)```

Parâmetros :

    img1 : Matriz da primeira imagem de entrada (canal único, 8 bits ou ponto flutuante)
    wt1 : Peso dos primeiros elementos da imagem de entrada a serem aplicados a imagem final
    img2 : Matriz da segunda imagem de entrada (canal único, 8 bits ou ponto flutuante)
    wt2 : Peso dos elementos da segunda imagem de entrada a serem aplicados à imagem final
    gammaValue : Medição da luz

## Subtração de imagem

Assim como a adição, podemos subtrair os valores de pixel em duas imagens e mesclá-los com a ajuda de ```cv2.subtract()```.
As imagens ainda devem ter o mesmo tamanho e profundidade.

Sintaxe: ```cv2.subtract(src1, src2)```
