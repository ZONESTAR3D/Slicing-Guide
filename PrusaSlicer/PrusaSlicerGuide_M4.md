## :warning: Attention Please :warning:
#### :exclamation:Please pay attention to distinguish the hot end type you used is M4 (a mix color hot end) hot end or E4 (a Non-mix color) hot end. If your printer has a M4 hot end, but you used a gcode file sliced by M4 hot end, it may cause block the hot end, vice versa. :exclamation:
For default, Z9M4, Z8PM4 and Z9V5-MK1/MK2/MK3 equiped with a M4 hotend, **Z9V5-MK4 equiped with a E4 hotend**.    
No matter which version of the M4 hot end, you can apply the same slice settings and the gcode file.    

--------
## Slicing muti-color for M4 hotend 
***Take Z9V5Pro with M4 hotend as an example***
:movie_camera:[**Video Tutorial**](https://youtu.be/_Ww2RFGlLNA)
### Step 1: choose printer presets "Z9 + M4 hotend"
![](pic/slicingM4-1.png)
### Step 2: load 3d model files (stl/obj/AMF file etc.)
![](pic/slicingM4-2.png) ![](pic/slicingM4-21.png)
- :memo: Usually, "split model" is inneed to print multi colors 3d model files, that is, a 3d model has been split into multiple STL files according to colors, and these files use the same origin coordinate position so that they can be merged correctly.
- :star2: PrusaSlicer has a powerful new feature, it can paint a 3d model file into multi colors, for details, please refer to :movie_camera:[**video tutorial**](https://youtu.be/C0a3Uble8rY).
### Step 3: Choose print filament type - PLA and set filament color
![](pic/slicingM4-3.png)
### Step 4: Assign extruders to different parts
![](pic/slicingM4-4.png)
### Step 5: Resize, cut, rotate, move the 3d model if need 
![](pic/slicingM4-5.png)  
### Step 6: Set the print settings: layer height, print speed, support, infill, etc.
![](pic/slicingM4-6.png)  
You need to set these parameters according to the shape of the model and your requirements for print quality. Even for some models, printing cannot be completed normally without support. For details please refer to:
- :point_right: [**PrusaSlicer introduction**](https://help.prusa3d.com/article/general-info_1910)
- :point_right: [**Slic3r User Manuual**](https://manual.slic3r.org/)
### Step 7: Set parameters for "wipe tower"
##### You may notice that a square square will appear in the sliced figure, which is called "Wipe tower" in PrusaSlicer. Because for the multi-color printer, while switching extruders, there are still the previous color filaments inside the hotend, it need to be clean before printing another color.   
![](pic/slicingM4-71.png)    
##### In order to obtain better cleaning effect and minimize to waste filament, we can set the amount of color purge according to different colors. Please pay attention to the following table, the columns shows the filament color of the last extruder printed, and the rows shows the filament color of the next extruder to be printed.
##### When we change from the extruder with lighter color filament to the extruder with darker color filaments, we can set a smaller extrusion erasure. On the contrary, when we change from the extruder with darker color filaments to the extruder with darker color filament, we need to set a smaller extrusion erasure
![](pic/slicingM4-72.png)  
### Step 8: Slicing
![](pic/slicingM4-8.png)  
### Step 9: Preview the sliced result (gcode file) and then save to gcode file to your PC and then copy to SD card
![](pic/slicingM4-9.png)  

-----
### M4 hotend user guide
[:book: User guide](https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4%20%204-IN-1-OUT%20Mixing%20Color%20Hotend)

--------
### Testing gcode files for M4 (4-IN-1-OUT mixing color) hotend
We have uploaded some testing gcode files, you can download and print them to test.   
:point_right: Click [**here**](./test_gcode/M4/readme.md) to download.
