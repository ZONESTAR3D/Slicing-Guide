## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4.md)
[![](../lanpic/ES.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-es.md)
[![](../lanpic/PT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-pt.md)
[![](../lanpic/FR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-fr.md)
[![](../lanpic/DE.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-de.md)
[![](../lanpic/IT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-it.md)
[![](../lanpic/RU.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-ru.md)
[![](../lanpic/JP.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-jp.md)
[![](../lanpic/KR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-kr.md)
<!-- [![](./lanpic/SA.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-ar.md) -->

----
## :warning: ATENÇÃO POR FAVOR :warning:
### Preste atenção para distinguir o tipo de hot end
Por favor, preste atenção para distinguir o tipo de hot end que você usou é **mix color (M4)** hot end ou **non mix color(E4)** hot end.    
<u>**Se você imprimir um arquivo gcode fatiado no hot end M4 com um hot end E4, ele poderá bloquear o hot end, vice-versa.**</u>    
Se você não sabe o que há de diferente entre o hotend E4 e M4, consulte [**aqui**][FAQ_M4E4].   

----
## Fatiamento multicolorido para hotend M4
#### :loudspeaker: Este manual toma Z9V5Pro-MK3 como exemplo
### :movie_camera: [**Tutorial em vídeo**](https://youtu.be/_Ww2RFGlLNA)
[![](https://img.youtube.com/vi/_Ww2RFGlLNA/0.jpg)](https://www.youtube.com/watch?v=_Ww2RFGlLNA)

### Etapa 1: escolha as predefinições da impressora "Z9 + M4 hotend"
![](./pic/slicingM4-1.png)
### Etapa 2: carregar arquivos de modelo 3D (arquivo stl/obj/AMF etc.)
![](./pic/loadstl_1.png) ![](./pic/loadstl_2.png)
- :memo: Normalmente, "modelo dividido" é necessário para imprimir arquivos de modelo 3D multicoloridos, ou seja, um modelo 3D foi dividido em vários arquivos STL de acordo com as cores, e esses arquivos usam a mesma posição de coordenadas de origem para que possam ser mesclado corretamente.
- :star2: PrusaSlicer tem um novo recurso poderoso, ele pode pintar um arquivo de modelo 3D em várias cores. Para obter detalhes, consulte :movie_camera: [**Guia de corte - Converta um arquivo 3D de uma cor em várias cores**](https://youtu.be/Yx4fKDRGEJ4).
##### [![](https://img.youtube.com/vi/Yx4fKDRGEJ4/0.jpg)](https://www.youtube.com/watch?v=Yx4fKDRGEJ4)

### Etapa 3: Escolha o tipo de filamento e defina a cor do filamento
![](./pic/filament_color.png)
### Etapa 4: Atribuir extrusoras a diferentes peças
![](./pic/assign_extruder.png)
### Etapa 5: Redimensione, corte, gire e mova o modelo 3D se necessário
![](./pic/slicing_adjust.png)
### Etapa 6: Definir as configurações de impressão
#### :warning: Observe que a opção "Retração quando a ferramenta está desabilitada" deve ser definida como 0.
![](./pic/switch_length.jpg)
#### definir altura da camada, velocidade de impressão, suporte, preenchimento, etc.
![](./pic/slicing_set.png)     
Você precisa definir esses parâmetros de acordo com o formato do modelo e seus requisitos de qualidade de impressão. Mesmo para alguns modelos, a impressão não pode ser concluída normalmente sem suporte. Para obter detalhes, consulte:
- :point_right: [**Introdução ao PrusaSlicer**](https://help.prusa3d.com/article/general-info_1910)
- :point_right: [**Manual do usuário Slic3r**](https://manual.slic3r.org/)
  
### Etapa 7: Definir parâmetros para "wipe tower"
Você pode notar que um quadrado aparecerá na figura fatiada, que é chamado de “Torre Wipe” no PrusaSlicer. Como para a impressora multicolorida, ao trocar de extrusora, ainda existem os filamentos de cores anteriores dentro do hotend, ela precisa ser limpa antes de imprimir outra cor.
###### ![](./pic/wipe_tower.png)
Para obter um melhor efeito de limpeza e minimizar o desperdício de filamento, podemos definir o volume de purga de acordo com cores diferentes. Consulte a tabela a seguir, as colunas mostram a extrusora anterior e as linhas mostram a próxima extrusora a ser impressa. Quando mudamos da extrusora com filamento de cor mais clara para a extrusora com filamentos de cor mais escura, podemos definir um “volume de purga” menor. Pelo contrário, quando passamos da extrusora com filamentos de cor mais escura para a extrusora com filamento de cor mais clara, precisamos definir um “volume de purga” maior.
###### ![](./pic/slicingM4-2.png)
### Etapa 8: Fatiar
![](./pic/slicing_go.png)
### Etapa 9: Visualize o resultado fatiado (arquivo gcode) e salve no arquivo gcode em seu PC e copie para o cartão SD
![](./pic/slicing_save.png)

----
## Como imprimir mais de 4 cores usando hot end M4
O hot end de mistura de cores M4 pode misturar 2 ~ 4 filamentos de extrusoras reais para produzir um novo filamento de cor, e este novo filamento de cor pode ser usado como uma nova extrusora (chamada **"extrusora virtual"**), as etapas de operação são as seguintes :
***O exemplo a seguir mostra como configurar 6 extrusoras - 4 extrusoras reais e 2 extrusoras virtuais. E5 é misturado com 50% de E1 e 50% de E2, E6 é misturado com 50% de E3 e 50% de E4.***
### Etapa 1: Adicionar extrusoras virtuais
![](./pic/slicingM4_6c_1.png)
:warning: Sugerimos **salvar**<sup>1</sup> as configurações em um **novo perfil**<sup>2</sup>.

### Etapa 2: Definir taxa de mixagem da nova "extrusora virtual"
#### Adicione comandos "Definir taxa de mixagem" em "Iniciar Gcode".
![](./pic/slicingM4_6c_2.png)     
:warning: Sugerimos que esses códigos G sejam colocados na frente do "Código G inicial".
>
     ;Definir taxa de mixagem
     ;E5 = 50%E1 + 50%E2
     M163 S0 P50
     M163 S1 P50
     M163 S2 P0
     M163 S3 P0
     M164 S4
     ;E6 = 50%E3 + 50%E4
     M163 S0 P0
     M163 S1 P0
     M163 S2 P50
     M163 S3 P50
     M164 S5

#### :memo: Introdução aos comandos "M163" e "M164"
>
     M163: Defina um único fator de mistura para uma extrusora de mistura, deve ser seguido por M164 para normalizá-los e confirmá-los.
      S[index] O índice do canal (extrusora real) a ser definido
      P[float] O valor da mixagem de (0,0 ~ 100,0)
      R Redefinir todas as configurações da extrusora de mistura para o padrão

     M164: Normalize e confirme a taxa de mixagem para uma extrusora virtual.
      S[index] A extrusora virtual para armazenar
  
     Normalizar: Dimensione automaticamente os valores da proporção de mistura de cada extrusora para atender aos requisitos da máquina

### Etapa 3: Atribuir as novas extrusoras virtuais ao modelo 3D e fatiar
Agora você pode atribuir 6 extrusoras ao modelo 3D, o processo de fatiamento é exatamente igual ao das 4 extrusoras.
1. Escolha o perfil da impressora.
2. Defina a cor do filamento das novas extrusoras.
3. Atribua extrusora para a peça do modelo 3D.     
###### ![](./pic/slicingM4_6c_3.png)

----
## Apêndice
### [:book: guia de uso do hotend M4](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/M4)
### [:book: Guia de uso do recurso de mistura de cores](https://github.com/ZONESTAR3D/Document-and-User-Guide/tree/master/Mixing_Color)
### [:arrow_down:Teste arquivos gcode para hot end M4](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/M4/readme.md)


----
[FAQ_M4E4]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/FAQ_M4E4.md