'''pip install bs4
pip install pycodestyle  flake8 pycodestyle_magic
pip install python-dateutil
pip install getuseragent
pip install pyside6
'''

from requests_html import HTMLSession
import sys
import requests
import re
import time
from bs4 import BeautifulSoup
from dateutil import parser
from getuseragent import UserAgent
from PySide6.QtCore import *
from PySide6.QtWidgets import *
#from pycodestyle_magic import pycodestyle_on
 
#pip install lxml
import lxml.html
#pip install downloader
#from downloader import Downloader
import urllib.request
from urllib.parse import urlparse

# Set 'useragent' for the requests to mimic human browsing
useragent = UserAgent(requestsPrefix=True).Random()
print(useragent)

# Set the target URL (example URL, please replace with the actual target
# page)
base_url ="https://www.cuinacatalana.eu/ca/pag/receptes/?s=&pag="
page=0

from requests_html import HTMLSession
session = HTMLSession()


while True:
    url = base_url+str(page)
    response = session.get(url)
    response.html.render()

    # Check response status
    if response.status_code == 200:
        #print (response.text)
        # Parse the page content
        soup = BeautifulSoup(response.content, 'lxml')
        #print(soup.prettify())
        signoff = soup.find("div", class_="signoff")
        if signoff:
            print("No more results found")
            break  # Break the loop if this message is found

        # Find all property listing items
        listings = soup.find_all("h2")
    
        # Extract data for each property
        print("*" * 50)
    
        for listing in listings:
            a_tag = listing.find("a")
            if a_tag and a_tag.get("href"):
                print(a_tag.get("href"))
        page = page + 1

    
            #price = listing.find()
    
            # Get the property price
            #price = listing.find('span', class_='item-price').get_text(
            #    strip=True)
    
            # Get the property location
           # location = listing.find('span', class_='item-detail').get_text(
            #    strip=True)
    
            # Print the data
            #print ("data")
            #print(f'Title: {title}')
            #print(f'Price: {price}')
            #print(f'Location: {location}')
        print('-' * 50)
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
