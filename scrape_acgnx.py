import cfscrape
import requests
import os
from recaptcha import *
from bs4 import BeautifulSoup
import re

# Requests wrapper
#url = 'https://www.acgnx.se/'
url = 'https://www.acgnx.se/show-8A7C71BCBEB854DDF0880AF26FB4504A47F50B2D.html'
session = requests.session()
session.headers = 'content-type'
session.mount("http://", cfscrape.CloudflareScraper())
scraper = cfscrape.create_scraper(sess=session)
req = scraper.get(url).content
#print req

### Save request as HTML named as 'Result.html'
f_name = '\Result.html'
f = open(f_name, 'w')
f.write(req.encode('UTF-8'))
f.close

### Excute JavaScript file
start = time()
driver = webdriver.Chrome(os.getcwd()+"\chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get(os.getcwd()+f_name)
#print driver.page_source

# Get download link
soup = BeautifulSoup(driver.page_source, "lxml")
link = str(soup.findAll(id="download"))
#print link
regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
link = regex.findall(link)
#print link
link = 'https://www.acgnx.se/'+str(link[0])
response = requests.request('GET', link)
print "link: "+ link + '\n', response



#mainWin = driver.current_window_handle
#driver = recaptcha_process(driver)
#print(driver.page_source)
#driver.close()
#elapsed = time() - start
#print(elapsed)



