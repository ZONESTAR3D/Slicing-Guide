
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
#### :warning: Dieses Tool ist derzeit nur für ZONESTAR 4-Extruder-3D-Farbmischdrucker (M4) anwendbar.
## :arrow_down: Download 
### [Download (für Windows)](GradientMixToolV1.zip)
<!-- ### :arrow_down:[Download (for Linux)](GradientMixToolV1.zip) -->

----
## :book: Benutzerhandbuch
### Kurzbeschreibung
**Gradient Mix Tool** ist eine GCode-Nachbearbeitungssoftware, die entwickelt wurde, um das Mischungsverhältnis der Extruder in der Druckhöhe (Z-Achsenrichtung) automatisch anzupassen. Es kann für ZONESTAR-3D-Farbmischdrucker verwendet werden.
**Gradient Mix Tool** ermöglicht das Einrichten von bis zu 6 ***Gradientenprozessen***. Jeder Gradientenprozess kann auf eines der in der importierten GCode-Datei verwendeten VTools angewendet werden und den angewendeten Höhenbereich sowie das Start- und End-Extruder-Mischverhältnis festlegen. Es ist möglich, mehrere Prozesse gleichzeitig anzuwenden, wenn:
- Die Prozesse auf dasselbe VTool in unterschiedlichen Höhenbereichen angewendet werden.
**Oder:**
- Die Prozesse auf den verschiedenen VTools auf denselben Höhenbereich angewendet werden.

### Gebrauchsanweisung
#### 1. Laden Sie die Software herunter und entpacken Sie sie auf Ihren PC (nur eine EXE-Datei).
#### 2. Führen Sie GradientMixToolVx.exe aus.
![](1.jpg)
#### 3. Laden Sie eine Gcode-Datei.
Die Software formuliert die importierte Gcode-Datei automatisch, um die Höhe des Modells, die Schichtdicke, das verwendete VTool usw. abzurufen, und öffnet ein Eingabeaufforderungsfeld, um diese Informationen anzuzeigen.
![](2.jpg)
#### 4. Legen Sie die Parameter der „Prozesse“ fest.
![](3.jpg)
#### 5. Klicken Sie auf die Schaltfläche „Generieren“, um eine neue Gcode-Datei zu generieren.
Sie können sehen, welche Gcode-Befehle im Fenster ***Gcode-Ansicht exportieren*** hinzugefügt wurden
![](4.jpg)
#### 6. Klicken Sie auf die Schaltfläche „Exportieren“, um zu exportieren und in einer neuen Gcode-Datei zu speichern.
Als Nächstes können Sie die exportierte Gcode-Datei auf Ihrem ZONESTR Mix Color 3D-Drucker ausdrucken.

----
### Beispiele
#### Beispiel:one: [Spiral Vase :arrow_down:](./SpiralVase.zip)
Dieses Beispiel zeigt, wie man eine einfarbige Spiralvase-Gcode-Datei in eine Gcode-Datei mit mehreren Farbverläufen umwandelt:
- Bei 0~20 mm Höhe, Farbverlauf von Extruder 1 Farbe zu Extruder 2 Farbe.
- Bei 20~40 mm Höhe, Farbverlauf von Extruder 2 Farbe zu Extruder 3 Farbe.
- Bei 40~60 mm Höhe, Farbverlauf von Extruder 3 Farbe zu Extruder 4 Farbe.
- Bei einer Höhe von 60 bis 80 mm Farbverlauf von Farbe Extruder 4 zu Farbe Extruder 1.

- Bei einer Höhe über 80 mm Farbmischung von Extruder 1 und Extruder 2 bei etwa 50:50 halten.
![](./SpiralVase.jpg)
#### Beispiel:two: [M4_4C_test :arrow_down:](./M4_4C_test.zip)
Dieses Beispiel zeigt, wie man eine Gcode-Datei mit einem 4-farbigen Testmodell in eine Gcode-Datei mit Farbverläufen für jede Farbe umwandelt:
- Die Originalfarbe von Extruder 1 wird in eine Farbe umgewandelt, die von Extruder 1 zu Extruder 2 verläuft.
- Die Originalfarbe von Extruder 2 wird in eine Farbe umgewandelt, die von Extruder 2 zu Extruder 3 verläuft.
- Die Originalfarbe von Extruder 3 wird in eine Farbe umgewandelt, die von Extruder 3 zu Extruder 4 verläuft.
- Die Originalfarbe von Extruder 4 wird in eine Farbe umgewandelt, die von Extruder 4 zu Extruder 4 verläuft 1.
![](./M4-4C-Test.jpg)
