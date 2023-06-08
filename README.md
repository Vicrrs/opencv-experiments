# opencv-experiments
Transferring to the repository an updated version of the experiments I performed with opencv

# Introdução

Trabalhando com imagens.

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
