### Language / Translate
[![](../lanpic/ES.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=es)
[![](../lanpic/PT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=pt)
[![](../lanpic/FR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=fr)
[![](../lanpic/RU.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=ru)
[![](../lanpic/IT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=it)
[![](../lanpic/DE.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=de)
[![](../lanpic/PL.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=pl)
[![](../lanpic/KR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=ko)
[![](../lanpic/JP.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=ja)
[![](../lanpic/SA.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=ar)
[![](../lanpic/CN.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide/tree/master/cura?_x_tr_sl=en&_x_tr_tl=zh-CN)

--------

## Install Cura and import ZONESTAR 3d printer profiles 
:green_book: [**What is resources files**](https://github.com/Ultimaker/Cura/wiki/Definition-Files-Explained)  :green_book: [**Cura user guide**](https://support.ultimaker.com/hc/en-us/categories/360002327600-Software)  

### Following the below steps to install cura and then import the ZONESTAR 3d printer profiles:  
- **Step 1**:  :arrow_down: Download and install  [**Cura software**](https://github.com/Ultimaker/Cura/releases)
- **Step 2**:  :arrow_down: Download [**Zonestar 3D Printer Profiles.**](./ZONESTAR_Cura_resources.zip) *<-click here and then click "download" button to download, the last updata on 2022-08-15.*.   
![](downloadzip.gif)  
- **Step 3**:   Unzip ***ZONESTAR_Cura_Resource.zip*** to your PC and then copy the "resource" files to the cura installation directory.    
:warning: For **Cura 5.x.x**, resource files store in ***"{Cura installed directory}\share\cura\resource"(e.g.:C:\Program Files\Ultimaker Cura 5.1.0\share\cura\resource)***         
:warning: For **Cura 4.x.x**, resource files store in ***"{Cura installed directory}\resource"(e.g.:C:\Program Files\Ultimaker Cura 4.13.1\resource)***   
![](ImportProfiles.gif)       
- **Step 4**: Run cura, you can find the Zonestar printers in the list while you choose "add mechine" in cura.    
![](machinelist.gif)
### You need to choose different printer model on Cura when you slicing one color or multi-colors 3d models, please refer to the below table:
|   Printer model  |Orignal Hotend Type| Print one color | Print multi colors |  
|------------------|-------------------|-----------------|--------------------|
|      Z6          |    one color      |       Z6        |        NA          | 
|      Z5X         |    one color      |       Z5X       |        NA          | 
|      Z5XM2       |    M2 hotend      |       Z5X       | Z10 with M2 hotend | 
|    Z8X/Z10S      |    one color      |  Z8 one color   |        NA          |
|    Z8XM2/Z10M2   |    M2 hotend      |  Z8 one color   | Z10 with M2 hotend |
|      Z8S         |    M3 hotend      |  Z8 one color   | Z10 with M2 hotend |
|      Z8T         |    M3 hotend      |  Z8 one color   | Z8 with M3 hotend  |
|      Z8PM3       |    M3 hotend      |  Z8 one color   | Z8 with M3 hotend  |
|      Z8PM4       |    M4 hotend      |  Z8 one color   | Z8 with M4 hotend  |
|      Z9M2        |    M2 hotend      |  Z9 one color   | Z9 with M2 hotend  |
|      Z9M3        |    M3 hotend      |  Z9 one color   | Z9 with M3 hotend  |
|      Z9M4        |    M4 hotend      |  Z9 one color   | Z9 with M4 hotend  |
|      Z9E4        |    E4 hotend      |  Z9 one color   | Z9 with E4 hotend  | 
| Z9V5-MK1/MK2/MK3 |    M4 hotend      |  Z9 one color   | Z9 with M4 hotend  | 
|   Z9V5-MK4       |    E4 hotend      |  Z9 one color   | Z9 with E4 hotend  | 

##### About hotend type
- [**M2 hotend:**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND#m2-2-in-1-out--mixing-color-hotend) 2-IN-1-OUT mixing color hotend    
- [**M3 hotend:**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND#m2-2-in-1-out--mixing-color-hotend) 3-IN-1-OUT mixing color hotend    
- [**M4 hotend:**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND#m44-in-1-out-mixing-color-hotend) 4-IN-1-OUT mixing color hotend    
- [**E4 hotend:**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND#e4-4-in-1-out-non-mix-color-hotend) 4-IN-1-OUT non-mixing color hotend    
For more information of the hotend, please refer to [**here**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND).

   


### Slicing Guide and video tutorial for ZONESTAR 3D Printer
<!-- - :movie_camera: [**Install and setup Cura 5.1.x**]()    -->
- :movie_camera: [**Install and setup Cura 4.x.x**](https://youtu.be/h2GynyUo7wQ)   
- :movie_camera: [**slicing 1 color 3d object (Z9V5 + M4 hotend)**](https://youtu.be/UDgjGRFrELc)   
- :movie_camera: [**slicing 4 colors 3d object (Z9V5 + M4 hotend)**](https://youtu.be/hP6Socp-Cz0)    
- :movie_camera: [**slicing 8 colors 3d object (Z9V5 + M4 hotend)**](https://youtu.be/qQ6UnTysqK0)  

------------
### Test gcode files
Example gcode and stl files.  
:point_right: [***More examples for M4(4-IN-1-OUT mix color) hotend***](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/M4%20%204-IN-1-OUT%20Mixing%20Color%20Hotend)  
:point_right: [***More examples for E4((4-IN-1-OUT non-mix color)) hotend***](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/E4%204-IN-1-OUT%20Non-Mixing%20Color%20Hotend)  
#### Settings for R3 hotend 
User guide for Cura slicing process of R3 hotend   
More hotend user guide, please refer to :point_right: [***More hotend user guide***](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND)  
