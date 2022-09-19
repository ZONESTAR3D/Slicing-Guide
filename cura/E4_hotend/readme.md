## Slicing guide for E4 hotend with Cura Slicer
Use Z9 with E4 hotend as an exmple, Z8 with E4 is the same.
### Prepare
- **Add printer** 
![](./E4_hotend/E4_1.gif)
- **Take a look the 'machine Start/End gcode' and 'exturder Start/End gcode'** 
![](./E4_hotend/E4_2.gif)
For details about the ***machine Start/End gcode***  and ***exturder Start/End gcode***, please refer :point_down:[here](#about-start-and-end-gcode)

-----------
### About start and end gcode
> Start gcode of the "Z9(Z8) with E4 hotend"

    M220 S100 ;Reset Feedrate
    M221 S100 ;Reset Flowrate

    G28 ;Home
    G21
    G90
    G1 Z5 F600
    G1 X5 Y10 F1500
    G1 Z0.3 F600
    ;===Pre-load filament start
    T0
    G92 E0
    G1 E20 F120
    G0  X5 Y50 F1200
    G1 Y250 E35
    G0  X5.5
    G1 Y50 E50
    G0  X6
    G1 Y250 E65
    G0  X6.5
    G1 Y50 E80
    G0  X7
    G1 Y250 E95
    G0  X7.5
    G1 Y50 E110
    G0  X8
    G92 E0
    G1 E-80 F3000
    G92 E0
    T1
    G92 E0
    G1 E20 F120
    G0  X8 Y50 F1200
    G1 Y250 E35
    G0  X8.5
    G1 Y50 E50
    G0  X9
    G1 Y250 E65
    G0  X9.5
    G1 Y50 E80
    G0 X10
    G1 Y250 E95
    G0 X10.5
    G1 Y50 E110
    G0 X11
    G92 E0
    G1 E-80 F3000
    G92 E0
    T2
    G92 E0
    G1 E20 F120
    G0 X11 Y50 F1200
    G1 Y250 E35
    G0 X11.5
    G1 Y50 E50
    G0 X12
    G1 Y250 E65
    G0 X12.5
    G1 Y50 E80
    G0 X13
    G1 Y250 E95
    G0 X13.5
    G1 Y50 E110
    G0 X14
    G92 E0
    G1 E-80 F3000
    G92 E0
    T3
    G92 E0
    G1 E20 F120
    G0 X14 Y50 F1200
    G1 Y250 E35
    G0 X14.5
    G1 Y50 E50
    G0 X15
    G1 Y250 E65
    G0 X15.5
    G1 Y50 E80
    G0 X16
    G1 Y250 E95
    G0 X16.5
    G1 Y50 E110
    G0 X17
    G0 Y155 F4800
    G92 E0
    G1 E-80 F3000
    G92 E0
    ;===Pre-load filament end
> End gcode of the "Z9(Z8) with E4 hotend"

> Exturder Start gcode of E4 hotend

> Exturder End gcode of E4 hotend

##### We have set the 
<!-- - :movie_camera: [**slicing 4 colors 3d object (Z9 + E4 hotend)**](https://youtu.be/hP6Socp-Cz0)     -->