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


## Detectando e Removendo Fundos Com Segmentação

* ``Thresholding``:  Thresholding converte uma imagem de tons de cinza em uma imagem binária (preto e branco) escolhendo um valor limite. Pixels mais escuros do que o limite tornam-se pretos, e pixels mais claros tornam-se brancos.  Isso funciona bem para imagens com alto contraste e iluminação uniforme. Você pode usar o método threshold() do OpenCV para aplicar o limite.

* ``Edge Detection``: A detecção de bordas encontra as bordas de objetos em uma imagem. Ao conectar bordas, você pode isolar o assunto em primeiro plano. O detector de borda Canny é um algoritmo popular implementado no método canny() do scikit-image. Ajuste os parâmetros low_threshold e high_threshold para detectar bordas.

* ``Region Growing``: O crescimento da região começa com um grupo de pontos de semente e cresce para fora para detectar regiões contíguas em uma imagem. Você fornece os pontos de semente e o algoritmo examina os pixels vizinhos para determinar se eles devem ser adicionados à região. Isso continua até que não haja mais pixels. O método skimage. segmentation. region_growing () implementa esta técnica.

* ``Watershed``: O algoritmo divisor de águas trata uma imagem como um mapa topográfico, com pixels de alta intensidade representando picos e vales representando fronteiras entre as regiões. Começa nos picos e inundações para baixo, criando barreiras quando diferentes regiões se encontram. O método skimage. segmentation. watershed() realiza segmentação por bacia hidrográfica.


## Usando Data Augmentation para expandir o conjunto de dados

O aumento de dados é uma técnica usada para expandir artificialmente o tamanho do seu conjunto de dados, gerando novas imagens a partir das existentes. Isso ajuda a reduzir o excesso de ajuste e melhora a generalização do seu modelo. Algumas técnicas de aumento comuns para dados de imagem incluem:

* ``Flipping and rotating``: Simplesmente inverter (horizontal ou verticalmente) ou girar (90, 180, 270 graus) imagens podem gerar novos pontos de dados. Por exemplo, se você tiver 1.000 imagens de gatos, invertida e girá-los pode dar 4.000 imagens totais (1.000 originais + 1.000 viradas horizontalmente + 1.000 viradas verticalmente + 1.000 giradas 90 graus).

* ``Cropping``: Cortar imagens para diferentes tamanhos e proporções cria novas imagens a partir do mesmo original. Isso expõe seu modelo a diferentes enquadramentos e composições do mesmo conteúdo. Você pode criar culturas aleatórias de tamanho variável ou segmentar proporções de culturas mais específicas, como quadrados.

* ``Color manipulation``: Ajustar o brilho, o contraste, a tonalidade e a saturação são maneiras fáceis de criar novas imagens aumentadas. Por exemplo, você pode ajustar aleatoriamente o brilho e o contraste de imagens em até 30% para gerar novos pontos de dados. Tenha cuidado para não distorcer muito as imagens, ou você corre o risco de confundir seu modelo.

* ``Image overlays``: Sobrepor imagens transparentes, texturas ou ruído em imagens existentes é outra técnica de aumento simples. Adicionar coisas como marcas d'água, logotipos, sujeira / arranha-louque ou ruído gaussiano pode criar variações realistas de seus dados originais. Comece com sobreposições sutis e veja como seu modelo responde.

* ``Combining techniques``: Para o maior aumento de dados, você pode combinar várias técnicas de aumento nas mesmas imagens. Por exemplo, você pode virar, girar, cortar e ajustar a cor das imagens, gerando muitos novos pontos de dados a partir de uma única imagem original. Mas tenha cuidado para não aumentar demais, ou você corre o risco de distorcer as imagens além do reconhecimento!


## Escolhendo as etapas de pré-processamento certas para sua aplicação


Escolher as técnicas corretas de pré-processamento para o seu projeto de análise de imagem depende de seus dados e objetivos. Alguns passos comuns incluem:

* ``Resizing``: O redimensionamento de imagens para um tamanho consistente é importante para que os algoritmos de aprendizado de máquina funcionem corretamente. Você vai querer que todas as suas imagens sejam da mesma altura e largura, geralmente um tamanho pequeno como 28x28 ou 64x64 pixels. O método redimensionar() nas bibliotecas OpenCV ou Pillow torna isso fácil de fazer programaticamente.

* ``Color conversion``: A conversão de imagens em tons de cinza ou em preto e branco pode simplificar sua análise e reduzir o ruído. O método cvtColor() no OpenCV converte imagens de RGB para escala de cinza. Para preto e branco, use limiaring.

* ``Noise reduction``: Técnicas como desfoque de Gaussian, desfocagem mediana e filtragem bilateral podem reduzir o ruído e suas imagens suaves. Os métodos GaussianBlur() e bilateral GaussianBlur() da OpenCV aplicam esses filtros.
A normalização
Normalizar os valores de pixels para uma faixa padrão, como 0 a 1 ou -1 a 1, ajuda os algoritmos a funcionar melhor. Você pode normalizar imagens com o método normalize() em imagem scikit.

* ``Contrast enhancement``: Para imagens de baixo contraste, a equalização de histograma melhora o contraste. O método equalizeHist() no OpenCV executa essa tarefa

* ``Edge detection``: Encontrar as bordas ou contornos em uma imagem é útil para muitas tarefas de visão computacional. O detector de borda Canny no método Canny() do OpenCV é uma escolha popular.

## Técnicas de Pré-processamento de imagens FAQs

Agora que você tem uma boa compreensão das várias técnicas de pré-processamento de imagens em Python, você provavelmente tem algumas perguntas persistentes. Aqui estão algumas das perguntas mais frequentes sobre pré-processamento de imagens e suas respostas:

### Quais formatos de imagem o Python é compatível?
O Python suporta uma ampla gama de formatos de imagem através de bibliotecas como OpenCV e Pillow.
Alguns dos principais formatos incluem:
* JPEG — Formato de imagem comum e com perdas
* PNG — Formato de imagem sem perdas bom para imagens com transparência
* TIFF — Formato de imagem sem perdas bom para imagens de alta profundidade de cor
* BMP — Formato de imagem raster sem compressão

### Quando devo redimensionar uma imagem?
Você deve redimensionar uma imagem quando:
* A imagem é muito grande para processar de forma eficiente. Reduzir o tamanho pode acelerar o processamento.
* A imagem precisa corresponder ao tamanho da entrada de um modelo de aprendizado de máquina.
* A imagem precisa ser exibida pn uma tela ou página da Web em um tamanho específico.

### Quais são algumas técnicas comuns de redução de ruído?
Algumas técnicas populares de redução de ruído incluem:
* Desfoque gaussiano — Usa um filtro gaussiano para desfocar a imagem e reduzir o ruído de alta frequência.
* Median Blur — Substitui cada pixel pela mediana dos pixels vizinhos. Eficaz na remoção de sal e pimenta.
* Filtro bilateral — Imagens de desfoque enquanto preserva as bordas. Ele pode remover o ruído enquanto mantém bordas afiadas.


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
