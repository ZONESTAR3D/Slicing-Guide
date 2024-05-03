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
## :warning: ATTENTION PLEASE :warning:
### Please pay attention to distinguish the hot end type
Please pay attention to distinguish the hot end type what you used is **mix color (M4)** hot end or **non mix color(E4)** hot end. 
<u>**If you print a gcode file sliced on M4 hot end with an E4 hot end, it may block the hot end, vice versa.**</u>     
If you don't know what's different between E4 and M4 hotend, please refder to [**here**][FAQ_M4E4].  

----
## Slicing muti-color for M4 hotend 
#### :loudspeaker: This manual is took Z9V5Pro-MK3 as an example
### :movie_camera: [**Video Tutorial**](https://youtu.be/_Ww2RFGlLNA)
[![](https://img.youtube.com/vi/_Ww2RFGlLNA/0.jpg)](https://www.youtube.com/watch?v=_Ww2RFGlLNA)

### Step 1: choose printer presets "Z9 + M4 hotend"
![](./pic/slicingM4-1.png)
### Step 2: load 3d model files (stl/obj/AMF file etc.)
![](./pic/loadstl_1.png) ![](./pic/loadstl_2.png)
- :memo: Usually, "split model" is inneed to print multi colors 3d model files, that is, a 3d model has been split into multiple STL files according to colors, and these files use the same origin coordinate position so that they can be merged correctly.
- :star2: PrusaSlicer has a powerful new feature, it can paint a 3d model file into multi colors, for details, please refer to :movie_camera: [**Slicing guide - Convert one color 3d file to multi colors**](https://youtu.be/Yx4fKDRGEJ4). 
##### [![](https://img.youtube.com/vi/Yx4fKDRGEJ4/0.jpg)](https://www.youtube.com/watch?v=Yx4fKDRGEJ4)

### Step 3: Choose filament type and set filament color
![](./pic/filament_color.png)
### Step 4: Assign extruders to different parts
![](./pic/assign_extruder.png)
### Step 5: Resize, cut, rotate, move the 3d model if need 
![](./pic/slicing_adjust.png)  
### Step 6: Set the print settings 
#### :warning: Please note that the "Retraction when tool is disabled" should be set to 0.    
![](./pic/switch_length.jpg)  
#### set layer height, print speed, support, infill, etc.
![](./pic/slicing_set.png)  
You need to set these parameters according to the shape of the model and your requirements for print quality. Even for some models, printing cannot be completed normally without support. For details please refer to:
- :point_right: [**PrusaSlicer introduction**](https://help.prusa3d.com/article/general-info_1910)      
- :point_right: [**Slic3r User Manuual**](https://manual.slic3r.org/)      
  
### Step 7: Set parameters for "wipe tower"
You may notice that a square will appear in the sliced figure, which is called "Wipe tower" in PrusaSlicer. Because for the multi-color printer, while switching extruders, there are still the previous color filaments inside the hotend, it need to be clean before printing another color.   
###### ![](./pic/wipe_tower.png)        
In order to obtain better cleaning effect and minimize to waste filament, we can set the purging volume according to different colors. Please see the following table, the columns shows the previous extruder and the rows shows the next extruder to be printed. When we change from the extruder with lighter color filament to the extruder with darker color filaments, we can set a smaller "purging volume". On the contrary, when we change from the extruder with darker color filaments to the extruder with lighter color filament, we need to set a bigger "purging volume".  
###### ![](./pic/slicingM4-2.png)  
### Step 8: Slicing
![](./pic/slicing_go.png)  
### Step 9: Preview the sliced result (gcode file) and then save to gcode file to your PC and then copy to SD card
![](./pic/slicing_save.png)  

----
## How to print more than 4 colors using M4 hot end
M4 color mixing hot end can mix 2 ~ 4 actual extruders filament to produce a new color filament, and this new color filament can be used as a new extruder (called **"virtual extruder"**), the operation steps are as follows:   
***Following example shows how to set 6 extruders - 4 actual extruders and 2 virtual extruders. E5 is mixed by 50% E1 and 50% E2, E6 is mixed by 50% E3 and 50% E4.***     
### Step 1: Add virtual extruders
![](./pic/slicingM4_6c_1.png)  
:warning: We suggest to **save**<sup>1</sup> the settings to a **new profile**<sup>2</sup>.   

### Step 2: Set mix rate of the new "virtual extruder"
#### Add "Set mix rate" commands to "Start Gcode". 
![](./pic/slicingM4_6c_2.png)  
:warning: We suggest that these g-codes be placed at the front of the "Start G-code". 
>
    ;Set mix rate
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

#### :memo: Introduction to "M163" and "M164" commands
>
    M163: Set a single mix factor for a mixing extruder, must be followed by M164 to normalize and commit them.
     S[index]   The channel (actual extruder) index to set
     P[float]   The mix value from (0.0 ~ 100.0)
     R   		Reset all mixing extruder settings to default

    M164: Normalize and commit the mix rate to a virtual extruder.
     S[index]   The virtual extruder to store
  
    Normalize:  Automatically scale the mixing ratio values of each extruder to meet machine requirements

### Step 3: Assign the new virtual extruders to 3D model and slicing
Now you can assign 6 extruders to the 3D model, slicing process is exactly the same as the 4 extruders.       
1. Choose the printer profile.   
2. Set the filament color of the new extruders.   
3. Assign extruder for the part of the 3D model.    
![](./pic/slicingM4_6c_3.png)   

----
## Appendix
### [:book: M4 hotend use guide](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/M4)
### [:book: Mixing color feature use guide](https://github.com/ZONESTAR3D/Document-and-User-Guide/tree/master/Mixing_Color)
### [:arrow_down:Test gcode files for M4 hot end](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/M4/readme.md)


----
[FAQ_M4E4]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/FAQ_M4E4.md