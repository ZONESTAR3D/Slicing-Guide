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
## Descargue e instale PrusaSlicer
### ![](./win.jpg) Para Windows:
##### ![][VIDEO_INSTALL]
   - Descargue PrusaSlicer desde el siguiente enlace y descomprímalo en su PC.
     - [:+1: :arrow_down: **Descargar PrusaSlicer V2.4.2**][PRUSASLICER_242] (Versión estable)
     - [:new: :arrow_down: **Descargar PrusaSlicer**][PRUSASLICER] (Todas las versiones lanzadas más recientes)

   ### ![](./macos.jpg) Para MacOS:
   :arrow_down: Descargue [**PrusaSlicer con archivo dmg de perfiles ZONESTAR**][PRUSASLICER_IMG] y luego instálelo en su PC.

   ### ![](./linux.jpg) Para Linux:
   :arrow_down: Descargue PrusaSlicer desde [**Prusa Github Page**][PRUSASLICER_RELEASE] y luego importe los perfiles de impresora 3D ZONESTAR más recientes.

#### Importar perfiles de impresora 3D ZONESTAR
- [**:arrow_down:Descargue los perfiles de la impresora 3D ZONESTAR**](./Profiles.zip) y descomprímalo en su PC.
- Copie los perfiles al directorio "recurso/perfiles" del directorio de instalación del software PrusaSlicer.
:advertencia:Es posible que deba eliminar las configuraciones anteriores; de lo contrario, los perfiles más nuevos no se podrán aplicar correctamente:advertencia:
Puede encontrar el directorio donde almacenar las configuraciones anteriores: ***ayuda>>Mostrar Floder de configuración***, para Windows, generalmente se almacena en ***"C:/Users/{nombre de su PC}/AppData/Roaming /PrusaSlicer[-alpha/beta]"***. Elimine todos estos archivos en este directorio y luego ejecute PrusaSlicer nuevamente.     
![0](./pic/0.png) ![1](./pic/1.png)

-----
## 2. Configurar la impresora
- 2.1 Busque prsua-slicer.exe y haga clic en él para ejecutarlo.    
![](pic/run1.png)
- 2.2 Elija su impresora, "Otros Proveedores>>Zonestar FFF>>su modelo de impresora>>terminar".    
![](pic/run2.png)

-----
## 3. Elija el valor preestablecido de la impresora
Elija la configuración preestablecida de la impresora según el modelo de su impresora, el tipo de hotend y los colores que desea imprimir.
![](pic/run3.png)
| Serie de impresoras | imprimir | Tipo de hotend | ajustes preestablecidos | Predeterminado para Máquina |
|:-------------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|
| Z5 | un color o 2 colores | Hotend M2 | Hotend Z5 + M2 | Z5M2 |
| Z5X | un color | hotend de un color | Z5X | Z5X |
| Z6 | un color | hotend de un color | Z6 | Z6 |
| Serie Z8 | un color | Cualquiera | Z8 + un color | / |
| Serie Z8 | un color | Extrusora de accionamiento directo | Z8 + DDE | / |
| Serie Z8 | multicolor | Hotend M3 | SALIENTE Z8 + M3 | Z8S-M3/Z8T/Z8PM3 |
| Serie Z8 | multicolor | Hotend M4 | SALIENTE Z8 + M4 | Z8PM4/Z8PM4Pro |
| Serie Z8 | multicolor | Hotend E4 | SALIENTE Z8 + E4 | / |
| Serie Z9 | un color | Cualquiera | Z9 + un color | / |
| Serie Z9 | un color | Extrusora de accionamiento directo | Z8 + DDE | / |
| Serie Z9 | multicolor | Hotend M3 | SALIENTE Z9 + M3 | Z9M3 |
| Serie Z9 | multicolor | Hotend M4 | SALIENTE Z9 + M4 | Z9M4/Z9V5Pro-MK1/2/3 |
| Serie Z9 | multicolor | Hotend M4 | CALIENTE Z9 + E4 | Z9V5Pro-MK4 |

(*)Predeterminado para Máquina: El tipo de hotend predeterminado utilizado por este modelo de impresora 3D.

-----
[PRUSASLICER_242]: https://github.com/ZONESTAR3D/Slicing-Guide/releases/tag/PrusaSlicer2.4.2
[PRUSASLICER_IMG]: https://github.com/ZONESTAR3D/Slicing-Guide/releases/tag/2.4.2
[PRUSASLICER]: https://github.com/ZONESTAR3D/Slicing-Guide/releases
[PRUSASLICER_RELEASE]: https://github.com/prusa3d/PrusaSlicer/releases
[VIDEO_INSTALL]: https://github.com/ZONESTAR3D/Slicing-Guide/assets/29502731/ce48a22c-a9aa-45e8-8544-c1c67c7cd021