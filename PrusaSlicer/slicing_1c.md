<!-- ### :globe_with_meridians: Choose Language (Translated by google)
[![](../lanpic/ES.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guid?_x_tr_sl=en&_x_tr_tl=es)
[![](../lanpic/PT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guid?_x_tr_sl=en&_x_tr_tl=pt)
[![](../lanpic/FR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=fr)
[![](../lanpic/DE.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=de)
[![](../lanpic/IT.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=it)
[![](../lanpic/SW.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=sv)
[![](../lanpic/PL.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=pl)
[![](../lanpic/DK.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=da)
[![](../lanpic/CZ.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=cs)
[![](../lanpic/HR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=hr)
[![](../lanpic/RO.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=ro)
[![](../lanpic/SK.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=sk)

[![](../lanpic/RU.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=ru)
[![](../lanpic/JP.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=ja)
[![](../lanpic/KR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=ko)
[![](../lanpic/ID.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=id)
[![](../lanpic/TH.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=th)
[![](../lanpic/VN.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=vi)
[![](../lanpic/IL.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=iw)
[![](../lanpic/SA.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=ar)
[![](../lanpic/TR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=tr)
[![](../lanpic/GR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=el)
[![](../lanpic/BR.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=pt)
[![](../lanpic/CN.png)](https://github-com.translate.goog/ZONESTAR3D/Slicing-Guide?_x_tr_sl=en&_x_tr_tl=zh-CN)

----- -->
## Single color 3d model slicing guide
***Take Z9V5pro as an example***  
:movie_camera:[**Video Tutorial**](https://youtu.be/6QU-jnycS8c)        
#### 1. **Choose printer presets "Z9 + One Color"**   
![](./pic/slicing1C-1.png)
#### 2. **load 3d model file (stl/obj/AMF file etc.)**    
![](./pic/slicing1C-2.png)
#### 3. **Choose filament type**   
![](./pic/slicing1C-3.png)
#### 4. **Resize, cut, rotate, move the 3d model if need**    
![](./pic/slicing1C-4.png)  
#### 5. **Set the print settings: layer height, print speed, support, infill, etc.**  
![](./pic/slicing1C-5.png)  
You may need to set these parameters according to the shape of the model and your requirements for print quality. For some models, the object even cannot be printed successfully if the settings is incorrect. For details please refer to:
  - :point_right: [**Print Settings**](https://help.prusa3d.com/category/print-settings_212)
  - :point_right: [**PrusaSlicer introduction**](https://help.prusa3d.com/article/general-info_1910)
#### 6. **Slicing**    
![](./pic/slicing1C-6.png)  
#### 7. **Preview the sliced result (gcode file) and then save the gcode file to your PC**     
![](./pic/slicing1C-7.png)  

-----
### :pushpin:Auto unload filament after printing finished  
If you were using the E4 hot end, we recommend that you add the following gcode commands to the "End G-code", to let the printer unload the filament from the hot end after printing finished.   
>
    ;pull out the filament 
    G92 E0
    G1 E-45 F1800
    G92 E0

![](./pic/slicing1C-8.png) 