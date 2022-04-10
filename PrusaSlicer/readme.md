## PrusaSlicer software
#### Version: 2.4.0-rc+win64 for windows7/10/11 
#### [> Download](https://downgit.github.io/#/home?url=https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicer-2.4.0-rc%2Bwin64)
   
#### After downloaded, unzip it to your PC, and then click "prusa-slicer" to start.
![](picture\0.png)

>  
A copy of PrusaSlicer software for win7/win10/win11, ZONESTAR 3d printer profiles has already added.
You can also download the PrusaSlicer software from here: 
[**https://github.com/prusa3d/PrusaSlicer/releases**](https://github.com/prusa3d/PrusaSlicer/releases)

## PrusaSlicer Profiles for ZONESTAR 3D Printers
#### [> Download](https://downgit.github.io/#/home?url=https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/Profiles)   
#### This directoy is Profiles for ZONESTAR 3D printer of PrusaSlicer, if your PrusaSilcer software doesn't download from Prusa3d github page or website, please download this profiles and copy to “\resources\profiles” folder which PrusaSlicer software installed.
![](picture\1.png)
#### If you have installed PrusaSlicer before, you may still need to delete previous configurations settings before apply this Profiles.
1. You can find the directory by open the PrusaSlicer menu: **help>>Show Configuration Floder**, for Windows OS, it is usually stored in "C:/Users/{your PC name}/AppData/Roaming/PrusaSlicer", as below shown:
2. Delete all of the files in this directory, and then open PrusaSlicer software again.
![1](picture\2.png)

## PrusaSlicer Settings
### 1. Configuration>>Configuration Wizard>>Next
![](picture\settings1.png)
### 2. Other Vendor>>ZONESTAR>>Next
![](picture\settings2.png)
### 3. Choose machine model>>Next
![](picture\settings3.png)
### 4. Choose printer model, filament(s) & print settings
![](picture\settings4.png)  
- **printer model** For orignal Z9V5Pro, please choose Z9+M4 HOTEND.  
- **filament** Choose filament you used.     
- **print settings** If you slicing one color 3d files, choose "SingelExtruder 0.2mm". If you slicing multi-color 3d files, choose "MultiExtruder 0.2mm".  


## PrusaSlicer Slicing
### PrusaSlicer User guide 
- **[PrusaSlicer introduction](https://www.prusa3d.com/page/prusaslicer_424/)**
- **PrusaSlcier is base on Slic3d, so you can also refer to [Slic3r User Manuual](https://manual.slic3r.org/)**

### 1. load stl files
![](picture\slicing1.png)
### 2. Auto add prime tower
![](picture\slicing2.png)
### 3. Amazing new features: Painting the 3d model to multi color
![](picture\slicing3.png)
### 4. Set purging volume
##### To add the “loaded purge value” of light-color filament can prevent being polluted by filaments of other colors.
![](picture\slicing4.png)
![](picture\slicing5.png)
![](picture\slicing6.png)
![](picture\slicing7.png)
##### For example, suppose that the filaments color of extruder  you use is E1: White / E2: Red / E3: Green/ E4: Blue，because white is easy to be polluted:   
- set to ***200mm*** from E2/E3/E4 to E1
![](picture\slicing8.png) 
- Set to ***30mm*** from E1 to E2/E3/E4  
![](picture\slicing9.png)
##### Other parameters are set according to similar principles too. 






   
