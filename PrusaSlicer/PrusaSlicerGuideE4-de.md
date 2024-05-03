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
## :warning: ACHTUNG BITTE :warning:
### Bitte achten Sie auf die Unterscheidung des Hot-End-Typs: M4-Hot-End oder E4-Hot-End.
Bitte achten Sie darauf, den von Ihnen verwendeten Hot-End-Typ zu unterscheiden: **Mischfarbe (M4)** Hot-End oder **Nicht-Mischfarbe (E4)** Hot-End.    
<u>**Wenn Sie eine Gcode-Datei drucken, die auf einem M4-Hot-End mit einem E4-Hot-End aufgeteilt ist, kann es sein, dass das Hot-End blockiert wird, und umgekehrt.**</u>   
Wenn Sie nicht wissen, was der Unterschied zwischen E4- und M4-Hotend ist, lesen Sie bitte [hier][FAQ_M4E4].

-----
## Mehrfarbiges Schneiden für E4-Hotend
***Nehmen Sie Z9V5Pro-MK4 als Beispiel***
##### :movie_camera: [**Video-Tutorial**](https://youtu.be/aets9JZ92iU)
[![](https://img.youtube.com/vi/aets9JZ92iU/0.jpg)](https://www.youtube.com/watch?v=aets9JZ92iU)
### Schritt 1: Wählen Sie die Druckervoreinstellungen „Z9 + E4 Hotend“
![](pic/slicingE4-1.png)
### Schritt 2: 3D-Modelldateien laden (stl/obj/AMF-Datei usw.)   
![](pic/loadstl_1.png) ![](pic/loadstl_2.png)     
- :memo: Normalerweise ist „Modell aufteilen“ erforderlich, um mehrfarbige 3D-Modelldateien zu drucken, d korrekt zusammengeführt werden.
- :star2: PrusaSlicer verfügt über eine leistungsstarke neue Funktion: Es kann eine 3D-Modelldatei in mehrere Farben malen. Weitere Informationen finden Sie unter:movie_camera: [**Slicing-Anleitung – Konvertieren Sie eine 3D-Datei mit einer Farbe in mehrere Farben**](https://youtu.be/Yx4fKDRGEJ4)
##### [![](https://img.youtube.com/vi/Yx4fKDRGEJ4/0.jpg)](https://www.youtube.com/watch?v=Yx4fKDRGEJ4)
### Schritt 3: Filamenttyp auswählen und Filamentfarbe festlegen
![](pic/filament_color.png)
### Schritt 4: Extruder verschiedenen Teilen zuordnen
![](pic/assign_extruder.png)
### Schritt 5: Ändern Sie die Größe, schneiden Sie das 3D-Modell aus, drehen Sie es und verschieben Sie es bei Bedarf
![](pic/slicing_adjust.png)
### Schritt 6: Legen Sie die Druckeinstellungen fest
#### Stellen Sie „Rückzug“ und „Rückzug bei deaktiviertem Werkzeug“ ein.
Bitte unterscheiden Sie zwischen 2 Arten von ***„Rückzügen“***:
1. Der übliche ***„Rückzug“*** bezieht sich auf das Drucken feiner Fäden derselben Farbe. Wenn sich der Drucker von einem Punkt zum anderen bewegt, werden die feinen Fäden etwas zurückgezogen, um den Ausfluss der feinen Fäden zu verringern Fadendüse. :warning: ***Die „Rückzugslänge“*** sollte für das E4-Hot-End weniger als 10 mm betragen.
2. ***„Rückzug bei deaktiviertem Werkzeug“*** bezieht sich auf den Vorgang des Herausziehens des feinen Drahts aus dem heißen Ende, wenn der Drucker von einem feinen Draht auf einen anderen umschaltet. :warning: ***„Rückzug bei deaktiviertem Werkzeug“*** sollte auf 0 gesetzt werden, da wir ***„G-Codes anpassen“*** im ***„Werkzeugwechsel-Gcode“*** hinzugefügt haben den Prozess des Filamentwechsels effektiver bewältigen. Weitere Einzelheiten finden Sie unter [**tool-change-gcode**][TOOLCHANGE_GCODE].    
![](pic/slicingE4-4.jpg)   

#### Legen Sie Schichthöhe, Druckgeschwindigkeit, Unterstützung, Füllung usw. fest.
![](pic/slicing_set.png)     
Sie müssen diese Parameter entsprechend der Form des Modells und Ihren Anforderungen an die Druckqualität einstellen. Selbst bei einigen Modellen kann der Druckvorgang ohne Unterstützung nicht normal durchgeführt werden. Einzelheiten finden Sie unter:
- :point_right: [**PrusaSlicer-Einführung**](https://help.prusa3d.com/article/general-info_1910)
- :point_right: [**Slic3r-Benutzerhandbuch**](https://manual.slic3r.org/)

### Schritt 7: Parameter für *Wischturm* festlegen
Möglicherweise stellen Sie fest, dass in der geschnittenen Figur ein Quadrat erscheint, das in PrusaSlicer „Wipe Tower“ genannt wird. Da sich beim Mehrfarbendrucker beim Wechseln des Extruders immer noch die Filamente der vorherigen Farbe im Hotend befinden, muss dieses sauber sein, bevor eine andere Farbe gedruckt werden kann.    
![](pic/wipe_tower.png)   
Um eine bessere Reinigungswirkung zu erzielen und die Filamentverschwendung zu minimieren, können wir die Spülmenge je nach Farbe einstellen. Bitte sehen Sie sich die folgende Tabelle an. Die Spalten zeigen den vorherigen Extruder und die Zeilen zeigen den nächsten Extruder, der gedruckt werden soll. Wenn wir vom Extruder mit Filamenten in hellerer Farbe zum Extruder mit Filamenten in dunklerer Farbe wechseln, können wir ein kleineres „Spülvolumen“ einstellen. Im Gegenteil, wenn wir vom Extruder mit dunkleren Filamentfarben zum Extruder mit dunkleren Filamentfarben wechseln, müssen wir ein größeres „Spülvolumen“ einstellen.   
:warning: ***Die Rückzugslänge sollte weniger als 10 mm betragen, da es sonst zu einer Blockierung des Hotends kommen kann.***    
:star: Beim E4-Hotend sind nur noch wenige Filamente im heißen Ende übrig, sodass wir am Wischturm ein kleineres Spülvolumen verwenden können.   
![](pic/slicingE4-2.png)
### Schritt 8: Schneiden
![](pic/slicing_go.png)
### Schritt 9: Sehen Sie sich das Sliced-Ergebnis (Gcode-Datei) in der Vorschau an, speichern Sie es dann als Gcode-Datei auf Ihrem PC und kopieren Sie es dann auf die SD-Karte   
![](pic/slicing_save.png)    
:star: Bei der Vorschau der Gcode-Datei können Sie sehen, dass an der Seite des Bettes einige zusätzliche Drucklinien erscheinen, die zum Vorladen von Filamenten dienen. Ausführliche Informationen zum Vorladen des Filaments finden Sie im [**:book: E4 Hotend-Benutzerhandbuch**][E4_USERGUIDE].    
![](pic/slicingE4-3.png)

-----
## Anhang
### Einführung von G-Code anpassen
Wenn Sie die Profildatei des ZONESTAR 3D-Druckers korrekt installiert haben, werden Sie sehen, dass wir einige Gcode-Codes in ***„Druckereinstellungen>>Benutzerdefinierter G-Code“*** hinzugefügt haben.  
Einzelheiten zum „Benutzerdefinierten G-Code“ finden Sie unter [:book: **Beschreibung des benutzerdefinierten Gcode**](./Custom_Gcode.md)    
![](./pic/Custom_Gcode.jpg)
### [:book: E4-Hot-End-Gebrauchsanleitung][E4_USERGUIDE]
### [:arrow_down: Gcode-Dateien für E4-Hot-End testen][E4_GCODE]
