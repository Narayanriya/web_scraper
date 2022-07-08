import requests
from bs4 import BeautifulSoup
import re

def timesofindia():
    url = "https://timesofindia.indiatimes.com/home/headlines"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    res=[]


    counter = 0

    for divtag in soup.find_all('div', {'class': 'top-newslist'}):
        for ultag in divtag.find_all('ul', {'class': 'clearfix'}):
            if (counter <= 10):
                for litag in ultag.find_all('li'):
                    counter = counter + 1
                    res.append(str(counter)+ ") " +" "+ litag.find('a')['title'])
    return(res)
                   

def indianexpress():
    url = "https://indianexpress.com/section/india/"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    res1 =[]



    counter = 0

    for divtag in soup.find_all('div', {'class': 'articles'}):
        
        for h2tag in divtag.find_all('h2', {'class': 'title'}):
            if (counter <= 10):
                for atag in h2tag.find_all('a'):
                    
                    counter = counter + 1
                    res1.append(str(counter)+") "  +" "+ atag.text)
    return(res1)
                    


def indiatoday():
    url = "https://www.indiatoday.in/india"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    res2 =[]



    counter = 0
    
    for divtag in soup.find_all('div', {'class': 'view-content'}):
    

            if (counter <= 10):
                for indiv in divtag.find_all('div', {'class': 'detail'}):
                    counter = counter + 1
                    res2.append(str(counter)+ ") " +" "+ indiv.find('h2')['title'])
    return(res2)
                    

def firstpost():
    url = "https://www.firstpost.com/category/india"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    res3 =[]



    counter = 0
    
    for divtag in soup.find_all('div', {'id': 'category-wrapper'}):
        
        if (counter <= 10):
            for indiv in divtag.find_all('div', {'class': 'big-thumb'}):
                
                counter = counter + 1
                res3.append(str(counter)+ ") " +" "+ indiv.find('img')['title'])
    return(res3)
                    


toe_res = timesofindia()
ie_res = indianexpress()
it_res = indiatoday()
fp_res = firstpost()

