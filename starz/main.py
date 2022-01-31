import os
import json
from conected import *

#this file creates a .json file in the same directory where it is hosted.

pwd= os.getcwd()    #path actual


"""


"""
files= os.listdir()

if "data.json" in files:
    
    for file in os.listdir():
    
        if ".json" in file:
            os.remove(file)
            
            finalDir= createListMoviesAndSeries()
            
            jsonString= json.dumps(finalDir)
            
            jsonFile= open("data.json","w")
            
            jsonFile.write(jsonString)
            jsonFile.close()
else:
    
    finalDir= createListMoviesAndSeries()
            
    jsonString= json.dumps(finalDir)    
    jsonFile= open("data.json","w")
    
    jsonFile.write(jsonString)
    jsonFile.close()
    
    


        
        
    