## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install.md)
[![](../lanpic/ES.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-es.md)
[![](../lanpic/PT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-pt.md)
[![](../lanpic/FR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-fr.md)
[![](../lanpic/DE.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-de.md)
[![](../lanpic/IT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-it.md)
[![](../lanpic/RU.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-ru.md)
[![](../lanpic/JP.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-jp.md)
[![](../lanpic/KR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-kr.md)
<!-- [![](./lanpic/SA.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-ar.md) -->

----
## Baixe e instale o PrusaSlicer
### ![](./win.jpg) Para Windows:
##### ![][VIDEO_INTSTALL]
   - Baixe o PrusaSlicer no link abaixo e descompacte no seu PC.
     - [:+1: :arrow_down:**Baixar PrusaSlicer V2.4.2**][PRUSASLICER_242] (versão estável)
     - [:new: :arrow_down:**Baixar PrusaSlicer**][PRUSASLICER] (todas as versões mais recentes lançadas)

   ### ![](./macos.jpg) Para MacOS:
   :arrow_down: Baixe [**PrusaSlicer com arquivo dmg de perfis ZONESTAR**][PRUSASLICER_IMG] e instale em seu PC.

   ### ![](./linux.jpg) Para Linux:
   :arrow_down: Baixe o PrusaSlicer da [**Página do Prusa no Github**][PRUSASLICER_RELEASE] e, em seguida, importe os perfis de impressora 3D ZONESTAR mais recentes.

#### Importar perfis de impressora 3D ZONESTAR
- [**:arrow_down:Baixar perfis de impressora 3D ZONESTAR**](./Profiles.zip) e descompacte-o em seu PC.
- Copie os perfis para o diretório "resource/profiles" do diretório de instalação do software PrusaSlicer.    
:warning: Você pode precisar excluir configurações anteriores, caso contrário, os perfis mais recentes não poderão ser aplicados corretamente :warning:     
Você pode encontrar o diretório onde armazena as configurações anteriores: ***Help>>Show Configuration Floder***, para Windows, geralmente é armazenado em ***"C:/Users/{nome do seu PC}/AppData/Roaming /PrusaSlicer[-alfa/beta]"***. Exclua todos esses arquivos neste diretório e execute o PrusaSlicer novamente.    
![0](./pic/0.png) ![1](./pic/1.png)

-----
## 2. Configurar impressora
- 2.1 Encontre o prsua-slicer.exe e clique nele para executar.    
![](pic/run1.png)
- 2.2 Escolha sua impressora, "Outros Fornecedores>>Zonestar FFF>>modelo de sua impressora>>acabamento".   
![](pic/run2.png)

-----
## 3. Escolha a predefinição da impressora
Escolha a predefinição da impressora de acordo com o modelo da impressora, tipo de hotend e cores que deseja imprimir.
![](pic/run3.png)
| Série de impressoras | imprimir | Tipo de hotend | predefinições | Padrão para Máquina |
|:-------------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|
| Z5 | uma cor ou 2 cores | Hotend M2 | Hotend Z5 + M2 | Z5M2 |
| Z5X | uma cor | hotend de uma cor | Z5X | Z5X |
| Z6 | uma cor | hotend de uma cor | Z6 | Z6 |
| Série Z8 | uma cor | Qualquer | Z8 + uma cor | / |
| Série Z8 | uma cor | Extrusora de acionamento direto | Z8 + DDE | / |
| Série Z8 | multicolorido | Hotend M3 | Z8 + M3 HOTENDA | Z8S-M3/Z8T/Z8PM3 |
| Série Z8 | multicolorido | Hotend M4 | Z8 + M4 HOTEND | Z8PM4/Z8PM4Pro |
| Série Z8 | multicolorido | Hotend E4 | Z8 + E4 HOTEND | / |
| Série Z9 | uma cor | Qualquer | Z9 + uma cor | / |
| Série Z9 | uma cor | Extrusora de acionamento direto | Z8 + DDE | / |
| Série Z9 | multicolorido | Hotend M3 | Z9 + M3 HOTEND | Z9M3 |
| Série Z9 | multicolorido | Hotend M4 | Z9 + M4 HOTEND | Z9M4/Z9V5Pro-MK1/2/3 |
| Série Z9 | multicolorido | Hotend M4 | Z9 + E4 HOTEND | Z9V5Pro-MK4 |

(*) Padrão para Máquina: O tipo de hotend padrão usado por este modelo de impressora 3D.

-----
[PRUSASLICER_242]: https://github.com/ZONESTAR3D/Slicing-Guide/releases/tag/PrusaSlicer2.4.2
[PRUSASLICER_IMG]: https://github.com/ZONESTAR3D/Slicing-Guide/releases/tag/2.4.2
[PRUSASLICER]: https://github.com/ZONESTAR3D/Slicing-Guide/releases
[PRUSASLICER_RELEASE]: https://github.com/prusa3d/PrusaSlicer/releases
[VIDEO_INTSTALL]: https://github.com/ZONESTAR3D/Slicing-Guide/assets/29502731/ce48a22c-a9aa-45e8-8544-c1c67c7cd021