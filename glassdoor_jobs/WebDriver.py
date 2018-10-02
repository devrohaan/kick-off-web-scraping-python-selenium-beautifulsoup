#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2016

@author: Rohan

This class gets the instance of specified web driver.

"""

# use "which packagename" command in linux to find its path

from selenium import webdriver


class WebDriver(object):
	
	def __init__(self,drivername):
		
		if drivername == 'Firefox':
			self.driver = webdriver.Firefox()
		elif drivername == 'ChromeDriver':
			self.driver = webdriver.Chrome(r"/usr/bin/chromedriver")  # provide the chromedriver Execution path in case of error
		elif drivername == 'PhantomJS':
			self.driver = webdriver.PhantomJS(r"/usr/bin/phantomjs")  # provide the phantomjs Execution path in case of error
			
	
		
	


