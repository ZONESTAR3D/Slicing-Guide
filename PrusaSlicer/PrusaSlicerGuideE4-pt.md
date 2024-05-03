[FAQ_M4E4]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/FAQ_M4E4.md
[TOOLCHANGE_GCODE]: https://github.com/ZONESTAR3D/Slicing-Guide/blob/master/PrusaSlicer/Custom_Gcode.md#tool-change-g-code
[E4_USERGUIDE]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/E4/User_guide
[E4_GCODE]: https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/E4/readme.md

----
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme.md)
[![](../lanpic/ES.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-es.md)
[![](../lanpic/PT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-pt.md)
[![](../lanpic/FR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-fr.md)
[![](../lanpic/DE.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-de.md)
[![](../lanpic/IT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-it.md)
[![](../lanpic/RU.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-ru.md)
[![](../lanpic/JP.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-jp.md)
[![](../lanpic/KR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-kr.md)
<!-- [![](./lanpic/SA.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-ar.md) -->

----
## :warning: ATENÇÃO POR FAVOR :warning:
### Por favor, preste atenção para distinguir o tipo de hot end: hot end M4 ou hot end E4.
Por favor, preste atenção para distinguir o tipo de hot end que você usou é **mix color (M4)** hot end ou **non mix color(E4)** hot end.    
<u>**Se você imprimir um arquivo gcode fatiado no hot end M4 com um hot end E4, ele poderá bloquear o hot end, vice-versa.**</u>    
Se você não sabe o que há de diferente entre o hotend E4 e M4, consulte [aqui][FAQ_M4E4].   

----
## Fatiamento multicolorido para hotend E4
***Tome Z9V5Pro-MK4 como exemplo***
##### :movie_camera: [Tutorial em vídeo](https://youtu.be/aets9JZ92iU)
[![](https://img.youtube.com/vi/aets9JZ92iU/0.jpg)](https://www.youtube.com/watch?v=aets9JZ92iU)
### Etapa 1, escolha as predefinições da impressora "Z9 + E4 hotend"
![](pic/slicingE4-1.png)
### Etapa 2: carregar arquivos de modelo 3D (arquivo stl/obj/AMF etc.)
![](pic/loadstl_1.png) ![](pic/loadstl_2.png)
- :memo: Normalmente, "modelo dividido" é necessário para imprimir arquivos de modelo 3D multicoloridos, ou seja, um modelo 3D foi dividido em vários arquivos STL de acordo com as cores, e esses arquivos usam a mesma posição de coordenadas de origem para que possam ser mesclado corretamente.
- :star2: PrusaSlicer tem um novo recurso poderoso, ele pode pintar um arquivo de modelo 3D em várias cores, para obter detalhes, consulte:movie_camera: [**Guia de corte - Converta um arquivo 3D de uma cor em várias cores**](https://youtu.be/Yx4fKDRGEJ4)
##### [![](https://img.youtube.com/vi/Yx4fKDRGEJ4/0.jpg)](https://www.youtube.com/watch?v=Yx4fKDRGEJ4)
### Etapa 3: Escolha o tipo de filamento e defina a cor do filamento
![](pic/filament_color.png)
### Etapa 4: Atribuir extrusoras a diferentes peças
![](pic/assign_extruder.png)
### Etapa 5: Redimensione, corte, gire e mova o modelo 3D se necessário
![](pic/slicing_adjust.png)
### Etapa 6: Definir as configurações de impressão
#### Definir "Retração" e "Retração quando a ferramenta está desabilitada"
Por favor, distinga entre 2 tipos de ***"Retração"***:
1. A ***"Retração"*** usual refere-se à impressão de linhas finas da mesma cor, quando a impressora se move de um ponto a outro, as linhas finas são puxadas um pouco para trás para reduzir o escoamento das linhas finas bocal de rosca. :warning: ***"Comprimento de retração"*** deve ser menor que 10mm para E4 Hot end.
2. ***"Retração quando a ferramenta está desativada"*** refere-se ao processo de puxar o fio fino para fora da extremidade quente quando a impressora muda de um fio fino para outro. :warning: ***"Retração quando a ferramenta está desabilitada"*** deve ser definido como 0 porque adicionamos ***"Personalizar códigos G"*** em ***"Alterar código G da ferramenta"*** para lidar de forma mais eficaz com o processo de troca de filamentos. Para obter mais detalhes, consulte [**tool-change-gcode**][TOOLCHANGE_GCODE].     
![](pic/slicingE4-4.jpg)

#### Defina a altura da camada, velocidade de impressão, suporte, preenchimento, etc.
![](pic/slicing_set.png)
Você precisa definir esses parâmetros de acordo com o formato do modelo e seus requisitos de qualidade de impressão. Mesmo para alguns modelos, a impressão não pode ser concluída normalmente sem suporte. Para obter detalhes, consulte:
- :point_right: [**Introdução ao PrusaSlicer**](https://help.prusa3d.com/article/general-info_1910)
- :point_right: [**Manual do usuário Slic3r**](https://manual.slic3r.org/)

### Etapa 7: Definir parâmetros para *wipe tower*
Você pode notar que um quadrado aparecerá na figura fatiada, que é chamado de “Torre Wipe” no PrusaSlicer. Como para a impressora multicolorida, ao trocar de extrusora, ainda existem os filamentos de cores anteriores dentro do hotend, ela precisa ser limpa antes de imprimir outra cor.    
![](pic/wipe_tower.png)     
Para obter um melhor efeito de limpeza e minimizar o desperdício de filamento, podemos definir o volume de purga de acordo com cores diferentes. Consulte a tabela a seguir, as colunas mostram a extrusora anterior e as linhas mostram a próxima extrusora a ser impressa. Quando mudamos da extrusora com filamento de cor mais clara para a extrusora com filamentos de cor mais escura, podemos definir um “volume de purga” menor. Pelo contrário, quando passamos da extrusora com filamentos de cor mais escura para a extrusora com filamento de cor mais escura, precisamos definir um “volume de purga” maior.    
:book: ***O comprimento de retração deve ser inferior a 10 mm, caso contrário pode levar ao bloqueio do hotend.***    
:star: Para o hotend E4, restam poucos filamentos no hotend, então podemos usar um volume de purga menor na torre de limpeza.    
![](pic/slicingE4-2.png)   
### Etapa 8: Fatiar
![](pic/slicing_go.png)
### Etapa 9: Visualize o resultado fatiado (arquivo gcode) e salve no arquivo gcode em seu PC e copie para o cartão SD
![](pic/slicing_save.png)    
:star: Ao visualizar o arquivo gcode, você pode ver que algumas linhas de impressão adicionais aparecerão na lateral da cama, que são para pré-carregar os filamentos. Para obter detalhes sobre como pré-carregar o filamento, consulte [**:book: E4 Hotend user guide**][E4_USERGUIDE].   
![](pic/slicingE4-3.png)   

----
## Apêndice
### Introdução do código G personalizado
Se você instalou corretamente o arquivo de perfis da impressora 3D ZONESTAR, verá que adicionamos alguns códigos gcode em ***"Configuração da impressora>>Código G personalizado"***.
Para obter detalhes sobre o "Código G personalizado", consulte [:book: **Descrição do Gcódigo personalizado**](./Custom_Gcode.md)     
![](./pic/Custom_Gcode.jpg)   
### [:book: Guia de uso do hot end E4][E4_USERGUIDE]
### [:arrow_down: Testar arquivos gcode para hot end E4][E4_GCODE]