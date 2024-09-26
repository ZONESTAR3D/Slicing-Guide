
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../../lanpic/EN.png)](./readme.md)
[![](../../lanpic/ES.png)](./readme-es.md)
[![](../../lanpic/PT.png)](./readme-pt.md)
[![](../../lanpic/FR.png)](./readme-fr.md)
[![](../../lanpic/DE.png)](./readme-de.md)
[![](../../lanpic/IT.png)](./readme-it.md)
[![](../../lanpic/RU.png)](./readme-ru.md)
[![](../../lanpic/JP.png)](./readme-jp.md)
[![](../../lanpic/KR.png)](./readme-kr.md)
[![](../../lanpic/SA.png)](./readme-ar.md)
[![](../../lanpic/CN.png)](./readme-cn.md)

----
# Gradient Mix Tool
#### :warning: Esta ferramenta é atualmente aplicável somente às impressoras 3D de mistura de cores ZONESTAR 4-extrusoras (M4).
## :arrow_down: Download 
### :arrow_down:[Download (para Windows)](./GradientMixToolV1.zip)
<!-- ### :arrow_down:[Download (for Linux)](GradientMixToolV1.zip) -->

----
## Guia do usuário
### Resumo
**Gradient Mix Tool** é um software de pós-processamento GCode, desenvolvido para ajustar automaticamente a taxa de mistura das extrusoras na altura da impressão (direção do eixo Z). Pode ser aplicado às impressoras 3D coloridas de mistura de cores ZONESTAR.
**Gradient Mix Tool** permite configurar até 6 ***Processos de gradiente***, cada processo de gradiente pode ser aplicado a uma das VTools usadas no arquivo GCode importado e definir o intervalo de altura aplicado e a taxa de mistura inicial e final da extrusora. É possível aplicar vários processos simultaneamente quando:
- Os processos são aplicados à mesma VTool em diferentes intervalos de altura.
**Ou:**
- Os processos são aplicados ao mesmo intervalo de altura nas diferentes VTools.
### Instruções de uso
#### 1. Baixe o software e descompacte-o no seu PC (apenas um arquivo exe).
#### 2. Execute GradientMixToolVx.exe.
![](1.jpg)
#### 3. Carregue um arquivo Gcode.
O software irá automaticamente frasear o arquivo Gcode importado para obter a altura do modelo, espessura da camada, VTool usado etc., e abrir uma caixa de prompt para mostrar essas informações.
![](2.jpg)
#### 4. Defina os parâmetros dos "processos".
![](3.jpg)
#### 5. Clique no botão Gerar para gerar um novo arquivo gcode.
Você pode ver quais comandos Gcode foram adicionados na janela ***exportar visualização Gcode***
![](4.jpg)
#### 6. Clique no botão Exportar para exportar e salvar em um novo arquivo gcode.
Em seguida, você pode imprimir o arquivo Gcode exportado na sua impressora 3D ZONESTR Mix Color.

----
### Exemplos
#### Exemplo:one: [Spiral Vase :arrow_down:](./SpiralVase.zip)
Este exemplo mostra como converter um arquivo Gcode de um vaso espiral de uma cor em um arquivo Gcode multi-gradiente:
- Na altura de 0~20 mm, gradiente da cor 1 da extrusora para a cor 2 da extrusora.
- Na altura de 20~40 mm, gradiente da cor 2 da extrusora para a cor 3 da extrusora.
- Na altura de 40~60 mm, gradiente da cor 3 da extrusora para a cor 4 da extrusora.
- Na altura de 60~80 mm, gradiente da cor 4 da extrusora para a cor 1 da extrusora.
- Acima de 80 mm de altura, mantenha a mistura de cores da extrusora 1 e da extrusora 2 em cerca de 50:50.
![](./SpiralVase.jpg)
#### Exemplo:two: [M4_4C_test :arrow_down:](./M4_4C_test.zip)
Este exemplo mostra como converter um arquivo Gcode de modelo de teste de 4 cores em um arquivo Gcode com gradientes para cada cor:
- A cor original da extrusora 1 é convertida em uma cor que gradiente da extrusora 1 para a extrusora 2.
- A cor original da extrusora 2 é convertida em uma cor que gradiente da extrusora 2 para a extrusora 3.
- A cor original da extrusora 3 é convertida em uma cor que gradiente da extrusora 3 para a extrusora 4.
- A cor original da extrusora 4 é convertida em uma cor que gradiente da extrusora 4 para a extrusora 1.
![](./M4-4C-Test.jpg)