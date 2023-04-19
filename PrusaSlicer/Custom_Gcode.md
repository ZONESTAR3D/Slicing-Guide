## Description of Custom G-code 
### Contents
- [**Start G-code**](#start-g-code)
- [**End G-code**](#end-g-code)
- [**Switch Extruder G-code**](#tool-change-g-code)

-----
### Start G-code
The "start G-code" can be divided into two parts. 
- **The first part** includes 10 commands wrote on the front. These commands are mainly to set the temperature, Home, raise the Z-axis.  
:warning:Please note that because PrusaSlicer MUST used "relative distances for extension" when slicing multi colors, (so a M83 commands MUST be added in the start-gcode"). Therefore, in the second part commands, the length of the extrusion is not cumulative. If you want to migrate these gcodes to other slicing software. Because other slicing software uses **absolute distances for extension** by default, you need to modify these commands.
- **The second part** is used to print 4 lines on the left side of the hot bed, to help confirm whether the filament has been correctly loaded to the hot end.:warning: The 2nd part are used for multi color printing only.     
>
    ;part 1
    M104 S[first_layer_temperature] ; set extruder temp
    M140 S[first_layer_bed_temperature] ; set bed temp
    M190 S[first_layer_bed_temperature] ; wait for bed temp
    M109 S[first_layer_temperature] ; wait for extruder temp
    G28 ; home all axes
    G21 ; set units to millimeters
    G90 ; use absolute coordinates
    M83 ; use relative distances for extrusion
    G1 Z5 F3000 ; lift nozzle
    G1 X5 Y10 F1500 ; move to prime start point
    G1 Z0.3 F3000 ; get ready to prime
    ;
    ;part 2 for multi color printing
    ;===Pre-load filament start
    ;M117 Preload Extruder #1
    T0
    G1 E20 F120
    G0 X5 Y50 F3000
    G1 Y250 E15 F1200
    G0 X5.5 F3000
    G1 Y50 E15 F1200
    G0 X6 F3000
    G1 Y250 E15 F1200
    G0 X6.5 F3000
    G1 Y50 E15 F1200
    G0 X7 F3000
    G1 Y250 E15 F1200
    G0 X7.5 F3000
    G1 Y50 E15 F1200
    G0 X8 F3000
    G1 E-80 F2400
    M400
    ;M117 Preload Extruder #2
    T1
    G1 E20 F120
    G0 X8 Y50 F3000
    G1 Y250 E15 F1200
    G0 X8.5 F3000
    G1 Y50 E15 F1200
    G0 X9 F3000
    G1 Y250 E15 F1200
    G0 X9.5 F3000
    G1 Y50 E15 F1200
    G0 X10 F3000
    G1 Y250 E15 F1200
    G0 X10.5 F3000
    G1 Y50 E15 F1200
    G0 X11 F3000
    G1 E-80 F2400
    M400
    ;M117 Preload Extruder #3
    T2
    G1 E20 F120
    G0 X11 Y50 F3000
    G1 Y250 E15 F1200
    G0 X11.5 F3000
    G1 Y50 E15 F1200
    G0 X12 F3000
    G1 Y250 E15 F1200
    G0 X12.5 F3000
    G1 Y50 E15 F600
    G0 X13 F3000
    G1 Y250 E15 F1200
    G0 X13.5 F3000
    G1 Y50 E15 F1200
    G0 X14 F3000
    G1 E-80 F2400
    M400
    ;M117 Preload Extruder #4
    T3
    G1 E20 F120
    G0 X14 Y50 F3000
    G1 Y250 E15 F1200
    G0 X14.5 F3000
    G1 Y50 E15 F1200
    G0 X15 F3000
    G1 Y250 E15 F1200
    G0 X15.5 F3000
    G1 Y50 E15 F1200
    G0 X16 F3000
    G1 Y250 E15 F1200
    G0 X16.5 F3000
    G1 Y50 E15 F1200
    G0 X17 F3000
    G0 Y155 F4800
    M300 S4000 P200
    G4 P100
    ;M300 S4000 P200
    ;===Pre-load filament end

### End G-code
The End G-code include “Homing hot end”, “Turn off heater, fan and motors” etc., these commands are common for all FDM 3d printers. And a "G1 E-45 F2100" command be added at the front to pull out the filament from the hot end after printing is finished.
>
    G92 E0
    G1 E-45 F2100 ;pull out filament from E4 hot end
    G28 XY
    M106 S0 ; turn off FAN
    M104 S0 ; turn off extruder
    M140 S0 ; turn off bed
    M84     ; disable motors

### Tool change G-code
Tool change also be called "switch extruder", which are some commands executed when switching extruder from one to another.    
For E4 hot end, when switching the extruder, we need to pull the last color filament from the hot end, and then push the next color filament into the hot end.    
The first three commands pull the filament from the hot end; Then a Tx command is to switch to the new extruder; The rest of commands are to push the next color filament into the hot end.  
You can appropriately increase or decrease the pull in length according to the type of filaments. In short, the longer the length is, the more time it takes to print, but the probability of hot end blockage will be reduced.
#### 1. Default "Tool change G-code"
The default **"Tool change G-code"** uses a 100mm pull-push length, it is applicable to most typs of filaments, especially those filaments added a lot of "tougheners" when produce, e.g. SILK-PLA. 
>
    ;Change extruder
    G92 E0
    G1 E-100 F3000;pull filament
    G92 E0
    T[next_extruder]
    G92 E0
    G1 E40 F2100; push filament-1
    G92 E0
    G1 E25 F1200; pushfilament-2
    G92 E0
    G1 E20 F1800; pushfilament-3
    G92 E0
    G1 E15 F600; push filament-4
    G92 E0

#### 2. 80mm pull-push length "Tool change G-code"
For PLA+ or ordinary PLA filament, you can shorten the pull-push length, "Tool change G-code" as below:
>
    ;Change extruder
    G92 E0
    G1 E-80 F3000;pull filament
    G92 E0
    T[next_extruder]
    G92 E0
    G1 E20 F2100; push filament-1
    G92 E0
    G1 E25 F1200; pushfilament-2
    G92 E0
    G1 E20 F1800; pushfilament-3
    G92 E0
    G1 E15 F600; push filament-4
    G92 E0

#### 3. 60mm pull-push length "Tool change G-code"
For ABS filament, you can further shorten the pull-push length, "Tool change G-code" as below:
>
    ;Change extruder
    G92 E0
    G1 E-60 F3000;pull filament
    G92 E0
    T[next_extruder]
    G92 E0
    G1 E25 F1200; pushfilament-1
    G92 E0
    G1 E20 F1800; pushfilament-2
    G92 E0
    G1 E15 F600; push filament-3
    G92 E0