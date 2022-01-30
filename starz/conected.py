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
    return "https://www.starz.com/ar/es/"
def requestURL():
    #Base URL to working with it
    return "https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?"

class Serie:

        def __init__(self,title,contentType,contentId,logLine,detail,childContent):
            self.title=title
            self.contentType= contentType
            self.contentId= contentId
            self.link= baseURL()+"series/"+title.replace(" ","-")+"/"+str(contentId)
            self.logLine= logLine
            self.rating= detail[0]
            self.cantSeason= detail[1]
            self.genre= detail[2]
            self.seasons=childContent
        
        def __str__(self):
            return """{contentType}:
                title: {title}
                contentId: {contentId}
                link: {link}
                logLine: {logLine}
                rating: {rating}
                cantSeason: {cantSeason}
                genre: {genre}
                seasons: {seasons}
            """.format(contentType=self.contentType,
            title=self.title,
            contentId=self.contentId,
            link= self.link,
            logLine=self.logLine,
            rating=self.rating,
            cantSeason= self.cantSeason,
            genre=self.genre,
            seasons=self.seasons)

class Movie:        
        def __init__(self,contentId,title,contentType,detail,logLine):
            self.contentId= contentId
            self.title= title
            self.link= baseURL() + "movies/" +title.replace(" ","-")+ "-" + str(contentId)
            self.contentType= contentType
            self.rating = detail[0]
            self.year= detail[1]
            self.genre= detail[2]
            self.logLine= logLine
            
            
        def __str__(self):
            return """{contentType}:
    Id: {contentId}
    title: {title}
    link: {link}
    rating = {rating}
    year= {year}
    genre= {genre}
    logLine: {logLine} #numéros maximos aprox. 400
        """.format( contentType= self.contentType,
                    contentId= self.contentId,
                    title= self.title,
                    link= self.link,
                    rating= self.rating,
                    year= self.year,
                    genre= self.genre,
                    logLine= self.logLine)

def listMovies():
    #get the resources directly in json format from the platform API
    response= requests.get(requestURL()+"includes=contentId,contentType,title,product,logLine,detail&contentType=Movie")
    
    soup= BeautifulSoup(response.text,"lxml")
    
    footer= soup.find("p").text

    print("-----CONECTED-----\n")
    
    y= json.dumps(eval(footer))
    
    movies= json.loads(y)
    
    print("Type y: ",type(y))
    print("Type: ",type(movies))
   
    
    
    
    for element in movies["playContentArray"]["playContents"]:
        #Use split in tag 'details' for separate the rating,year and genre.
        movie= Movie(element["contentId"],element["title"],element["contentType"],element["detail"].split("| "),element["logLine"])
        print(movie)

def listSeries():
    #include=title,contentType,contentId,logLine,detail,childContent&contentType=Series
    response= requests.get(requestURL()+"include=title,contentType,contentId,logLine,detail,childContent&contentType=Series")
    
    soup= BeautifulSoup(response.text,"lxml")
    
    footer= soup.find("p").text

    print("-----CONECTED-----\n")

    
    #print(footer)
    
    y= json.dumps(eval(footer),sort_keys=True)

    series=json.loads(y)

    

    for element in series["playContentArray"]["playContents"]:
        serie=Serie(element["title"],element["contentType"],element["contentId"],element["logLine"],element["detail"].split("| "),element["childContent"])

        print(serie,"\n")


#listMovies()

listSeries()
   




    
    




