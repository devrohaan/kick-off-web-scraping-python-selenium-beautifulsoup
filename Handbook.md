[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

# Cooking the Cookbook: Web Scarping
*... a run-through of the whole show.*

###### Turning the unstructured data on the web into machine readable, structured data which is ready for analysis.

### What is Web Scarping?

What do you do when you have a question you want to answer, but don’t have the data at hand? Same thing
as everyone else: Google it. Only this time as a coder, you also write a program to go onto whatever website Google sent you to
and take out all those lovely bits and pieces of information!

As the name suggests, this is a technique used for extracting data from websites. It is an automated process
where an application processes the HTML of a Web Page to extract data for manipulation such as converting
the Web page to another format and copying it into a local database or spreadsheet for later retrieval or
analysis.

Data is collected from different sources such as Web, Database, log files etc. and then it is thoroughly cleaned and reshaped, and further used for analysis and explored to determine the hidden patterns and trends which is really essential for any business decision making, Extracting data from web is always easy with the help of API's but what if website doesn't provide any API's, In such case, Web Scraping is an excellent way to extract the unstructured data from web and put that in structured format 

###  Web Scraping Tools

- There are a few ways you can start web scraping in python. If you are just after the HTML you will probably
be fine using the requests library. Basically this sends a request to a website and returns you the response filled with HTML code which you can sort through to find what you need.
- BeautifulSoup is a good option most of the time.
- Web scraping with Python often requires no more than the use of the Beautiful Soup module to reach the
goal. Beautiful Soup is a popular Python library that makes web scraping by traversing the DOM (document
object model) easier to implement.
However, some websites use JavaScript links. Therefore, examples using Python and Beautiful Soup will not
work without some extra additions. With Selenium, programming a Python script to automate a web browser
is possible.
- Selenium, on the other hand, uses a driver that basically opens up a version of your web browser that can be
controlled by python. This has the advantage that the website you are visiting views you basically like any
other human surfer allowing you to access information in the same way. Plus you can see it in action which is
pretty cool.


### What is Selenium?

*Selenium is a Web Browser Automation Tool. Primarily, it is for automating web applications for testing
purposes, but is certainly not limited to just that.* It allows you to open a browser of your choice & perform
tasks as a human being would, such as:

- Clicking buttons
- Entering information in forms
- Searching for specific information on the web pages

The Selenium package is used to automate web browser interaction from Python.

### What is PhantomJS?

*PhantomJS is a headless browser that can be used with the Selenium web automation module. Unlike the
FirefoxDriver or ChromeDriver, the browser stays totally invisible during the process.*

A headless browser is a web browser without a graphical user interface. In other words it is a browser, a
piece of software, that access web pages but doesn't show them to any human being. They're actually used to
provide the content of web pages to other programs.
So technically, PhantomJS is a headless WebKit with JavaScript API
In future versions of PhantomJS, the GhostDriver component have been included.
GhostDriver is a pure JavaScript implementation of the WebDriver Wire Protocol for PhantomJS. It's a
Remote WebDriver that uses PhantomJS as a back-end.
So, Ghostdriver is the bridge we need to use Selenium WebDriver with Phantom.JS.
Selenium control Phantomjs via Ghostdriver.


# Warm-Up: BeautifulSoup

Hi Buddy! This walk through will help you get ready for [kick-off-web-scraping-python-selenium-beautifulsoup](https://github.com/robagwe/kick-off-web-scraping-python-selenium-beautifulsoup/blob/master/kick-off-Scraping.py)!

I am going to discuss few basics of BeautifulSoup library and Selenium. It would be great if you actually go
through the code samples.

**urllib:** contains functions for requesting data across the web, handling cookies, and even changing metadata
such as headers and your user agent.
Note: In Python 3.x, urllib2 was renamed urllib and was split into several submodules: urllib.request,
urllib.parse, and url lib.error.

**urlopen:** is used to open a remote object across a network and read it. Because it is a fairly generic library
(it can read HTML files, image files, or any other file stream with ease)

> The web is messy. Data is poorly formatted, websites go down, and closing tags go missing. One of the most
frustrating experiences in web scraping is to go to sleep with a scraper running, dreaming of all the data
you’ll have in your database the next day—only to find out that the scraper hit an error on some unexpected
data format and stopped execution shortly after you stopped looking at the screen.

> *Hence we must try: and except :*
		
		try:
			html = urlopen("https://en.wikipedia.org/wiki/Cristio_Ronaldo")
		except (HTTPError, AttributeError) as e:
 			print(e)
			
			
> BeautifulSoup’s find() and findAll() are the two functions you will likely use the most. With them, you can
easily filter HTML pages to find lists of desired tags.
	findAll(tag, attributes, recursive, text, limit, keywords)
	find(tag, attributes, recursive, text, keywords)

> In all likelihood, 95% of the time you will find yourself only needing to use the first two arguments: tag and
attributes. The recursive argument is a boolean. How deeply into the document do you want to go? If recursion is set to
True, the findAll function looks into children, and child- ren’s children, for tags that match your parameters.
Default is True

*Find more details on BeautifulSoup [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).*

### You are expected to have a good hands on in python Regex module while dealing with BeautifulSoup. I have drafted an introductory [kick-off-regex-python](https://github.com/robagwe/kick-off-regex-python) repository, which might be helpful to start-off with.

### Uses Cases of Web Scraping:

There are many uses for Web Scraping but I will mention just a few:
- Online Price Change Monitoring & Price Comparison
- Product Review scraping: to watch your competition
- Gathering Real Estate Listings
- Weather Data Monitoring
- Website Change Detection
- Research, Data Mining
- Tracking Online Presence and Reputation
- Web Data Integration


**Ethical Warning:**.

> First, check the site with the information you need and see if they have an API. If they do, that means they
were kind enough to try to set up an easy way to access their information that is probably beneficial for both
you and them. Second, check out their terms of service agreement. They might not want you scraping; it can
be pretty intensive on their part to keep getting hit with requests. From a robot. Who is even MORE unlikely
to make spurious purchases from their invasive ads. And third, just to be thorough, do a search combining
their website and ‘robot.txt’. You’ll likely find a file telling you what you are allowed to scrap and what you
are not. Cool.

> Some websites don't like to be scrapped and in that case you need to disguise your web scraping bot as a
Human Being. Hence we must make use of such drivers.

> It is important to note that Web scraping is against most websites’ terms of service. Your IP address may be
banned from a website if you scrape too frequently or maliciously.



###### List of important Selenium methods used quite frequently. Visit [here](https://selenium-python.readthedocs.io/) for more information.
	
	1. driver.navigate().to(url);
	2. driver.forward();
	3. driver.navigate().forward();
	4. driver.navigate().back();
	5. driver.navigate().refresh();
	6. isSelected( ) – This method tests if a element is active or selected. It doesn’t allow any parameter, but it
			does return a Boolean status.
	7. isEnabled();
	8. submit( ) – This method initiates the submission of an HTML form. It doesn’t allow any parameter and
		       its return type is void.
	9. element.submit();



