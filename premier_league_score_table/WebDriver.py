#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2016

@author: Rohan

This class gets the instance of specified web driver.

"""

from selenium import webdriver


class WebDriver(object):

    def __init__(self,drivername):

        if drivername == 'Firefox':
            self.driver = webdriver.Firefox()
        elif drivername == 'ChromeDriver':
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            self.driver = webdriver.Chrome(r"/usr/bin/chromedriver",chrome_options=options)  # provide the chromedriver execution path in case of error
        elif drivername == 'PhantomJS':
            self.driver = webdriver.PhantomJS(r"/usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")  # provide the phantomjs execution path in case of error

        self.driver.implicitly_wait(20)  # seconds
		#This tells Selenium that we would like it to wait for a certain amount of time before throwing an exception that if it cannot find the element on the page.



