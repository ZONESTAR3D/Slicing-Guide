### :globe_with_meridians: Choose Language (Translated by google)
[![](../lanpic/ES.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl)
[![](../lanpic/FR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl)
[![](../lanpic/PT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl)
[![](../lanpic/DE.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl)
[![](../lanpic/IT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=it&_x_tr_hl)
[![](../lanpic/PL.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=pl&_x_tr_hl)
[![](../lanpic/RU.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl)
[![](../lanpic/BR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl)
[![](../lanpic/GR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=el&_x_tr_hl)

[![](../lanpic/JP.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl)
[![](../lanpic/KR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=ko&_x_tr_hl)
[![](../lanpic/ID.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl)
[![](../lanpic/TH.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=th&_x_tr_hl)
[![](../lanpic/VN.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=vi&_x_tr_hl)
[![](../lanpic/IL.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=iw&_x_tr_hl)
[![](../lanpic/SA.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=ar&_x_tr_hl)
[![](../lanpic/TR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=tr&_x_tr_hl)
[![](../lanpic/CN.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4?_x_tr_sl=en&_x_tr_tl=zh-CN&_x_tr_hl)

-----
## :warning: Attention Please, this guide is for M4 hot end :warning:
### **Please pay attention to distinguish the hot end type: M4 hot end or E4 hot end**. 
If your printer has a M4 hot end, but you used a gcode file sliced by M4 hot end, it may cause block the hot end, vice versa. For default, Z9M4, Z8PM4 and Z9V5-MK1/MK2/MK3 equiped with a M4 hotend, Z9V5-MK4 equiped with a E4 hotend. You can apply the same slice settings and the gcode file to all version of M4 hot end.
- **M4 hot end:** 4-IN-1-OUT **mix color** hot end.    
- **E4 hot end:** 4-IN-1-OUT **non-mix color** hot end.    

-----
## Slicing muti-color for M4 hotend 
***Take Z9V5Pro with M4 hotend as an example***
:movie_camera:[**Video Tutorial**](https://youtu.be/_Ww2RFGlLNA)
### Step 1: choose printer presets "Z9 + M4 hotend"
![](pic/slicingM4-1.png)
### Step 2: load 3d model files (stl/obj/AMF file etc.)
![](pic/loadstl_1.png) ![](pic/loadstl_2.png)
- :memo: Usually, "split model" is inneed to print multi colors 3d model files, that is, a 3d model has been split into multiple STL files according to colors, and these files use the same origin coordinate position so that they can be merged correctly.
- :star2: PrusaSlicer has a powerful new feature, it can paint a 3d model file into multi colors, for details, please refer to :movie_camera:[**video tutorial**](https://youtu.be/C0a3Uble8rY).
### Step 3: Choose filament type and set filament color
![](pic/filament_color.png)
### Step 4: Assign extruders to different parts
![](pic/assign_extruder.png)
### Step 5: Resize, cut, rotate, move the 3d model if need 
![](pic/slicing_adjust.png)  
### Step 6: Set the print settings 
#### :warning: Please note that the "Retraction when tool is disabled" should be set to 0.    
![](pic/switch_length.jpg)  
#### set layer height, print speed, support, infill, etc.
![](pic/slicing_set.png)  
You need to set these parameters according to the shape of the model and your requirements for print quality. Even for some models, printing cannot be completed normally without support. For details please refer to:
- :point_right: [**PrusaSlicer introduction**](https://help.prusa3d.com/article/general-info_1910)      
- :point_right: [**Slic3r User Manuual**](https://manual.slic3r.org/)      
  
### Step 7: Set parameters for "wipe tower"
You may notice that a square will appear in the sliced figure, which is called "Wipe tower" in PrusaSlicer. Because for the multi-color printer, while switching extruders, there are still the previous color filaments inside the hotend, it need to be clean before printing another color.   
![](pic/wipe_tower.png)        
In order to obtain better cleaning effect and minimize to waste filament, we can set the purging volume according to different colors. Please see the following table, the columns shows the previous extruder and the rows shows the next extruder to be printed. When we change from the extruder with lighter color filament to the extruder with darker color filaments, we can set a smaller "purging volume". On the contrary, when we change from the extruder with darker color filaments to the extruder with lighter color filament, we need to set a bigger "purging volume".  
![](pic/slicingM4-2.png)  
### Step 8: Slicing
![](pic/slicing_go.png)  
### Step 9: Preview the sliced result (gcode file) and then save to gcode file to your PC and then copy to SD card
![](pic/slicing_save.png)  

-----
## How to print more than 4 colors using M4 hot end
M4 color mixing hot end can mix 2 ~ 4 actual extruders filament to produce a new color filament, and this new color filament can be used as a new extruder (called **"virtual extruder"**), the operation steps are as follows:   
***Following example shows how to set 6 extruders - 4 actual extruders and 2 virtual extruders. E5 is mixed by 50% E1 and 50% E2, E6 is mixed by 50% E3 and 50% E4.***     
### Step 1: Add virtual extruders
![](pic/slicingM4_6c_1.png)  
:warning: We suggest to **save**<sup>1</sup> the settings to a **new profile**<sup>2</sup>.   

### Step 2: Set mix rate of the new "virtual" extruder
#### Add the mix rate set gcode commands to "Start Gcode". 
![](pic/slicingM4_6c_2.png)  
:warning: We suggest that these g-codes be placed at the front of the "Start G-code". 

#### The added code is as follows:
>
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
    ........... (Previous start gcode commands)
#### :memo: About M163 and M164 Gcode commands
>
    M163: Set a single mix factor for a mixing extruder, must be followed by M164 to normalize and commit them.
     S[index]   The channel (actual extruder) index to set
     P[float]   The mix value from (0~100.0)
     R   				Reset all mixing extruder settings to default

    M164: Normalize and commit the mix rate to a virtual extruder.
     S[index]   The virtual extruder to store
  
    Normalize:  The sum of the ratios of all actual extruders needs to be 100, if the sum is not 100, the printer will automatically scale the ratio to meet this requirement.

### Step 3: Assign the new virtual extruders to 3D model and slicing
Now you can assign 6 extruders to the 3D model, slicing process is exactly the same as the 4 extruders. 
:warning: Choose the **printer profile**<sup>1</sup> before slicing, and you can clicl the color block to set the **filament color**<sup>2</sup> of the new extruders.   
![](pic/slicingM4_6c_3.png)   

-----
## M4 hotend user guide
[:book: User guide](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/M4%20%204-IN-1-OUT%20Mixing%20Color%20Hotend)

--------
## Testing gcode files for M4 (4-IN-1-OUT mixing color) hotend
We have uploaded some testing gcode files, you can download and print them to test.   
:point_right: Click [**here**](./test_gcode/M4/readme.md) to download.
