# opencv-experiments
Transferring to the repository an updated version of the experiments I performed with opencv

# Introdução

OpenCV -> Visão computacional com Python e OpenCV

* Ciência que estuda e desenvolve tecnologias que permitem que as máquinas enxerguem e extraem características de um meio/cena.
* Captação por sensores e/ou dispositivos
* Reconhecer, manipular e processar.

![vc](https://github.com/Vicrrs/opencv-experiments/assets/87845548/d74622e7-f682-4b44-816f-0c0245895b84)


## O que é pré-processamento de imagem e por que é importante?

O pré-processamento de imagens é o processo de manipular dados brutos de imagem em um formato utilizável e significativo. Ele perminte eliminar distorções indesejadas e melhorar as qualidades específicas essenciais para aplicações indesejadas e melhorar as qualidades específicas essenciais para aplicações de visão computacional. O pré-processamento é um primeiro passo cricial para preparar os dados de imagens antes de alimentá-los em modelos de aprendizado de máquina.

Existem várias técnicas utilizadas no pré-processamento de imagens:

* ``Redimensionar``: Redimensionar imagens a um tamanho uniforme é importante para que os algoritmos de aprendizado de máquina funcionem corretamente. Podemos usar o método ``resize()`` do OpenCV para redimensionar a imagem.

* ``Grayscaling``: Converter imagens coloridas em escala de cinze pode simplificar seus dados de imagem e reduzir as necessidades computacionais de alguns algoritmos. O método `cvtColor()` pode ser usado para converter RGB em escala de cinza.

* `Redução de ruído`: técnicas de suavização, desfoque e filtragem podem ser aplicadas para remover ruídos indesejados das imagens. Os métodos ``GaussianBlur()`` e ``medianBlur()`` são comumente usados para isso.

* `Normalização`: A normalização ajusta os valores de intensidade dos pixels para um intervalo desejado, muitas vezes entre 0 e 1. Isso pode melhorar o desempenho dos modelos de machine learning. `Normalize()`, scikit-image pode ser utilizado para isso.

* ``Binarização``: A binarização converte imagens em tons de cinza em preto e branco por limiar. O método de `threshold()` é usado para binarizar imagens no OpenCV.

* `Melhoria de contraste`: O contraste de imagens pode ser ajustado usando a equalização do histograma. O método ``equalizeHist()`` aumenta o contraste de imagens.


Com a combinação certa dessas técnicas, você pode melhorar significativamente seus dados de imagem e criar melhores aplicativos de visão computacional. O pré-processamento de imagens permite refinar imagens brutas em um formato adequado para o problema.

## Aplicando filtros para reduzir ruído e afiar imagens

* ``O desfoque Gaussiano``: O filtro de desfoque gaussiano reduz detalhes e ruído em uma imagem. Ele "borra" a imagem aplicando uma função gaussiana a cada pixel e seus pixels vircundantes. Isso pode ajudar a suavizar bordas e detalhes em preparação para detecção de borda ou outras técnicas de processamento.

* `Desfoque médio`: O filtro de desfoque mediano é útil para remover o ruído de sal e pimenta de uma imagem. Ele funciona substituindo cada pixel pelo valor médio e seus pixels vizinhos. Isso pode ajudar a suavizar os pixels ruidosos isolados, preservando as bordas.

* `Filtro Laplaciano`: O filtro Laplaciano é usado para detectar bordas em uma imagem. Ele funciona detectando áreas de mudança de intensidade rápida. A saída será uma imagem com arestas destacadas, que pode ser usada para detecção de borda. Isso ajuda a identificar e extrair recursos de uma imagem.

* `Unsharp Masking`: É uma técnica usada para aguçar detalhes e melhorar as bordas em uma imagem. Ele funciona subtraindo uma versao desfocada da imagem original. Isso amplifica as bordas e detalhes, fazendo com que a imagem pareça mais nítida. O mascaramento desfiado pode ser usado para afiar detalhes antes da extração de recursos ou da detecção de objetos.

* `Bilateral Filter`: O filtro bilateral suaviza as imagens enquanto preserva as bordas. Ele faz isso considerando tanto a proximidade espacial quanto a semelhança de cores de pixel. Pixels que estão próximos espacialmente e de cor semelhante são suavizados juntos. Pixels que são distantes ou muito diferentes em cores não são suavizados. Isso resulta em uma imagem suavizada com bordas afiadas. O filtro bilateral pode ser útil para a redução de ruído antes da detecção de borda.

### Sistema da Visão Computacional

![sistema_VC](https://github.com/Vicrrs/opencv-experiments/assets/87845548/fd8313a9-b656-45be-8926-dae00cd5ca1c)

* Aquisição: captação da imagem, simular os olhos, humanos, dispositivos responsáveis por compor esse papel são os scanners, filmadora e câmera.

* Processamento: melhorar a imagem

* Segmentação: Particionar a imagem em regiões de interesse.

* Análise da imagem: encontrar uma condição numérica que representa parte da imagem.

* Reconhecimento de padrão: Classificar ou agrupar as imagens com base em um conjunto de características.



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
