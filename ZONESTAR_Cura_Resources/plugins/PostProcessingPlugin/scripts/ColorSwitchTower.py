# Color switching Tower Genaration
# This script is specific for the ZONESTAR M3 and M4 3d printer 
# It runs with the PostProcessingPlugin which is released under the terms of the AGPLv3 or higher.
# This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms

# Authors of the Color switching Tower Genaration plug-in / script:
# Written by Hally.Zhong - hally@zonestar3d.com

#history / change-log:
#V1.0.1 - Initial

import re
from ..Script import Script

class ColorSwitchTower(Script):
    def __init__(self):
        super().__init__()
        
    def getSettingDataString(self):
        return """{
            "name": "ZONESTAR Color Switch Tower Genaration V1.0.1",
            "key": "ColorSwitchTower",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "pattern_type":
                {
                    "label": "Choose Pattern Type",
                    "description": "Pattern Type is line or square",
                    "type": "enum",
                    "options": {
                        "line":"Line",
                        "square":"Square"
                    },
                    "default_value": "line"
                },
                "line_width_factor":
                {
                    "label": "line width factor of the tower",
                    "description": "= line width of tower / nozzle size, between 0.8 ~ 1.6",
                    "type": "float",
                    "default_value": 1.0,
                    "minimum_value": 0.8,
                    "maximum_value": 1.6
                },
                "used_color_number":
                {
                    "label": "Used Color Number",
                    "description": "The number of colors used when printing, between 3 ~ 8",
                    "type": "int",
                    "default_value": 3
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
                    "label": "length of the tower",
                    "description": "Value to the length (at X axis) of the tower (mm), between 20 ~ 100",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 60,
                    "minimum_value": 20,
                    "maximum_value": 100
                },
                "flow_length":
                {
                    "label": "flow length",
                    "description": "Need to be extruded filament length when switch to a new color (mm), between 10 ~ 100",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 50,
                    "minimum_value": 10,
                    "maximum_value": 100
                },
                "retraction_length":
                {
                    "label": "retraction length",
                    "description": "Value to retract length when go to or leave the tower(mm), between 5 ~ 20",
                    "type": "int",
                    "unit": "mm",
                    "default_value": 8,
                    "minimum_value": 5,
                    "maximum_value": 20   
                },
                "retraction_speed":
                {
                    "label": "retraction speed",
                    "description": "Value to retracte speed when go to or leave the tower(mm/s), between 15 ~ 40",
                    "type": "int",
                    "unit": "mm/s",
                    "default_value": 25,
                    "minimum_value": 15,
                    "maximum_value": 40
                },
                "remove_M104":
                {
                    "label": "Remove Unexpected M104",
                    "description": "Remove redundant temperature setting instructions",
                    "type": "bool",
                    "default_value": true
                }
            }
        }"""
        
    def execute(self, data):
        startx = self.getSettingValueByKey("tower_start_x")
        starty = self.getSettingValueByKey("tower_start_y")       
        retractionlength = self.getSettingValueByKey("retraction_length")
        retractionspeed = self.getSettingValueByKey("retraction_speed") * 60
        colors = self.getSettingValueByKey("used_color_number") 
        factor = self.getSettingValueByKey("line_width_factor")
        towerlength = self.getSettingValueByKey("tower_length")
        flowlength = self.getSettingValueByKey("flow_length")
        if self.getSettingValueByKey("pattern_type") == "line":
            patterntype = 0
        else:
            patterntype = 1
        
        #logo_file = open(output.gcode, "w+")
        #logo_file.write(";;; This file is created by ZONESTAR Color Switch Tower Genaration V1.0.1b\n")
        #logo_file.write(";;; Website: https://zonestar3d.com\n")
        #logo_file.write(";\n")
        
        bFindM109 = 0
        bFindM104 = 0
        bfisrtTx = 1
        bHasPattern = 0
        
        oldExtrID = -1
        curExtrID = -1
        new_e = 0
        
        oldlayer = 0
        curlayer = 0
        totallayers = 99999
        
        #flowfactor = (1.75*1.75)/(0.4*0.4)
        flowfactor = (1.75*1.75*4)/(factor*factor)
        wipelength = 5
                 
        index = 0;
        for layer in data:
            lines = layer.split("\n")
            for line in lines:
                line = line.strip()                
                if len(line) == 0:
                    continue
                    
                #logo_file.write(line+"\n")
                if ";FLAVOR:Marlin" in line:
                    addtion_gcode = ""
                    if patterntype == 0:
                        addtion_gcode += ";pattern_type is Line\n"
                    else:
                        addtion_gcode += ";pattern_type is Square\n"
                    addtion_gcode += ";colors = {0:d}\n".format(colors)
                    addtion_gcode += ";factor = {0:.2f}\n".format(factor)
                    addtion_gcode += ";start_x = {0:.2f}\n".format(startx)
                    addtion_gcode += ";start_y = {0:.2f}\n".format(starty)        
                    addtion_gcode += ";towerlength = {0:.2f}\n".format(towerlength)
                    addtion_gcode += ";flowlength = {0:.2f}\n".format(flowlength)
                    addtion_gcode += ";retractionlength = {0:.2f}\n".format(retractionlength)
                    addtion_gcode += ";retractionspeed = {0:d}\n".format(retractionspeed)
                    #logo_file.write(addtion_gcode)
                    #logo_file.write(";\n")
                    data[index] += addtion_gcode
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
                    
                #store the extrude length
                if line.startswith("G") and self.getValue(line, "G") == 1:
                    if self.getValue(line, "E") is not None:
                        new_e = float(self.getValue(line, "E"))
                        #logo_file.write(";new_e = {:.5f}\n".format(new_e))
                    continue
                
                # add tower line when layer changed
                if ";LAYER:" in line:   
                    substr = line[line.find(";LAYER:") + len(";LAYER:"):]
                    curlayer = int(substr)
                    #logo_file.write(";got curlayer={:d}\n".format(curlayer))
                    curExtrno = -1
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
                            #add retration gcode, before go to the tower 
                            #================================================================
                            #logo_file.write(";current E = {:.2f}\n".format(new_e))
                            hopz = 0.5
                            addtion_gcode = ";Start of tower for layer switching, generated by colorSwitchTower\n"
                            #z up
                            addtion_gcode += "G91\nG1 F480 Z{:.1f}\nG90\n".format(hopz)
                            #go to
                            addtion_gcode += "G0 F6000 X{0:.2f} Y{1:.2f}\n".format(startx,starty)
                            #load filament
                            addtion_gcode += "G92 E0\nG1 E{0:.2f} F{1:d}\n".format(retractionlength,retractionspeed)
                            data[index] += addtion_gcode
                            #logo_file.write(addtion_gcode)
                            #================================================================
                            #Genarate tower gcode
                            #================================================================                            
                            addtion_gcode = ""
                            if patterntype == 0:
                                p_width = (flowlength*colors*factor*flowfactor)/(towerlength*2)
                            else:
                                p_width = towerlength
                            p_gap = (p_width * towerlength) /(flowlength*flowfactor -p_width-towerlength)
                            #p_gap = towerlength * flowlength * colors/(towerlength - flowlength*colors)
                            addtion_gcode += ";width = {0:.2f}, gap = {1:.2f}\n".format(p_width,p_gap)
                            cur_x = startx + curExtrno * factor/2
                            cur_y = starty + curExtrno * factor/2                            
                            addtion_gcode += "G0 X{0:.2f} Y{1:.2f} F6000\n".format(cur_x,cur_y)
                            #z down
                            hopz += layerheight
                            addtion_gcode += "G91\nG1 F360 Z-{:.1f}\nG90\nG1 F3000\n".format(hopz)
                            data[index] += addtion_gcode
                            #logo_file.write(addtion_gcode)
                            #
                            cur_e = 0.0
                            for i in range(0, 100):
                                addtion_gcode = ""
                                #1 X+
                                cur_x += p_gap
                                cur_e += p_gap/flowfactor
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                                #1 Y+
                                cur_y += p_width
                                cur_e += p_width/flowfactor
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                                if (cur_x - startx - towerlength) > 0.1:
                                    data[index] += addtion_gcode
                                    #logo_file.write(addtion_gcode)
                                    break
                                #2 X+
                                cur_x += p_gap
                                cur_e += p_gap/flowfactor
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                                #3 Y-
                                cur_y -= p_width
                                cur_e += p_width/flowfactor
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)                                
                                if (cur_x - startx - towerlength) > 0.1:
                                    data[index] += addtion_gcode
                                    #logo_file.write(addtion_gcode)
                                    break
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                            #================================================================
                            #restore the extruder length
                            #================================================================
                            addtion_gcode = "G91\nG1 F360 Z{:.1f}\nG90\n".format(layerheight)
                            #restore the extruder length
                            addtion_gcode += "G92 E0\nG1 E-{0:.2f} F{1:d}\n".format(retractionlength,int(retractionspeed))
                            addtion_gcode += "G92 E{:.2f}\n".format(new_e)
                            addtion_gcode += ";End of Tower for layer switching, generated by colorSwitchTower\n\n"
                            data[index] += addtion_gcode
                            #logo_file.write(addtion_gcode)
                            continue
                        #
                        continue
                    #
                    continue
                #
                #add tower when color changed
                #find Tx command and add command
                if line.startswith("T") and (self.getValue(line, "T") is not None):                    
                    curExtrID = self.getValue(line, "T")
                    #logo_file.write(";got T{0:d}\n".format(curExtrID))
                    if curExtrID > 7:
                        continue
                    #Ignore the first Tx command
                    if oldExtrID == -1: #the fist tool chain setting command, don't make patterent  
                        oldExtrID = curExtrID
                        #logo_file.write(";Pass the first one Tx\n")
                        continue
                    #logo_file.write(";ready to add tower\n")
                    oldExtrID = curExtrID
                    curExtrno += 1
                    #make patterent
                    bHasPattern = 1
                    #================================================================
                    #add retration gcode, before go to the tower 
                    #================================================================
                    hopz = 0.5
                    addtion_gcode = ";Start of tower for toolchain change, generated by colorSwitchTower\n"
                    addtion_gcode += "G1 E-{0:.2f} F{1:d}\n".format(retractionlength,retractionspeed)
                    addtion_gcode += "G91\nG1 F360 Z{:.1f}\nG90\n".format(hopz)
                    addtion_gcode += "G0 F6000 X{0:.2f} Y{1:.2f}\n".format(startx,starty)
                    addtion_gcode += "G1 E0 F{0:d}\n".format(retractionspeed)
                    addtion_gcode += "G91\nG1 F360 Z-{:.1f}\nG90\n".format(hopz)
                    data[index] += addtion_gcode
                    #logo_file.write(addtion_gcode)                    
                    #================================================================
                    #Genarate tower gcode
                    #================================================================
                    if patterntype == 0:
                        cur_x = startx - curExtrno * factor / 2
                        cur_y = starty + curExtrno * factor / 2
                        cur_e = 0
                        addtion_gcode = ""
                        addtion_gcode += "G1 F3000\n"
                        addtion_gcode += "G0 X{0:.2f} Y{1:.2f}\n".format(cur_x,cur_y)
                        data[index] += addtion_gcode
                        #logo_file.write(addtion_gcode)                        
                        for i in range(0, 100):
                            #1 X+
                            cur_x += towerlength
                            cur_e += towerlength/flowfactor
                            addtion_gcode = ""
                            addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                            #2 Y+
                            cur_y += ((colors-curExtrno)*2 -1)*factor/2
                            cur_e += ((colors-curExtrno)*2 -1)*factor/(flowfactor*2)
                            addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                            #3 X-
                            cur_e += towerlength/flowfactor
                            if (cur_e <= (flowlength - towerlength/(flowfactor*2))):
                                cur_x -= towerlength
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                            else:
                                cur_x -= (towerlength-wipelength)
                                cur_e -= (towerlength-wipelength)/flowfactor
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                                cur_x -= wipelength
                                addtion_gcode += "G0 X{0:.2f} Y{1:.2f}\n".format(cur_x,cur_y)
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                                break
                            #4 Y+
                            cur_y += (curExtrno*2 + 1)*factor/2
                            cur_e += (curExtrno*2 + 1)*factor/(flowfactor*2)
                            addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x,cur_y,cur_e)
                            data[index] += addtion_gcode
                            #logo_file.write(addtion_gcode)                            
                    else:
                        cur_e = 0.0
                        #logo_file.write(addtion_gcode)
                        for i in range(0, 1000):
                            cur_x = float(startx + (curExtrno * factor / 2) + (i * factor * colors / 2))
                            cur_y = float(starty + (curExtrno * factor / 2) + (i * factor * colors / 2))
                            move_length = float(towerlength - curExtrno * factor - i * factor * colors)
                            #goto to the start position
                            addtion_gcode = ""
                            addtion_gcode += "G0 F6000 X{0:.2f} Y{1:.2f}\n".format(cur_x, cur_y)
                            addtion_gcode += "G1 F3000\n"
                            #x+
                            cur_x += move_length
                            cur_e += move_length/flowfactor
                            addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x, cur_y, cur_e)
                            #Y+
                            cur_y += move_length
                            cur_e += move_length/flowfactor
                            addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x, cur_y, cur_e)
                            #x-
                            cur_x -= move_length
                            cur_e += move_length/flowfactor
                            addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x, cur_y, cur_e)
                            #Y-
                            cur_e += move_length/flowfactor
                            if(cur_e >= flowlength) or (move_length <= 4):
                                cur_y -= (move_length-wipelength)
                                cur_e -= (move_length-wipelength)/flowfactor
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x, cur_y, cur_e)
                                cur_y -= wipelength
                                addtion_gcode += "G0 X{0:.2f} Y{1:.2f} \n".format(cur_x, cur_y)
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                                break
                            else:
                                cur_y -= move_length
                                addtion_gcode += "G1 X{0:.2f} Y{1:.2f} E{2:.2f}\n".format(cur_x, cur_y, cur_e)
                                data[index] += addtion_gcode
                                #logo_file.write(addtion_gcode)
                    #================================================================
                    #retration before leave the tower
                    #================================================================
                    addtion_gcode = "G92 E0\n"
                    addtion_gcode += "G91\nG1 F360 Z{:.1f}\nG90\n".format(hopz)
                    addtion_gcode = ";End of tower for toolchain change, generated by colorSwitchTower\n\n"
                    data[index] += addtion_gcode
                    #logo_file.write(addtion_gcode)
                    continue
                #Tn
            #for line
            index += 1
        #for layer
        #logo_file.close()
        return data
