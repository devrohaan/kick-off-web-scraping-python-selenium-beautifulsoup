#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2018

@author: Rohan

Simple Python Web Scraper: English Premier League score table update.

Script Requirements: Python3, BeautifulSoup, Selenium, PhantomJS, csv, time, pandas, tabulate, pickle

"""
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from WebDriver import WebDriver
from urllib.error import HTTPError
from time import sleep
from time import time
import pandas as pd
from tabulate import tabulate
import pickle


url = "http://www.espn.in/football/table/_/league/eng.1"

def currentYearScoreTable(browser):
    
    try:
        browser.driver.get(url)
        soup = BeautifulSoup(browser.driver.page_source)
        # next four lines are magic lines otherwise life would be hell, disecting the Soup. Just Hate it!! Say thanks to Pandas
        table = soup.find_all('table')[0]
        df = pd.read_html(str(table), header = 0)
        print(df[0])
        print(tabulate(df[0],tablefmt='psql'))
        # magic lines end
        
        #with blocks handle closing so again a good pratice!
        with open("Curent_EPL_Standings.txt", "wb") as f:
            pickle.dump(tabulate(df[0],tablefmt='psql'), f)
    
    except (HTTPError, AttributeError) as e:
        print("Error:", e)
        
    finally:
        
        browser.driver.quit()
    

def allEPLScoreTables(browser):
    
    try:
        browser.driver.get(url)
        links = browser.driver.find_elements_by_name("&lpos=eng.1:standings:filter:year")
        print(links)
        
        for year in links:
            browser = WebDriver("ChromeDriver")
            browser.driver.get(year.get_attribute('href'))
            soup = BeautifulSoup(browser.driver.page_source)
            table = soup.find_all('table')[0]
            df = pd.read_html(str(table), header = 0)
            print(tabulate(df[0],tablefmt='psql'))   
            with open("All_EPL_Standings.txt", "wb") as f:
                pickle.dump(tabulate(df[0],tablefmt='psql'), f)
        
    except (HTTPError, AttributeError) as e:
        print("Error:", e)
    finally:
        browser.driver.quit()    

    
if __name__ == "__main__":
    print("Current Year:")
    start_time = time.time()
    browser = WebDriver("ChromeDriver") # you can give three options here 1.Firefox 2.ChromeDriver 3.PhantomJS
    currentYearScoreTable(browser);
    print("Score Table is updated in Curent_EPL_Standings.txt")
    print("Execution Time: ", time.time() - start_time, "secomds")
    print("#########################")
    print("All Years:")
    start_time = time.time()
    browser = WebDriver("ChromeDriver") # you can give three options here 1.Firefox 2.ChromeDriver 3.PhantomJS
    allEPLScoreTables(browser);
    print("Score Tables are updated in All_EPL_Standings.txt")
    print("Execution Time: ", time.time() - start_time, "secomds")
    
    
    
