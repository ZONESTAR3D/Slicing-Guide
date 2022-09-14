# Color switching Tower Genaration
# This script is specific for the ZONESTAR M3 and M4 3d printer 
# It runs with the PostProcessingPlugin which is released under the terms of the AGPLv3 or higher.
# This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms

# Authors of the Color switching Tower Genaration plug-in / script:
# Written by Hally.Zhong - hally@zonestar3d.com

#history / change-log:
#V1.1.0 - released
#
#V1.0.1 - Initial

import re
from ..Script import Script

class ColorSwitchTower_V1_1_0(Script):
    def __init__(self):
        super().__init__()
        
    def getSettingDataString(self):
        return """{
            "name": "ZONESTAR Color Switch Tower Genaration V1.1.0",
            "key": "ColorSwitchTowerV110",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "pattern_type":
                {
                    "label": "Pattern",
                    "description": "Pattern Type is line or square",
                    "type": "enum",
                    "options": {
                        "line":"Line",
                        "square":"Square"
                    },
                    "default_value": "line"
                },
                "line_width":
                {
                    "label": "Line width",
                    "description": "= line width of tower, recommended value is between 1 and 1.3 times of the nozzle size",
                    "type": "float",
                    "unit": "mm",
                    "default_value": 0.4,
                    "minimum_value": 0.2,
                    "maximum_value": 0.8
                },
                "used_color_number":
                {
                    "label": "Used color number",
                    "description": "The number of colors used when printing, between 3 ~ 8",
                    "type": "int",
                    "default_value": 3,
                    "maximum_value": 8
                },
                "tower_start_x":
                {
                    "label": "x of the tower",
                    "description": "Value to start position at X axis (mm), between 5 ~ 500",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 150,
                    "minimum_value": 5,
                    "maximum_value": 500
                },
                "tower_start_y":
                {
                    "label": "y of the tower",
                    "description": "Value to start position at Y axis (mm), between 5 ~ 500",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 250,
                    "minimum_value": 5,
                    "maximum_value": 500
                },
                "tower_length":
                {
                    "label": "Tower Length",
                    "description": "Value to the length (at X axis) of the tower (mm), between 20 ~ 100",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 60,
                    "minimum_value": 20,
                    "maximum_value": 100
                },
                "flow_length":
                {
                    "label": "Flow length",
                    "description": "Need to be extruded filament length when switch to a new color (mm), between 10 ~ 100",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 50,
                    "minimum_value": 10,
                    "maximum_value": 100
                },
                "print_speed":
                {
                    "label": "Print speed",
                    "description": "printing speed of the tower, recommended value between 30 ~ 60",
                    "type": "int",
                    "unit": "mm/s",
                    "default_value": 50,
                    "minimum_value": 10,
                    "maximum_value": 100
                },
                "speed_firstlayer":
                {
                    "label": "First layer speed",
                    "description": "printing speed of the tower on the first layer, percent of the print speed",
                    "type": "int",
                    "unit": "%",
                    "default_value": 60,
                    "minimum_value": 50,
                    "maximum_value": 100
                },
                "retraction_length":
                {
                    "label": "Retraction length",
                    "description": "Value to retract length when go to or leave the tower(mm), between 5 ~ 20",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 10,
                    "minimum_value": 5,
                    "maximum_value": 20   
                },
                "retraction_speed":
                {
                    "label": "Retraction speed",
                    "description": "Value to retracte speed when go to or leave the tower(mm/s), between 15 ~ 40",
                    "type": "int",
                    "unit": "mm/s",
                    "default_value": 25,
                    "minimum_value": 15,
                    "maximum_value": 40
                },
                "recover_length":
                {
                    "label": "Recover length",
                    "description": "Value to recover length after retraction (mm), between 0 ~ 1.0",
                    "type": "float",
                    "unit": "mm",
                    "default_value": 0.1,
                    "minimum_value": 0.0,
                    "maximum_value": 1.0   
                },
                "recover_speed":
                {
                    "label": "Recover speed",
                    "description": "Value to recover speed (mm/s), between 15 ~ 40",
                    "type": "int",
                    "unit": "mm/s",
                    "default_value": 20,
                    "minimum_value": 15,
                    "maximum_value": 40
                },
                "zhop_heigth":
                {
                    "label": "Z Hop",
                    "description": "Z axis hop heigth when go to and leave the tower(mm)",
                    "type": "float",
                    "unit": "mm",
                    "default_value": 0.5,
                    "minimum_value": 0.2,
                    "maximum_value": 1.0
                },
                "retracte_type":
                {
                    "label": "Retracte type",
                    "description": "Retraction applied to all extruder steppers or to only previous extruder",
                    "type": "enum",
                    "options": {
                        "all":"all extruders",
                        "previous":"previous extruder"
                    },
                    "default_value": "all"
                },
                "extra_extrusion":
                {
                    "label": "Enable extra extrude line",
                    "description": "To avoid scraping of filament caused by retraction, printing extra lines of extrude simultaneously on the side of the tower",
                    "type": "bool",
                    "default_value": true,
                    "enabled": "retracte_type == 'all'"
                },
                "remove_M104":
                {
                    "label": "Remove unexpected M104",
                    "description": "Remove redundant temperature setting instructions",
                    "type": "bool",
                    "default_value": true
                }
            }
        }"""
        
    def execute(self, data):
        colors = self.getSettingValueByKey("used_color_number")
        startx = self.getSettingValueByKey("tower_start_x")
        starty = self.getSettingValueByKey("tower_start_y")     
        linewidth = round(self.getSettingValueByKey("line_width"),2)
        towerlength = self.getSettingValueByKey("tower_length")
        flowlength = self.getSettingValueByKey("flow_length")
        printspeed =  self.getSettingValueByKey("print_speed") * 60
        speedfirstlayer =   int(printspeed * self.getSettingValueByKey("speed_firstlayer") / 100)
        retractionlength = self.getSettingValueByKey("retraction_length")
        retractionspeed = self.getSettingValueByKey("retraction_speed") * 60
        recoverlength = round(self.getSettingValueByKey("recover_length"),2)
        recoverspeed = self.getSettingValueByKey("recover_speed") * 60
        hopz = round(self.getSettingValueByKey("zhop_heigth"),1)
        
        #logo_file = open("d:/output.gcode", "w+")
        #logo_file.write(";;; This file is created by ZONESTAR Color Switch Tower Genaration V1.0.1b\n")
        #logo_file.write(";;; Website: https://zonestar3d.com\n")
        #logo_file.write(";\n")
        
        bFindM109 = 0
        bFindM104 = 0
        bfisrtTx = 1
        bHasPattern = 0
        
        oldExtrID = -1
        curExtrID = -1
        SwitchingCnt = 0
        backup_e = 0
        
        oldlayer = 0
        curlayer = -1
        totallayers = 99999
        
        flowfactor = round(((1.75*1.75)/(linewidth*linewidth))*1.15,2)
        wipelength = 3
        
        index = 0
        for layer in data:
            lines = layer.split("\n")
            for line in lines:
                line = line.strip()                
                if len(line) == 0:
                    continue
                    
                #logo_file.write(line+"\n")
                if ";FLAVOR:Marlin" in line:
                    addtion_gcode = ""
                    if self.getSettingValueByKey("pattern_type") == "line":
                        addtion_gcode += ";pattern type is Line\n"
                    else:
                        addtion_gcode += ";pattern type is Square\n"
                    addtion_gcode += ";colors = {0:d}\n".format(colors)
                    addtion_gcode += ";line width = {0:.2f} mm\n".format(linewidth)
                    addtion_gcode += ";start_x = {0:d} mm\n".format(startx)
                    addtion_gcode += ";start_y = {0:d} mm\n".format(starty)        
                    addtion_gcode += ";tower length = {0:d}mm\n".format(towerlength)
                    addtion_gcode += ";flow length = {0:d} mm/min\n".format(flowlength)
                    addtion_gcode += ";print speed = {0:d} mm/min\n".format(printspeed)
                    addtion_gcode += ";speed on first layer = {0:d} mm/min\n".format(speedfirstlayer)
                    addtion_gcode += ";retraction length = {0:.2f} mm\n".format(retractionlength)
                    addtion_gcode += ";retraction speed = {0:d} mm/min\n".format(retractionspeed)
                    addtion_gcode += ";recover length = {0:.2f} mm\n".format(recoverlength)
                    addtion_gcode += ";recover speed = {0:d} mm/min\n".format(recoverspeed)
                    addtion_gcode += ";flowfactor = {0:.2f}\n".format(flowfactor)
                    if self.getSettingValueByKey("retracte_type") == "all":
                        addtion_gcode += ";Synchronous retracte\n"
                        l = retractionlength/2
                        s = retractionspeed
                        addtion_gcode += "M207 S{0:.2f} F{1:d} W0 Z0\n".format(l, s)
                        addtion_gcode += "M208 S{0:.2f} F{1:d} W0 R{2:d}\n".format(recoverlength, recoverspeed, s)
                    else:
                        addtion_gcode += ";Retract previous extruder only\n"
                    if self.getSettingValueByKey("extra_extrusion"):
                            addtion_gcode += ";Extra extrusion is enabled\n"
                    data[index] += addtion_gcode
                    #logo_file.write(addtion_gcode)
                    #logo_file.write(";\n")
                    continue
                    
                if ";Layer height:" in line:
                    substr = line[line.find(";Layer height:") + len(";Layer height:"):]
                    layerheight = round(float(substr),2)
                    addtion_gcode = ";Layer height={:.2f}\n".format(layerheight)
                    data[index] += addtion_gcode
                    #logo_file.write(";got total_layers = {:d}\n".format(totallayers))
                    continue
                    
                # find total layers
                if ";LAYER_COUNT:" in line:
                    substr = line[line.find(";LAYER_COUNT:") + len(";LAYER_COUNT:"):]
                    totallayers = int(substr)
                    #logo_file.write(";got total_layers = {:d}\n".format(totallayers))
                    continue
                #
                #M109?
                #set flag when find the first M109, and remove others M109
                if line.startswith("M") and "M109" in line:
                    if bFindM109 == 1 and totallayers - curlayer > 1:
                       #not the first M109 command
                       if self.getSettingValueByKey("remove_M104"):
                           #remove this line
                           data[index] = ";removed by script " + line + "\n"
                           #logo_file.write(";remove a M109\n")
                    bFindM109 = 1
                    continue
                    
                #M104?
                #set flag when find the first M104, and remove others M104
                if line.startswith("M") and "M104" in line and (totallayers - curlayer > 1):
                    if bFindM104 == 1 or bFindM109 == 1:
                        #not the first M104 command                        
                        if self.getSettingValueByKey("remove_M104"):
                            #remove this line
                            data[index] = ";removed by script " + line+ "\n"
                            #logo_file.write(";remove a M104\n")
                    bFindM104 = 1
                    continue
                    
                #backup the position
                if line.startswith("G") and (self.getValue(line, "G") == 1 or self.getValue(line, "G") == 0):
                    if self.getValue(line, "E") is not None:
                        backup_e = float(self.getValue(line, "E"))
                        #logo_file.write(";backup_e = {:.5f}\n".format(backup_e))
                    if self.getValue(line, "X") is not None:
                        backup_x = float(self.getValue(line, "X"))
                        #logo_file.write(";backup_x = {:.5f}\n".format(backup_x))
                    if self.getValue(line, "Y") is not None:
                        backup_y = float(self.getValue(line, "Y"))
                        #logo_file.write(";backup_y = {:.5f}\n".format(backup_y))
                    if self.getValue(line, "Z") is not None:
                        backup_z = float(self.getValue(line, "Z"))
                        #logo_file.write(";backup_y = {:.2f}\n".format(backup_z))
                
                # add tower line when layer changed
                if ";LAYER:" in line:   
                    substr = line[line.find(";LAYER:") + len(";LAYER:"):]
                    curlayer = int(substr)
                    #logo_file.write(";got curlayer={:d}\n".format(curlayer))
                    SwitchingCnt = 0
                    if curlayer - oldlayer > 0:
                        #logo_file.write(";ready to add tower\n")                        
                        oldlayer = curlayer
                        if bHasPattern == 1:
                            #alread has a pattern, don't make it again
                            bHasPattern = 0
                            continue
                        else:
                            #need to add a patteren
                            #bHasPattern = 1
                            #================================================================
                            # prepare data
                            #================================================================
                            #logo_file.write(";current E = {:.5f}\n".format(backup_e))
                            addtion_gcode = ";Start of tower for layer switching, generated by colorSwitchTower\n"
                            if self.getSettingValueByKey("pattern_type") == "line":
                                p_width = ((flowlength*colors*linewidth*flowfactor)/towerlength) - (linewidth*2)
                            else:
                                p_width = towerlength
                            #small p-gap in the first layer
                            if curlayer <= 1:
                                p_gap = linewidth*1.2
                            else:
                                p_gap = (p_width * towerlength) /(flowlength*flowfactor -p_width-towerlength)
                            cur_x = startx
                            cur_y = starty
                            addtion_gcode += ";width = {0:.3f}, gap = {1:.3f}\n".format(p_width,p_gap)
                            data[index] += addtion_gcode
                            #================================================================
                            #add retration gcode, before go to the tower 
                            #================================================================
                            #Retraction
                            addtion_gcode = ""
                            addtion_gcode += "G92 E0\nG1 E-{0:.4f} F{1:d}\n".format(retractionlength, retractionspeed)
                            #z hop
                            cur_z = backup_z + hopz
                            addtion_gcode += "G1 F360 Z{:.2f}\n".format(cur_z)
                            addtion_gcode += "G8 F6000 X{0:.3f} Y{1:.3f}\n".format(cur_x,cur_y)
                            cur_z = backup_z-layerheight
                            addtion_gcode += "G1 F360 Z{:.2f}\n".format(cur_z)
                            #Recover
                            recover_e = retractionlength + recoverlength
                            addtion_gcode += "G92 E0\nG1 E{0:.4f} F{1:d}\nG92 E0\n".format(recover_e,recoverspeed)
                            if curlayer > 1:
                                addtion_gcode += "G1 F{:d}\n".format(printspeed)
                            else:
                                addtion_gcode += "G1 F{:d}\n".format(speedfirstlayer)
                            data[index] += addtion_gcode
                            #logo_file.write(addtion_gcode)
                            #================================================================
                            #Genarate tower
                            #================================================================
                            cur_e = 0.0
                            for i in range(0, 100):
                                addtion_gcode = ""
                                #1 Y+
                                cur_y += p_width
                                cur_e += p_width/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x,cur_y,cur_e)
                                #2 X+
                                if (curlayer > 1 and cur_x >= startx + towerlength - linewidth) or (curlayer <= 1 and cur_x >= startx + towerlength - linewidth):
                                    data[index] += addtion_gcode
                                    #logo_file.write(addtion_gcode)
                                    break
                                elif curlayer > 1 and cur_x >= startx + towerlength - p_gap:
                                    cur_x += linewidth
                                    addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x,cur_y,cur_e)
                                else:
                                    cur_x += p_gap
                                    cur_e += p_gap/flowfactor
                                    addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x,cur_y,cur_e)
                                #3 Y-
                                cur_y -= p_width
                                cur_e += p_width/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x,cur_y,cur_e)                                
                                #4 X+
                                if (curlayer > 1 and cur_x >= startx + towerlength - linewidth) or (curlayer <= 1 and cur_x >= startx + towerlength - linewidth):
                                    data[index] += addtion_gcode
                                    #logo_file.write(addtion_gcode)
                                    break
                                elif curlayer > 1 and cur_x >= startx + towerlength - p_gap:
                                    cur_x += linewidth
                                    addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x,cur_y,cur_e)
                                else:
                                    cur_x += p_gap
                                    cur_e += p_gap/flowfactor
                                    addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x,cur_y,cur_e)
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                            #================================================================
                            #restore the extruder length
                            #================================================================
                            addtion_gcode = ""
                            #retracte
                            addtion_gcode += "G92 E0\nG1 E-{0:.3f} F{1:d}\n".format(retractionlength,retractionspeed)
                            #Z hop and go to 
                            cur_z = backup_z + hopz
                            addtion_gcode += "G1 F360 Z{:.2f}\n".format(cur_z)
                            addtion_gcode += "G8 F6000 X{0:.3f} Y{1:.3f}\n".format(backup_x,backup_y)
                            addtion_gcode += "G1 F360 Z{:.2f}\n".format(backup_z)
                            #recover
                            recover_e = retractionlength + recoverlength
                            addtion_gcode += "G92 E0\nG1 E{0:.4f} F{1:d}\n".format(recover_e,recoverspeed)
                            #resume e
                            addtion_gcode += "G92 E{:.5f}\n".format(backup_e)
                            addtion_gcode += ";End of Tower for layer switching, generated by colorSwitchTower\n\n"
                            data[index] += addtion_gcode
                            #logo_file.write(addtion_gcode)
                            continue
                        #
                    #
                #
                #add tower when color changed
                #find Tx command and add command
                if line.startswith("T") and (self.getValue(line, "T") is not None) and curlayer >= 0:                    
                    curExtrID = self.getValue(line, "T")
                    #logo_file.write(";got T{:d}\n".format(curExtrID))
                    if curExtrID > 7:
                        continue
                    #Ignore the first Tx command
                    if oldExtrID < 0: #the fist tool chain setting command, don't make patterent
                        oldExtrID = curExtrID
                        #logo_file.write(";Pass the first one Tx\n")
                        continue
                    #logo_file.write(";ready to add tower\n")
                    #make patterent
                    bHasPattern = 1
                    #================================================================
                    #add retration gcode before go to the tower 
                    #================================================================                           
                    cur_z = backup_z + hopz
                    recover_e = retractionlength + recoverlength
                    addtion_gcode = ";Start of tower for toolchain change, generated by colorSwitchTower\n"
                    #Retracte
                    if self.getSettingValueByKey("retracte_type") == "all":
                        addtion_gcode += "G92 E0\nG10\n"
                    else:
                        addtion_gcode += "T{:d}\n".format(oldExtrID)
                        addtion_gcode += "G92 E0\nG1 E-{0:.3f} F{1:d}\n".format(retractionlength,retractionspeed)
                        addtion_gcode += "T{:d}\n".format(curExtrID)
                        addtion_gcode += "G92 E0\nG1 E-{0:.3f} F{1:d}\n".format(retractionlength,retractionspeed)
                    #Z Hop
                    addtion_gcode += "G1 F360 Z{0:.2f}\n".format(cur_z)
                    addtion_gcode += "G8 F6000 X{0:.3f} Y{1:.3f}\n".format(startx,starty)
                    addtion_gcode += "G1 F360 Z{:.2f}\n".format(backup_z)
                    #Recover
                    if self.getSettingValueByKey("retracte_type") == "all":
                        addtion_gcode += "G92 E0\nG11\n"
                    else:
                        addtion_gcode += "T{:d}\n".format(oldExtrID)
                        addtion_gcode += "G92 E0\nG1 E{0:.4f} F{1:d}\n".format(recover_e,recoverspeed)
                        addtion_gcode += "T{:d}\n".format(curExtrID)
                        addtion_gcode += "G92 E0\nG1 E{0:.4f} F{1:d}\nG92 E0\n".format(recover_e,recoverspeed)
                    #done
                    data[index] += addtion_gcode
                    #logo_file.write(addtion_gcode)
                    #refersh old extustion, must be here!!!!
                    oldExtrID = curExtrID
                    
                    #================================================================
                    #Genarate tower gcode
                    #================================================================
                    if curlayer <= 1:
                        movementspeed = speedfirstlayer
                    else:
                        movementspeed = printspeed
                    if self.getSettingValueByKey("pattern_type") == "line":
                        cur_x = startx
                        cur_y = starty
                        #
                        cur_e = 0
                        if self.getSettingValueByKey("extra_extrusion"):
                            addtion_gcode = ""
                            addtion_gcode += "T17\nG92 E0\n"
                            for i in range(0, 3):
                                cur_x += towerlength
                                cur_e += towerlength/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                                cur_y += linewidth
                                addtion_gcode += "G8 Y{0:.3f} F{1:d}\n".format(cur_y,movementspeed)
                                cur_x -= towerlength
                                cur_e += towerlength/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                                cur_y += linewidth
                                addtion_gcode += "G8 Y{0:.3f} F{1:d}\n".format(cur_y,movementspeed)
                            addtion_gcode += "T{:d}\nG92 E0\n".format(curExtrID)
                            data[index] += addtion_gcode       
                        #
                        cur_x -= SwitchingCnt * linewidth
                        cur_y += SwitchingCnt * linewidth
                        cur_e = 0
                        addtion_gcode = ""
                        addtion_gcode += "G8 X{0:.3f} Y{1:.3f} F6000\n".format(cur_x,cur_y)
                        data[index] += addtion_gcode
                        #logo_file.write(addtion_gcode)
                        for i in range(0, 100):
                            #1 X+
                            cur_x += towerlength
                            cur_e += towerlength/flowfactor
                            addtion_gcode = ""
                            addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                            #2 Y+
                            cur_y += ((colors - SwitchingCnt)*2 -1)*linewidth
                            cur_e += ((colors - SwitchingCnt)*2 -1)*linewidth/flowfactor
                            addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,speedfirstlayer)
                            #3 X-
                            if (cur_e <= (flowlength - towerlength/(flowfactor*2))):
                                cur_x -= towerlength
                                cur_e += towerlength/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                            else:
                                cur_x -= (towerlength - wipelength)
                                cur_e += (towerlength - wipelength)/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                                cur_x -= wipelength
                                addtion_gcode += "G8 X{0:.3f} Y{1:.3f} F{2:d}\n".format(cur_x,cur_y,movementspeed)
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                                break
                            #4 Y+
                            cur_y += (SwitchingCnt*2 + 1)*linewidth
                            cur_e += (SwitchingCnt*2 + 1)*linewidth/flowfactor
                            addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                            data[index] += addtion_gcode
                            #logo_file.write(addtion_gcode)                            
                    else:
                        #
                        if self.getSettingValueByKey("extra_extrusion"):
                            addtion_gcode = ""
                            addtion_gcode += "T17\nG92 E0\n"
                            cur_e = 0
                            for i in range(0, 2):
                                cur_x = startx - 2*linewidth + i*linewidth
                                cur_y = starty - 2*linewidth + i*linewidth
                                move_length = towerlength + 4*linewidth - 2*i*linewidth
                                cur_x += move_length
                                cur_e += move_length/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                                cur_y += move_length
                                cur_e += move_length/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                                cur_x -= move_length
                                cur_e += move_length/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                                cur_y -= move_length
                                cur_e += move_length/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f} F{3:d}\n".format(cur_x,cur_y,cur_e,movementspeed)
                            addtion_gcode += "T{:d}\nG92 E0\n".format(curExtrID)
                            data[index] += addtion_gcode       
                        #
                        cur_e = 0.0
                        #logo_file.write(addtion_gcode)
                        for i in range(0, 1000):
                            cur_x = float(startx + (SwitchingCnt * linewidth) + (i * linewidth * colors))
                            cur_y = float(starty + (SwitchingCnt * linewidth) + (i * linewidth * colors))
                            move_length = float(towerlength - SwitchingCnt * linewidth * 2 - i * linewidth * colors * 2)
                            #goto to the start position
                            addtion_gcode = ""
                            addtion_gcode += "G8 F6000 X{0:.3f} Y{1:.3f}\n".format(cur_x, cur_y)
                            addtion_gcode += "G1 F{:d}\n".format(movementspeed)
                            #x+
                            cur_x += move_length
                            cur_e += move_length/flowfactor
                            addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x, cur_y, cur_e)
                            #Y+
                            cur_y += move_length
                            cur_e += move_length/flowfactor
                            addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x, cur_y, cur_e)
                            #x-
                            cur_x -= move_length
                            cur_e += move_length/flowfactor
                            addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x, cur_y, cur_e)
                            #Y-
                            if(cur_e >= flowlength) or (move_length <= 4):
                                cur_y -= (move_length-wipelength)
                                cur_e += (move_length-wipelength)/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x, cur_y, cur_e)
                                cur_y -= wipelength
                                addtion_gcode += "G8 X{0:.3f} Y{1:.3f} \n".format(cur_x, cur_y)
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                                break
                            else:
                                cur_y -= move_length
                                cur_e += move_length/flowfactor
                                addtion_gcode += "G1 X{0:.3f} Y{1:.3f} E{2:.4f}\n".format(cur_x, cur_y, cur_e)
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                    #================================================================
                    #retration before leave the tower
                    #================================================================
                    addtion_gcode = ""
                    addtion_gcode += "G92 E0\n"
                    #Retracte
                    if self.getSettingValueByKey("retracte_type") == "all":
                        addtion_gcode += "G10\n"
                    else:
                        addtion_gcode += "G1 E-{0:.3f} F{1:d}\n".format(retractionlength,retractionspeed)
                    #Z hop
                    cur_z = backup_z + hopz
                    addtion_gcode += "G1 F360 Z{:.2f}\n".format(cur_z)
                    addtion_gcode += "G8 F6000 X{0:.3f} Y{1:.3f}\n".format(backup_x, backup_y)
                    addtion_gcode += "G1 F360 Z{:.2f}\n".format(backup_z)
                    #Recover
                    if self.getSettingValueByKey("retracte_type") == "all":
                        addtion_gcode += "G11\n"
                    else:
                        addtion_gcode += "G1 E{0:.4f} F{1:d}\n".format(recoverlength,recoverspeed)
                    addtion_gcode += "G92 E0\n"
                    addtion_gcode += ";End of tower for toolchain change, generated by colorSwitchTower\n\n"
                    data[index] += addtion_gcode
                    #logo_file.write(addtion_gcode)
                    SwitchingCnt += 1
                    continue
                #Tn
            #for line
            index += 1
        #for layer
        #logo_file.close()
        return data
