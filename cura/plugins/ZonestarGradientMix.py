# ZONESTAR ColorMix script - 2/3/4-IN-1-OUT extruder color mix and blending
# This script is specific for the ZONESTAR mixing color 3d printer
# It runs with the PostProcessingPlugin which is released under the terms of the AGPLv3 or higher.
# This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms

#Authors of the 2-1 ColorMix plug-in / script:
# Written by Hally Zhong - hally@zonestar3d.com

#history / change-log:
#V1.0.0 - Initial

# Uses -
# M163 - Set Mix Factor 
# M164 - Save Mix Factor to a VTOOL
# M166 - Start a gradient mix

import re #To perform the search and replace.
from ..Script import Script

class ZonestarGradientMix(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Zonestar Gradient Color Mix Tool V1.0.0",
            "key":"ZonestarGradientColorMix",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "extruder_number":
                {
                    "label": "Extruder Number",
                    "description": "Number of extruders, 2 ~ 4",
                    "type": "int",
                    "default_value": 4,
                    "minimum_value": "2",
                    "maximum_value": "4"
                },
                "segments_number":
                {
                    "label": "Segments",
                    "description": "Number of segments, 2 ~ 5",
                    "type": "int",
                    "default_value": 2,
                    "minimum_value": "1",
                    "maximum_value": "5"
                },
                "units_of_measurement":
                {
                    "label": "Units",
                    "description": "Input value as mm or layer number",
                    "type": "enum",
                    "options": {"mm":"mm","layer":"Layer"},
                    "default_value": "mm"   
                },                
                "segment1_start_height":
                {
                    "label": "Segment 1 Start Height",
                    "description": "Value to start height of Segment 1 (mm or layer)",
                    "type": "float",
                    "default_value": 0,
                    "minimum_value": "0"
                },
                "segment1_end_height":
                {
                    "label": "Segment 1 End Height",
                    "description": "Value to end height of Segment 1 (mm or layer)",
                    "type": "float",
                    "default_value": 10,
                    "minimum_value": "0",                    
                    "minimum_value_warning": "segment1_start_height"                
                },
                "segment1_start_mixrate_extrduer1":
                {
                    "label": "E1 Start weight - S1",
                    "description": "Extruder 1 start mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100"
                },                
                "segment1_start_mixrate_extrduer2":
                {
                    "label": "E2 Start weight - S1",
                    "description": "Extruder 2 start mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100"                    
                },                
                "segment1_start_mixrate_extrduer3":
                {
                    "label": "E3 Start weight - S1",
                    "description": "Extruder 3 start mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "extruder_number > 2"                 
                },
                "segment1_start_mixrate_extrduer4":
                {
                    "label": "E4 Start weight - S1",
                    "description": "Extruder 4 start mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "extruder_number > 3"                  
                },
                "segment1_end_mixrate_extrduer1":
                {
                    "label": "E1 End weight - S1",
                    "description": "Extruder 1 end mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100"               
                },
                "segment1_end_mixrate_extrduer2":
                {
                    "label": "E2 End weight - S1",
                    "description": "Extruder 2 end mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100"
                },
                "segment1_end_mixrate_extrduer3":
                {
                    "label": "E3 End weight - S1",
                    "description": "Extruder 3 end mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "extruder_number > 2"                 
                },                                
                "segment1_end_mixrate_extrduer4":
                {
                    "label": "E4 End weight - S1",
                    "description": "Extruder 4 end mix weight of Segment 1, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "extruder_number > 3"
                },
                "segment2_jointwith_last":
                {
                    "label": "Joint with end of segment 1",
                    "description": "Use the end height and color mix ratio of the previous stage as the start height and color mix ratio of this stage",
                    "type": "bool",
                    "default_value": true,
                    "enabled": "segments_number > 1"
                },
                "segment2_start_height":
                {
                    "label": "Segment 2 Start Height",
                    "description": "Value to start height of Segment 2 (mm or layer)",
                    "type": "float",
                    "default_value": 11,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment1_end_height",
                    "enabled": "not segment2_jointwith_last and segments_number > 1"
                },
                "segment2_end_height":
                {
                    "label": "Segment 2 End Height",
                    "description": "Value to end height of Segment 2 (mm or layer)",
                    "type": "float",
                    "default_value": 20,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment2_start_height",
                    "enabled": "segments_number > 1"
                },  
                "segment2_start_mixrate_extrduer1":
                {
                    "label": "E1 Start weight - S2",
                    "description": "Extruder 1 start mix weight of Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment2_jointwith_last and segments_number > 1"
                },                
                "segment2_start_mixrate_extrduer2":
                {
                    "label": "E2 Start weight - S2",
                    "description": "Extruder 2 start mix weight of Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment2_jointwith_last and segments_number > 1"                    
                },                
                "segment2_start_mixrate_extrduer3":
                {
                    "label": "E3 Start weight - S2",
                    "description": "Extruder 3 start mix weight of Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "not segment2_jointwith_last and segments_number > 1 and extruder_number > 2"
                },                
                "segment2_start_mixrate_extrduer4":
                {
                    "label": "E4 Start weight - S2",
                    "description": "Extruder 4 start mix weight of Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "not segment2_jointwith_last and segments_number > 1 and extruder_number > 3"
                },
                "segment2_end_mixrate_extrduer1":
                {
                    "label": "E1 End weight - S2",
                    "description": "Extruder 1 end mix weight of Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 1"                    
                },
                "segment2_end_mixrate_extrduer2":
                {
                    "label": "E2 End weight - S2",
                    "description": "Extruder 2 end mix weight of Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 1"                    
                },
                "segment2_end_mixrate_extrduer3":
                {
                    "label": "E3 End weight - S2",
                    "description": "Extruder 3 end mix weight of at Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "segments_number > 1 and extruder_number > 2"                 
                },
                "segment2_end_mixrate_extrduer4":
                {
                    "label": "E4 End weight - S2",
                    "description": "Extruder 4 end mix weight of Segment 2, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "segments_number > 1 and extruder_number > 3"                  
                },
                "segment3_jointwith_last":
                {
                    "label": "Joint with end of segment 2",
                    "description": "Use the end height and color mix ratio of the previous stage as the start height and color mix ratio of this stage",
                    "type": "bool",
                    "default_value": true,
                    "enabled": "segments_number > 2"
                },
                "segment3_start_height":
                {
                    "label": "Segment 3 Start Height",
                    "description": "Value to start height of Segment 3 (mm or layer)",
                    "type": "float",
                    "default_value": 20.1,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment2_end_height",                    
                    "enabled": "not segment3_jointwith_last and segments_number > 2"
                },
                "segment3_end_height":
                {
                    "label": "Segment 3 End Height",
                    "description": "Value to end height of Segment 3 (mm or layer)",
                    "type": "float",
                    "default_value": 30,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment3_start_height",
                    "enabled": "segments_number > 2"
                },   
                "segment3_start_mixrate_extrduer1":
                {
                    "label": "E1 Start weight - S3",
                    "description": " Extruder 1 start mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment3_jointwith_last and segments_number > 2"
                },                
                "segment3_start_mixrate_extrduer2":
                {
                    "label": "E2 Start weight - S3",
                    "description": "Extruder 2 start mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment3_jointwith_last and segments_number > 2"                    
                },                
                "segment3_start_mixrate_extrduer3":
                {
                    "label": "E3 Start weight - S3",
                    "description": "Extruder 3 start mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "not segment3_jointwith_last and segments_number > 2 and extruder_number > 2"
                },                
                "segment3_start_mixrate_extrduer4":
                {
                    "label": "E4 Start weight - S3",
                    "description": "Extruder 4 start mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "not segment3_jointwith_last and segments_number > 2 and extruder_number > 3"
                },
                "segment3_end_mixrate_extrduer1":
                {
                    "label": "E1 End weight - S3",
                    "description": "Extruder 1 end mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 2"                    
                },
                "segment3_end_mixrate_extrduer2":
                {
                    "label": "E2 End weight - S3",
                    "description": "Extruder 2 end mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 2"                    
                },
                "segment3_end_mixrate_extrduer3":
                {
                    "label": "E3 End weight - S3",
                    "description": "Extruder 3 end mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "segments_number > 2 and extruder_number > 2"                 
                },
                "segment3_end_mixrate_extrduer4":
                {
                    "label": "E4 End weight - S3",
                    "description": "Extruder 4 end mix weight of Segment 3, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "segments_number > 2 and extruder_number > 3"                  
                },
                "segment4_jointwith_last":
                {
                    "label": "Joint with end of segment 3",
                    "description": "Use the end height and color mix ratio of the previous stage as the start height and color mix ratio of this stage",
                    "type": "bool",
                    "default_value": true,
                    "enabled": "segments_number > 3"
                },
                "segment4_start_height":
                {
                    "label": "Segment 4 Start Height",
                    "description": "Value to start height of Segment 4 (mm or layer)",
                    "type": "float",
                    "default_value": 30,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment3_end_height",                    
                    "enabled": "not segment4_jointwith_last and segments_number > 3"
                },
                "segment4_end_height":
                {
                    "label": "Segment 4 End Height",
                    "description": "Value to end height of Segment 4 (mm or layer)",
                    "type": "float",
                    "default_value": 40,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment4_start_height",
                    "enabled": "segments_number > 3"
                }, 
                "segment4_start_mixrate_extrduer1":
                {
                    "label": "E1 Start weight - S4",
                    "description": " Extruder 1 start mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment4_jointwith_last and segments_number > 3"
                },                
                "segment4_start_mixrate_extrduer2":
                {
                    "label": "E2 Start weight - S4",
                    "description": " Extruder 2 start mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment4_jointwith_last and segments_number > 3"
                },                
                "segment4_start_mixrate_extrduer3":
                {
                    "label": "E3 Start weight - S4",
                    "description": "Extruder 3 start mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "not segment4_jointwith_last and segments_number > 3 and extruder_number > 2"
                },                
                "segment4_start_mixrate_extrduer4":
                {
                    "label": "E4 Start weight - S4",
                    "description": "Extruder 2 start mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "not segment4_jointwith_last and segments_number > 3 and extruder_number > 3"
                },
                "segment4_end_mixrate_extrduer1":
                {
                    "label": "E1 End weight - S4",
                    "description": "Extruder 1 end mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 3"                    
                },
                "segment4_end_mixrate_extrduer2":
                {
                    "label": "E2 End weight - S4",
                    "description": "Extruder 2 end mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 3"                    
                },
                "segment4_end_mixrate_extrduer3":
                {
                    "label": "E3 End weight - S4",
                    "description": "Extruder 3 end mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "segments_number > 3 and extruder_number > 2"                 
                },
                "segment4_end_mixrate_extrduer4":
                {
                    "label": "E4 End weight - S4",
                    "description": "Extruder 4 end mix weight of Segment 4, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "segments_number > 3 and extruder_number > 3"                  
                },
                "segment5_jointwith_last":
                {
                    "label": "Joint with end of segment 4",
                    "description": "Use the end height and color mix ratio of the previous stage as the start height and color mix ratio of this stage",
                    "type": "bool",
                    "default_value": true,
                    "enabled": "segments_number > 4"
                },
                "segment5_start_height":
                {
                    "label": "Segment 5 Start Height",
                    "description": "Value to start height of Segment 5 (mm or layer)",
                    "type": "float",
                    "default_value": 40,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment4_end_height",                    
                    "enabled": "not segment5_jointwith_last and segments_number > 4"
                },
                "segment5_end_height":
                {
                    "label": "Segment 5 End Height",
                    "description": "Value to end height of Segment 5 (mm or layer)",
                    "type": "float",
                    "default_value": 50,
                    "minimum_value": "0",
                    "minimum_value_warning": "segment5_start_height",
                    "enabled": "segments_number > 4"
                },  
                "segment5_start_mixrate_extrduer1":
                {
                    "label": "E1 Start weight - S5",
                    "description": " Extruder 1 start mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment5_jointwith_last and segments_number > 4"
                },                
                "segment5_start_mixrate_extrduer2":
                {
                    "label": "E2 Start weight - S5",
                    "description": " Extruder 2 start mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "not segment5_jointwith_last and segments_number > 4"
                },                
                "segment5_start_mixrate_extrduer3":
                {
                    "label": "E3 Start weight - S5",
                    "description": "Extruder 3 start mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "not segment5_jointwith_last and segments_number > 4 and extruder_number > 2"
                },                
                "segment5_start_mixrate_extrduer4":
                {
                    "label": "E4 Start weight - S5",
                    "description": "Extruder 4 start mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "not segment5_jointwith_last and segments_number > 4 and extruder_number > 3"
                },
                "segment5_end_mixrate_extrduer1":
                {
                    "label": "E1 End weight - S5",
                    "description": "Extruder 1 end mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 4"                    
                },
                "segment5_end_mixrate_extrduer2":
                {
                    "label": "E2 End weight - S5",
                    "description": "Extruder 2 end mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100",
                    "enabled": "segments_number > 4"                    
                },
                "segment5_end_mixrate_extrduer3":
                {
                    "label": "E3 End weight - S5",
                    "description": "Extruder 3 end mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",   
                    "enabled": "segments_number > 4 and extruder_number > 2"                 
                },
                "segment5_end_mixrate_extrduer4":
                {
                    "label": "E4 End weight - S5",
                    "description": "Extruder 4 end mix weight of Segment 5, 0 ~ 100",
                    "type": "int",
                    "default_value": 0,
                    "minimum_value": "0",
                    "maximum_value": "100",  
                    "enabled": "segments_number > 4 and extruder_number > 3"                  
                }
            }
        }"""
        
    def getValue(self, line, key, default = None): #replace default getvalue due to comment-reading feature
        if not key in line or (";" in line and line.find(key) > line.find(";") and
                                   not ";ChangeAtZ" in key and not ";LAYER:" in key):
            return default
        subPart = line[line.find(key) + len(key):] #allows for string lengths larger than 1
        if ";ChangeAtZ" in key:
            m = re.search("^[0-4]", subPart)
        elif ";LAYER:" in key:
            m = re.search("^[+-]?[0-9]*", subPart)
        else:
            #the minus at the beginning allows for negative values, e.g. for delta printers
            m = re.search("^[-]?[0-9]*\.?[0-9]*", subPart)
        if m == None:
            return default
        try:
            return float(m.group(0))
        except:
            return default

    def execute(self, data):        
        # logo_file = open("d:/logo_zonestarcolormix.txt", "w+")        
        # logo_file.write(";;; This file is created by ZonestarColorMix\n")
        # logo_file.write("============================================\n")
        # logo_message = ""

        #get mix weight and start and end height        
        start_Z_height = [0 for i in range(5)]
        end_Z_height = [0 for i in range(5)]
        start_mix_table = [[0 for i in range(5)] for j in range(5)]
        end_mix_table = [[0 for i in range(5)] for j in range(5)]

        extruders = self.getSettingValueByKey("extruder_number")
        segments = self.getSettingValueByKey("segments_number")

        #segment1
        # logo_message += "1\n"
        start_Z_height[0] = self.getSettingValueByKey("segment1_start_height")        
        start_mix_table[0][0] = self.getSettingValueByKey("segment1_start_mixrate_extrduer1")        
        start_mix_table[0][1] = self.getSettingValueByKey("segment1_start_mixrate_extrduer2")
        if extruders > 2:
            start_mix_table[0][2] = self.getSettingValueByKey("segment1_start_mixrate_extrduer3")            
        if extruders > 3:
            start_mix_table[0][3] = self.getSettingValueByKey("segment1_start_mixrate_extrduer4")

        end_Z_height[0] = self.getSettingValueByKey("segment1_end_height")
        end_mix_table[0][0] = self.getSettingValueByKey("segment1_end_mixrate_extrduer1")
        end_mix_table[0][1] = self.getSettingValueByKey("segment1_end_mixrate_extrduer2")
        if extruders > 2:
            end_mix_table[0][2] = self.getSettingValueByKey("segment1_end_mixrate_extrduer3")
        if extruders > 3:
            end_mix_table[0][3] = self.getSettingValueByKey("segment1_end_mixrate_extrduer4")
        
        #segment2
        # logo_message += "2\n"
        if segments > 1:
            if self.getSettingValueByKey("segment2_jointwith_last"):
                start_Z_height[1] = end_Z_height[0]
                start_mix_table[1][0] = end_mix_table[0][0]
                start_mix_table[1][1] = end_mix_table[0][1]
                if extruders > 2:
                    start_mix_table[1][2] = end_mix_table[0][2]
                if extruders > 3:
                    start_mix_table[1][3] = end_mix_table[0][3]
            else:
                start_Z_height[1] = self.getSettingValueByKey("segment2_start_height")
                start_mix_table[1][0] = self.getSettingValueByKey("segment2_start_mixrate_extrduer1")
                start_mix_table[1][1] = self.getSettingValueByKey("segment2_start_mixrate_extrduer2")
                if extruders > 2:
                    start_mix_table[1][2] = self.getSettingValueByKey("segment2_start_mixrate_extrduer3")                
                if extruders > 3:
                    start_mix_table[1][3] = self.getSettingValueByKey("segment2_start_mixrate_extrduer4")

            end_Z_height[1] = self.getSettingValueByKey("segment2_end_height")            
            end_mix_table[1][0] = self.getSettingValueByKey("segment2_end_mixrate_extrduer1")            
            end_mix_table[1][1] = self.getSettingValueByKey("segment2_end_mixrate_extrduer2")
            if extruders > 2:
                end_mix_table[1][2] = self.getSettingValueByKey("segment2_end_mixrate_extrduer3")
            if extruders > 3:
                end_mix_table[1][3] = self.getSettingValueByKey("segment2_end_mixrate_extrduer4")
        
        #segment3
        # logo_message += "3\n"
        if segments > 2:
            if self.getSettingValueByKey("segment3_jointwith_last"):
                start_Z_height[2] = end_Z_height[1]
                start_mix_table[2][0] = end_mix_table[1][0]
                start_mix_table[2][1] = end_mix_table[1][1]
                if extruders > 2:
                    start_mix_table[2][2] = end_mix_table[1][2]
                if extruders > 3:
                    start_mix_table[2][3] = end_mix_table[1][3]
            else:
                start_Z_height[2] = self.getSettingValueByKey("segment3_start_height")            
                start_mix_table[2][0] = self.getSettingValueByKey("segment3_start_mixrate_extrduer1")            
                start_mix_table[2][1] = self.getSettingValueByKey("segment3_start_mixrate_extrduer2")
                if extruders > 2:
                    start_mix_table[2][2] = self.getSettingValueByKey("segment3_start_mixrate_extrduer3")
                if extruders > 3:
                    start_mix_table[2][3] = self.getSettingValueByKey("segment3_start_mixrate_extrduer4")

            end_Z_height[2] = self.getSettingValueByKey("segment3_end_height")
            end_mix_table[2][0] = self.getSettingValueByKey("segment3_end_mixrate_extrduer1")
            end_mix_table[2][1] = self.getSettingValueByKey("segment3_end_mixrate_extrduer2")
            if extruders > 2:
                end_mix_table[2][2] = self.getSettingValueByKey("segment3_end_mixrate_extrduer3")
            if extruders > 3:
                end_mix_table[2][3] = self.getSettingValueByKey("segment3_end_mixrate_extrduer4")
        
        #segment4
        # logo_message += "4\n"
        if segments > 3:
            if self.getSettingValueByKey("segment4_jointwith_last"):
                start_Z_height[3] = end_Z_height[2]
                start_mix_table[3][0] = end_mix_table[2][0]
                start_mix_table[3][1] = end_mix_table[2][1]
                if extruders > 2:
                    start_mix_table[3][2] = end_mix_table[2][2]
                if extruders > 3:
                    start_mix_table[3][3] = end_mix_table[2][3]
            else:
                start_Z_height[3] = self.getSettingValueByKey("segment4_start_height")            
                start_mix_table[3][0] = self.getSettingValueByKey("segment4_start_mixrate_extrduer1")            
                start_mix_table[3][1] = self.getSettingValueByKey("segment4_start_mixrate_extrduer2")
                if extruders > 2:
                    start_mix_table[3][2] = self.getSettingValueByKey("segment4_start_mixrate_extrduer3")
                if extruders > 3:
                    start_mix_table[3][3] = self.getSettingValueByKey("segment4_start_mixrate_extrduer4")

            end_Z_height[3] = self.getSettingValueByKey("segment4_end_height")
            end_mix_table[3][0] = self.getSettingValueByKey("segment4_end_mixrate_extrduer1")
            end_mix_table[3][1] = self.getSettingValueByKey("segment4_end_mixrate_extrduer2")
            if extruders > 2:
                end_mix_table[3][2] = self.getSettingValueByKey("segment4_end_mixrate_extrduer3")
            if extruders > 3:
                end_mix_table[3][3] = self.getSettingValueByKey("segment4_end_mixrate_extrduer4")

        #segment5
        # logo_message += "5\n"
        if segments > 4:
            if self.getSettingValueByKey("segment5_jointwith_last"):
                start_Z_height[4] = end_Z_height[3]
                start_mix_table[4][0] = end_mix_table[3][0]
                start_mix_table[4][1] = end_mix_table[3][1]
                if extruders > 2:
                    start_mix_table[4][2] = end_mix_table[3][2]
                if extruders > 3:
                    start_mix_table[4][3] = end_mix_table[3][3]
            else:
                start_Z_height[4] = self.getSettingValueByKey("segment5_start_height")            
                start_mix_table[4][0] = self.getSettingValueByKey("segment5_start_mixrate_extrduer1")            
                start_mix_table[4][1] = self.getSettingValueByKey("segment5_start_mixrate_extrduer2")
                if extruders > 2:
                    start_mix_table[4][2] = self.getSettingValueByKey("segment5_start_mixrate_extrduer3")
                if extruders > 3:
                    start_mix_table[4][3] = self.getSettingValueByKey("segment5_start_mixrate_extrduer4")

            end_Z_height[4] = self.getSettingValueByKey("segment5_end_height")
            end_mix_table[4][0] = self.getSettingValueByKey("segment5_end_mixrate_extrduer1")
            end_mix_table[4][1] = self.getSettingValueByKey("segment5_end_mixrate_extrduer2")
            if extruders > 2:
                end_mix_table[4][2] = self.getSettingValueByKey("segment5_end_mixrate_extrduer3")
            if extruders > 3:
                end_mix_table[4][3] = self.getSettingValueByKey("segment5_end_mixrate_extrduer4")
                
        #get layer height
        # logo_message += "6\n"
        layerHeight = 0
        for active_layer in data:
            lines = active_layer.split("\n")
            for line in lines:
                if ";Layer height: " in line:
                    layerHeight = self.getValue(line, ";Layer height: ", layerHeight)
                    break
            if layerHeight != 0:
                break        
        #default layerHeight if not found
        if layerHeight == 0:
            layerHeight = .2
        
        #get layers to use
        # logo_message += "7\n"
        startLayer = [0 for i in range(5)]
        endLayer = [0 for i in range(5)]
        start_height_mm = [0.0 for i in range(5)]
        end_height_mm = [0.0 for i in range(5)]
        if self.getSettingValueByKey("units_of_measurement") == "mm":
            for i in range(segments):
                startLayer[i] = int(round(start_Z_height[i] / layerHeight))
                start_height_mm[i] = start_Z_height[i]
                endLayer[i] = int(round(end_Z_height[i] / layerHeight))
                end_height_mm[i] = end_Z_height[i]
        else:
            for i in range(segments):
                startLayer[i] = int(start_Z_height[i])
                endLayer[i] = int(end_Z_height[i])
                start_height_mm[i] = startLayer[i]*layerHeight
                end_height_mm[i] = endLayer[i]*layerHeight
        
        # Check if the mix rate is the same
        # logo_message += "8\n"
        flag_GradientMix = [0]*segments
        for i in range(segments):
            for j in range(extruders):
                if start_mix_table[i][j] != end_mix_table[i][j] and startLayer[i] != endLayer[i]:
                    flag_GradientMix[i] = 1
                    break
        # set vtool gcode
        set_vtool_gcode = ["","","","",""]            
        for i in range(segments):
            addtion_gcode = ""
            addtion_gcode += ";Set start VTOOL 5 for gradient mix printing\n"
            for j in range(extruders):
                addtion_gcode += "M163 S{0:d} P{1:d}\n".format(j, start_mix_table[i][j])                
            addtion_gcode += "M164 S5\n"    
            if flag_GradientMix[i] != 0:
                addtion_gcode += ";Set End VTOOL 6 for gradient mix printing\n"
                for j in range(extruders):
                    addtion_gcode += "M163 S{0:d} P{1:d}\n".format(j, end_mix_table[i][j])
                addtion_gcode += "M164 S6\n"
            set_vtool_gcode[i] = addtion_gcode

        #set gradient mix gcode        
        # logo_message += "9\n"
        set_GradientMix_gcode = ["","","","",""]                
        for i in range(segments): 
            if flag_GradientMix[i] != 0:
                m = i + 1
                addtion_gcode = ";Start Stage {0:d} gradient mix printing\n".format(m)
                addtion_gcode += "M166 S1 A{0:.1f} Z{1:.1f} I5 J6\n".format(start_height_mm[i], end_height_mm[i])                
            else:
                addtion_gcode = "T5\n"
            set_GradientMix_gcode[i] = addtion_gcode

        #start scanning
        # logo_message += "10\n"        
        # for i in range(segments):
        #     logo_message += set_vtool_gcode[i]
        # for i in range(segments):
        #     logo_message += set_GradientMix_gcode[i]
        # logo_file.write(logo_message)
        # logo_message = ""

        index = 0
        layer = -1
        flag_added = [0 for i in range(5)]
        for active_layer in data:
            modified_gcode = ""
            lineIndex = 0
            lines = active_layer.split("\n")
            for line in lines:
                #don't leave blanks 
                line = line.strip()
                if len(line) == 0:
                    continue
                    
                if ";FLAVOR:Marlin" in line:
                    modified_gcode += ";ZonestarGradientMix plugin settings\n"
                    modified_gcode += ";extruders = {0:d}, segments = {1:d}, layerHeight = {2:.1f}\n".format(extruders, segments, layerHeight)                    
                    for i in range(segments):
                        m = i + 1
                        modified_gcode += ";Segment {0:d}: start layer = {1:d}, height = {2:.1f}mm. end layer = {3:d}, height = {4:.1f}mm.\n".format(m, startLayer[i], start_height_mm[i], endLayer[i], end_height_mm[i])                        

                if ";LAYER_COUNT:" in line and startLayer[0] == 0:
                    flag_added[0] = 1
                    modified_gcode += ";===============================================\n"
                    modified_gcode += ";Add by ZonestarGradientMix plugin\n"
                    modified_gcode += ";Segment 1 --> start layer = 0, height = 0mm; end layer = {0:d}, height = {1:.1f}mm\n".format(endLayer[0], end_height_mm[0])
                    modified_gcode += set_vtool_gcode[0]
                    modified_gcode += set_GradientMix_gcode[0]
                    modified_gcode += ";===============================================\n"

                # # find current layer
                if ";LAYER:" in line:                    
                    #substr = line[line.find(";LAYER:") + len(";LAYER:"):]
                    #layer = int(substr)
                    layer = self.getValue(line, ";LAYER:", layer)
                    #search for layers to manipulate    
                    for i in range(segments):                
                        if layer >= int(startLayer[i] - 1) and flag_added[i] == 0:
                            flag_added[i] = 1
                            #add mixing commands
                            m = i + 1
                            modified_gcode += ";===============================================\n"
                            modified_gcode += ";Add by ZonestarGradientMix plugin\n"
                            modified_gcode += ";Segment {0:d} --> start layer = {1:d}, height={2:.1f}mm; end layer = {3:d}, height = {4:.1f}mm\n".format(m, startLayer[i], start_height_mm[i], endLayer[i], end_height_mm[i])                            
                            modified_gcode += set_vtool_gcode[i]
                            modified_gcode += set_GradientMix_gcode[i]
                            modified_gcode += ";===============================================\n"
                lineIndex += 1  #for deleting index   
            data[index] += modified_gcode  
            # logo_message += modified_gcode
            index += 1
        # logo_file.write(logo_message)
        return data