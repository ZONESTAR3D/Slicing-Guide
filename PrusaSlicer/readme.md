### Language / Translate
[![](../lanpic/ES.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=es)
[![](../lanpic/PT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=pt)
[![](../lanpic/FR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=fr)
[![](../lanpic/RU.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=ru)
[![](../lanpic/IT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=it)
[![](../lanpic/DE.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=de)
[![](../lanpic/PL.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=pl)
[![](../lanpic/KR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=ko)
[![](../lanpic/JP.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=ja)
[![](../lanpic/SA.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=ar)
[![](../lanpic/CN.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer?_x_tr_sl=en&_x_tr_tl=zh-CN)

--------
## :warning: Attention Please :warning:
### :exclamation:Please pay attention to distinguish the hot end type what you used is M4 (mix color hot end) hot end or E4 (Non-mix color) hot end. If your printer has a M4 hot end, but you used a gcode file sliced by M4 hot end, it may cause block the hot end, vice versa. :exclamation:
--------
## :book: Contents
- [**Download software**](#1-download-prusaslicer-software-and-profiles)
- [**Setup printer**](#2-setup-printer)
- [**Set print preset**](#3-set-print-preset)
- [**Slicing one Color**](#4-slicing-one-color)
- [**Slicing muti-color for M4 hotend**](#5-slicing-muti-color-for-m4-hotend)
- [**Slicing muti-color for E4 hotend**](#6-slicing-muti-color-for-e4-hotend)
--------
## 1. Download PrusaSlicer software and profiles
#### :point_right: [PrusaSlicer introduction](https://help.prusa3d.com/article/general-info_1910)

#### For Windows
- :arrow_down: [**Download PrusaSlicer 2.4.2 with ZONESTAR 3D Printer Profiles**](https://github.com/ZONESTAR3D/Slicing-Guide/releases)     
Download it and unzip it to your PC or laptop, and then find and run the "PrusaSlicer.exe".    

#### For Macos or linux
- :arrow_down: [**Download PrusaSlicer software**](https://github.com/prusa3d/PrusaSlicer/releases)
- :arrow_down: [**Download profiles**](https://downgit.github.io/#/home?url=https:%2F%2Fgithub.com%2FZONESTAR3D%2FSlicing-Guide%2Ftree%2Fmaster%2FPrusaSlicer%2FProfiles)
- Copy Profiles to "resource/profiles" directory of the installation directory of the PrusaSlicer software.

#### If you have installed PrusaSlicer before, you may still need to delete previous configurations settings before apply this Profiles
##### You can find the directory by open the PrusaSlicer menu: **help>>Show Configuration Floder**, for Windows OS, it is usually stored in "C:/Users/{your PC name}/AppData/Roaming/PrusaSlicer", as below shown:
##### Delete all of the files in this directory, and then open PrusaSlicer software again.
![0](./pic/0.png)![1](./pic/1.png)

## 2. Setup printer
#### 2.1 Find the PrsuaSlicer.exe and click it to run
![](pic/run1.png)
#### 2.2 Choose your printer, "Other Vendors>>Zonestar FFF>>your printer model>>finish"
![](pic/run2.png)

## 3. Set print preset
Choose system presets according to your printer, hotend and the colors you want to print. 
#### 3.2 Printer model: Z9V5Pro and Z9M4
- If you print one color, choose "Z9 + One Color"  
- If your printer has a M4 (4-IN-1-OUT mixing color) hotend and print multi-color, choose "Z9 + M4 HOTEND"  
- If your printer has a E4 (4-IN-1-OUT Non-mixing color) hotend and print multi-color, choose "Z9 + E4 HOTEND"  
- If you printer has a Direct Drive Extruder, choose “Z9 + DDE”  
#### 3.2 Printer model: Z9M3 
- If you print one color, choose "Z9 + One Color"  
- If you print multi-color, choose "Z9 + M3 HOTEND"  
- If your printer has M4 (4-IN-1-OUT mixing Color) HOTEND, choose “Z9 + M4 HOTEND“ 
- If your printer has E4 (4-IN-1-OUT Non-mixing Color) HOTEND, choose “Z9 + E4 HOTEND“ 
- If your printer has a Direct Drive Extruder, choose “Z9 + DDE”  
#### 3.3 Printer model: Z8S-M3/Z8T-M3/Z8P-M3/Z8P-M4
  - If you print one color, choose "Z8 + One Color"  
  - If your printer has a M3 hotend and print multi-color, choose "Z8 + M3 HOTEND"  
  - If your printer has a M4 hotend and print multi-color, choose "Z8 + M4 HOTEND"  
  - If your printer has a E4 (4-IN-1-OUT Non-mixing Color) HOTEND, choose “Z9 + E4 HOTEND“    
  - If your printer has a Direct Drive Extruder, choose “Z8 + DDE” 
#### 3.4 Printer model: Z5S-M2/D805S-M2, choose "Z5 + M2 HOTEND"  
#### 3.5 Printer model: Z5X/Z6, , choose "Zonestar Z5X" or "Zonestar Z6"
![](pic/run3.png)

## 4. Slicing one color
***Take Z9V5pro with M4 hotend as an example***
:movie_camera:[**Video Tutorial**](https://www.youtu.be/6QU-jnycS8c)  
#### 4.1 choose printer presets "Z9 + One Color"
![](pic/slicing1C-1.png)
#### 4.2 load 3d model file (stl/obj/AMF file etc.)
![](pic/slicing1C-2.png)
#### 4.3 Choose print filament type
![](pic/slicing1C-3.png)
#### 4.4 Resize, cut, rotate, move the 3d model if need
![](pic/slicing1C-4.png)  
#### 4.5 Set the print settings: layer height, print speed, support, infill, etc.
![](pic/slicing1C-5.png)  
You may need to set these parameters according to the shape of the model and your requirements for print quality. For some models, the object even cannot be printed successfully if the settings is incorrect. For details please refer to:
- :point_right: [**Print Settings**](https://help.prusa3d.com/category/print-settings_212)
- :point_right: [**PrusaSlicer introduction**](https://help.prusa3d.com/article/general-info_1910)
#### 4.6 Slicing
![](pic/slicing1C-6.png)  
#### 4.7 Preview the sliced result (gcode file) and then save to gcode file to your PC and then copy to SD card
![](pic/slicing1C-7.png)  


## 5. Slicing muti-color for M4 hotend  
##### [:book: User guide](./PrusaSlicerGuide_M4.md)
##### :movie_camera:[Video Tutorial](https://youtu.be/_Ww2RFGlLNA)    
##### :arrow_down: [Test gcode files](./test_gcode/M4/readme.md)

## 6. Slicing muti-color for E4 hotend
##### [:book: User guide](./PrusaSlicerGuide_E4.md)
##### :movie_camera:[Video Tutorial](https://youtu.be/aets9JZ92iU)   
##### :arrow_down: [Test gcode files](./test_gcode/E4/readme.md)