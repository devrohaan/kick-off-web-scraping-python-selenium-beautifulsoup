#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2016

@author: Rohan

Simple Python Web Scraper: Glassdoor jobs notifier based on company name and location.

Script Requirements: Python3, BeautifulSoup, Selenium, PhantomJS, csv, time

"""
from selenium.webdriver.common.keys import Keys
from WebDriver import WebDriver
from urllib.error import HTTPError
from time import sleep
from time import time
import csv


url = "https://www.glassdoor.co.in/index.htm"

def findMeAJob(browser, companyname, location):
    try:
        browser.driver.get(url)
        keywordSearch = browser.driver.find_element_by_id("KeywordSearch")
        locationSearch = browser.driver.find_element_by_id("LocationSearch")
        keywordSearch.send_keys(companyname)
        locationSearch.send_keys(Keys.COMMAND+'a') # this was creating trouble in Mac OS so added a pause of 1 second. Don't use .clear() to clear out the existing text.
        sleep(1)
        locationSearch.send_keys(Keys.DELETE)
        sleep(1)
        locationSearch.send_keys(location)
        sleep(1)
        browser.driver.find_element_by_id("HeroSearchButton").click()
        job_list = browser.driver.find_elements_by_class_name("jl")
        
        csvFile = open("./GlassDoor_Jobs.csv", "w+")
        writer = csv.writer(csvFile)
        for job in job_list:
            print(job.text)
            writer.writerow((job.text))
    except (HTTPError, AttributeError) as e:
        print("Error:", e)
    finally:
        csvFile.close()
        browser.driver.quit()
		

    
    
if __name__ == "__main__":
    start_time = time()
    browser = WebDriver("ChromeDriver") # you can give three options here 1.Firefox 2.ChromeDriver 3.PhantomJS
    findMeAJob(browser, "TCS", "India"); # hard-coded for quick demonstration purpose.
    print("Jobs are Posted in GlassDoor_Jobs.csv")
    print("Execution Time: ", time() - start_time, "secomds")
