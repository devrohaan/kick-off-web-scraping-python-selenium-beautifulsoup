#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2016

@author: Rohan

Simple Python Web Scraper: Scrap Pablo Picasso Quotes

Script Requirements: Python3, selenium, PhantomJS, csv, time

"""

from WebDriver import WebDriver
from urllib.error import HTTPError
import time
import csv


url = "https://www.brainyquote.com/authors/pablo_picasso"

def getPabloQuotes(browser):
    try:
        browser.driver.get(url)
        pb_Qoutes = browser.driver.find_elements_by_class_name("b-qt") # To access .b-qt single class : find_element_by_class_name
        pb_links = browser.driver.find_elements_by_class_name("b-qt")
        csvFile = open("./PB_Quotes.csv", "w+")
        writer = csv.writer(csvFile)
        for quotes, quote_link in zip(pb_Qoutes, pb_links):
            print (quotes.text, quote_link.get_attribute('href'))
            writer.writerow((quotes.text, quote_link.get_attribute('href')))

    except (HTTPError, AttributeError) as e:
        print("Error:",e)
    finally:
        csvFile.close()
        browser.driver.quit()


if __name__ == "__main__":

    start_time = time.time()
    browser = WebDriver("ChromeDriver") # you can give three options here 1.Firefox 2.ChromeDriver 3.PhantomJS
    getPabloQuotes(browser)
    print("Quotes are Updated in PB_Quotes.csv")
    print("Execution Time: ", time.time() - start_time, "secomds")
