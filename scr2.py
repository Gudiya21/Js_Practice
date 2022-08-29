import json
import requests
from bs4 import BeautifulSoup
from task1 import scraping_data
url="https://www.imdb.com/title/tt0111161/"
response=requests.get(url)

Soup=BeautifulSoup(response.content,"html.parser")

def first_movie_data():
    movie_name=url.find("div",class_="sc-b73cd867-0 fbOhB").get_text()
    releasing_year=url.find("li",class_="ipc-inline-list__item")
    movie_details=url.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt").get.text()
    print(movie_details)
    # list=[]
    # first_movie=scraping_data
    # for i in movie_name:
    #     dic={}
        
    #     name=i.h1.text
    #     dic["Movie name"]=name
        
    # for year in releasing_year:
    #     Year=year.li.text
    #     dic["Releasing year"]=Year
    
    # for j in movie_details:
    #     director=j.find("li",class_="ipc-metadata-list__item")
    #     dic["Director"]=director
first_movie_data()