"""
instalamos 
pip install beautifulsoup4
pip install lxml

"""
from bs4 import BeautifulSoup
import requests
import json

"""
def baseConected():
    response= requests.get("https://www.starz.com/ar/es/")

    print("starz: ",response.status_code)
    return baseConected

"""
def baseURL():
    #Base URL to working with it
    return "https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?"


def listMovies():
    #get the resources directly in json format from the platform API
    response= requests.get(baseURL()+"includes=contentId,contentType,title,product,logLine,detail&contentType=Movie")
    
    soup= BeautifulSoup(response.text,"lxml")
    
    footer= soup.find("p").text

    print("-----CONECTED-----\n")
    
    y= json.dumps(eval(footer),sort_keys=True)
    
    movies= json.loads(y)
    
    print("Type y: ",type(y))
    print("Type: ",type(movies))
   
    class Movie:        
        def __init__(self,contentId,title,contentType,detail,logLine):
            self.contentId= contentId
            self.title= title
            self.contentType= contentType
            self.rating = detail[0]
            self.year= detail[1]
            self.genre= detail[2]
            self.logLine= logLine
            
            
        def __str__(self):
            return """{contentType}:
    Id: {contentId}
    title: {title}
    rating = {rating}
    year= {year}
    genre= {genre}
    logLine: {logLine} #numéros maximos aprox. 400
        """.format( contentType= self.contentType,
                    contentId= self.contentId,
                    title= self.title,
                    rating= self.rating,
                    year= self.year,
                    genre= self.genre,
                    logLine= self.logLine)
    
    
    for element in movies["playContentArray"]["playContents"]:
        #Use split in tag 'details' for separate the rating,year and genre.
        movie= Movie(element["contentId"],element["title"],element["contentType"],element["detail"].split("| "),element["logLine"])
        print(movie)
    

listMovies()



    
    




