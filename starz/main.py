#!/usr/bin/python3

import os
import json
from conected import *

#this file creates a .json file in the same directory where it is hosted.

files= os.listdir()

if "data.json" in files:
    
    for file in os.listdir():
    
        if ".json" in file:
            os.remove(file)
            
            finalDir= createListMoviesAndSeries()           
            
            jsonFile= open("data.json","w",encoding='utf8')
            
            jsonString= json.dumps(finalDir,ensure_ascii=False)
            
            jsonFile.write(jsonString)
            jsonFile.close()
else:
    
    finalDir= createListMoviesAndSeries()
            
      
    jsonFile= open("data.json","w",encoding='utf8')
    
    jsonString= json.dumps(finalDir,ensure_ascii=False)  
    
    jsonFile.write(jsonString)
    jsonFile.close()
    
    


        
        
    