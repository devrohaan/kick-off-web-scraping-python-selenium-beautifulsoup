#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2016

@author: Rohan

Basics of Python Web Scraping: 

Hi Buddy! This is a kick-off-script to get hands on.
Script Requirements: Python3, BeautifulSoup, urllib

I have implemented few basic examples using selenium, Do check them out! This script covers approximately 0.1% of entire
python web scraping. Here my motive is to get you familiar with the tools that python provides if you forsee your career in 
web automation.
  	
"""

from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


#Simple Ex. 1

html = urlopen("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")
bsObj =BeautifulSoup(html.read())
#print(bsObj) # shows the entire page source HTML i.e. DOM (Document Object Model) structure for the page mentioned in the URL

print(bsObj.h1) #accessing tags
print(bsObj.h2) #accessing tags
print(bsObj.body.h3) #accessing tags

'''
There are two main things that can go wrong in this line:
 The page is not found on the server (or there was some error in retrieving it)
 The server is not found

Along with this, there are fair chances that a mentioned attribute in the DOM is not present.

Hence, we must this. It is the most important web scraping ritual to handle these two basic exceptions.
'''


#Simple Ex. 2: Invalid Link

try:
    html = urlopen("https://en.wikipedia.org/wiki/Cristio_Ronaldo") 
except HTTPError as e:
    print(e)
	

#Simple Ex. 3: Best practise

try:
    html = urlopen("https://en.wikipedia.org/wiki/Cristio_Ronaldo") 
except (HTTPError, AttributeError) as e:
    print(e)
	

# Few BeautifulSoup methods


html = urlopen("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")
bsObj = BeautifulSoup(html)    
nameList = bsObj.findAll("span", {"class":"nowrap"}) #prints all values with tag span and class as nowrap whereas, find() returns only the first occurence of the condition
for name in nameList:
    print(name.get_text()) 
print(len(nameList))    
   
    
crnamecount = bsObj.findAll(text = "Cristiano Ronaldo") # calculates the count this string is present in the page
print(len(crnamecount)) #17 times printed 


id = bsObj.findAll(id = "mw-content-text")
print(len(id))
print(id) # return DOM bcz it is not a list so we cant do get_text()



# parsing table

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

tabledata = bsObj.findAll("table",{"id":"giftList"}) # fetches the entire table data DOM code
print(tabledata)    


# images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")}) # "." indicates presence of any one charater so to escape its original meaning we use "\."

# crawl deep

'''
find the first div with id tag and then find all links present in that div  
'''

html = urlopen("http://en.wikipedia.org/wiki/Cristiano_Ronaldo") 
bsObj = BeautifulSoup(html)
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")): 
    print(link) #all links present in that div 
    #OP: <a href="/wiki/Frank_McLintock" title="Frank McLintock">McLintock</a>
    #if 'href' in link.attrs:
    #   print(link.attrs['href'])

	
