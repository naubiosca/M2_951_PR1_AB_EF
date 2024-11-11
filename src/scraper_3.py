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


# Dynamic website scraping alternative using Selenium
#pip install selenium
from selenium import webdriver

# Exemple google
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
#url ='https://www.idealista.com/en/venta-viviendas/madrid-madrid/'
#url = 'https://www.fotocasa.es/ca/comprar/habitatges/barcelona-capital/totes-les-zones/l'
#url = "https://www.habitaclia.com/viviendas-barcelona.html"
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
driver.implicitly_wait(10)
print("ChromeDriver is working!")
print (driver.title)


# Open the webpage

# Extract the page source or interact with the page
page_source = driver.page_source

print(page_source)

# Don't forget to quit the driver after you're done
driver.quit()
'''

from requests_html import HTMLSession
session = HTMLSession()


# Set request headers to mimic a browser request
#cookie = '''__utmc=22935970; ajs_anonymous_id=09afdabe-ccec-4c39-ad90-088b1f9e767d; _gcl_au=1.1.734506090.1726037352; _fbp=fb.1.1726037352022.65446587151869647; _ga=GA1.2.737935508.1726037351; ASPSESSIONIDACSQCTTQ=DBCFACBBOMOCBOEOHPNGGGGN; borosTcf=eyJwb2xpY3lWZXJzaW9uIjoyLCJjbXBWZXJzaW9uIjoxLCJwdXJwb3NlIjp7ImNvbnNlbnRzIjp7IjEiOnRydWUsIjIiOnRydWUsIjMiOnRydWUsIjQiOnRydWUsIjUiOnRydWUsIjYiOnRydWUsIjciOnRydWUsIjgiOnRydWUsIjkiOnRydWUsIjEwIjp0cnVlfX0sInNwZWNpYWxGZWF0dXJlcyI6eyIxIjp0cnVlfX0=; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; adit-xandr-id=4945204317052799840; __gsas=ID=15d4a2046f4c2dc1:T=1729799059:RT=1729799059:S=ALNI_MZTIfiOjTAIb5l35EcKUF4E3oIwdg; habGeoIp=1; supportsFlash=false; ASP.NET_SessionId=1qk010wiga1efsdmwinxuudz; ad_tamanofotos=n; _hjSessionUser_774043=eyJpZCI6ImRmMTBiYjdmLWNiZjItNTdlZS05NWQ3LTdlYjNjZjA0NzMzMSIsImNyZWF0ZWQiOjE3Mjk3OTkwNjAyNTEsImV4aXN0aW5nIjp0cnVlfQ==; info-alerta=visible; ASPSESSIONIDCCDASQSS=NHMNDGOCKBKIOEIDCLMMDBDH; _uetvid=8dd5abd0924011efaa080d70f5fa28bd; cto_bundle=lhIsRV9XUUg3allucjNOcVB0S0lnVVptaVdFWkxtZ3dlejU2cjVhQUpGRjZvY2lNJTJCcmRmJTJCeWpZWmUlMkJ3S2JHeFg5bWhJMUdCUUxLNTFDd0lmaWxiR1BQZWg1JTJCYk1yb21weDE2SVh6b3VsOVR3YTBTNmh4UExHOFlvUFBncFU0dXAzR29BZkJheENEVGRmYjRUU25sUUpva1dDSmlRY0dFaW13SmlsbmZ0VlBoJTJCZXFBJTNE; ASPSESSIONIDSABBTTSR=FENMPKNCKCIKANMEMMJCFKHK; ASPSESSIONIDQCDDQTQS=HPLHKNKDBELDABMPCLLJFNMJ; habitacliaUtmz=utmcsr=www.google.com|utmcmd=referal|utmccn=referal; ASPSESSIONIDQAQABQDT=GJHGGBCAKHJNHCOHNAEPJOOC; __utma=22935970.737935508.1726037351.1730646634.1731262133.7; __utmz=22935970.1731262133.7.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); AMCV_05FF6243578784B37F000101%40AdobeOrg=-408604571%7CMCIDTS%7C20038%7CMCMID%7C43873057172224341712342652396031657352%7CMCAAMLH-1731866935%7C6%7CMCAAMB-1731866935%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1731269335s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.6.0; didomi_token=eyJ1c2VyX2lkIjoiMTkyYzAwZWUtMGNhYi02OTkwLWJmOWQtMDM4N2IyYTE3YWQxIiwiY3JlYXRlZCI6IjIwMjQtMTAtMjRUMTk6NDQ6MTMuNTE0WiIsInVwZGF0ZWQiOiIyMDI0LTExLTEwVDE4OjA4OjU4LjY1NVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpzZWdtZW50IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOmFkZXZpbnRhbS1ZRkFLVWV4TiIsImM6bWV0YXBsYXRmLU5SZVZwbUxRIiwiYzpjcml0ZW8tUDQ4ZUdUMnciLCJjOmdvb2dsZWlyZS1mZkthUGFSRCIsImM6YWRldmludGEtbW90b3ItbW90b3IiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb2xvY2F0aW9uX2RhdGEiLCJjb211bmljYXItVmN5NkRKV0giLCJ1c29kZWxvcy1RcExwTThqVyIsInRyYW5zZmVyLXRvLW1vdG9yIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyfQ==; euconsent-v2=CQG_4wAQH36sAAHABBENBOFsAP_gAEPgAAiQKiNX_G__bWlr8X73aftkeY1P9_h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3TBIQNlGJDURVCgaogVryDMaEyUoTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vr991dx2B-t7dr83dzyy41Hn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_pE2_eT1l_tWvp7D9-cts7_XW89_fff_9Pn_-uB_-_3_vBUAAkw0KiAMsCQkINAwggQAqCsICKBAAAACQNEBACYMCnYGAS6wkQAgBQADBACAAEGQAIAAAIAEIgAgAKBAABAIFAAGABAMBAAQMAAIALAQCAAEB0DFMCCAQLABIzIiFMCEIBIICWyoQSAIEFcIQizwCIBETBQAAAAAFYAAgLBYHEkgJUJBAlxBtAAAQAIBBAAUIJOTAAEAZstQeDJtGVpgGD5gkQ0wDIAiAA.f_wACHwAAAAA; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.591434.1731262146; notificacionesLiveUltimosCincoMinutos=ZmFsc2U=; _hjSession_774043=eyJpZCI6Ijg3OGMyYWI2LTU0N2ItNGQ5My1iMmMxLTU0ZDMxZjI0MzU3YSIsImMiOjE3MzEyNjIxNTg1NjcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjDonePolls=894300; reese84=3:wzbxndHSqtxJmf/mz+ASlA==:KZoeB1UVbekfYiXarObFOHx3XZBVjUy0A0HkDWY6jxZcS1v9RP8tIyB7kbLcStRjTpyLt6kWTLxljyfOeaXcIBnf216YwN2V9aKQ7GaBf0zr5qu7m9nxScqXETVOp8+Iu0rnMmaYqsLQwZqard4ZughmuzCop55p7XbdZGvFHjT0zjNv9N9Vb2R+ZYrW3fHtCPabAUMgWsqicorPC5TwD/zeKsby8b1sjeofmxdUYJwzhUt4ZnQiibZDyz9bfa6HbHfXjXLUkfUWg6xae/ExjZeVATk9ZMNuX/VS6Wp/51mE8MfCzmPZPCb/qX4uVYAO63fIXBAN0EfOVogXdzFpiuTpu58rnJj7SMLxtEvwpXks1w8+1cqEzXLG3aBddGx+e7M0TXuJTuAQ3firjLulOrznThhtjDI5Th4adHTWvAP+SfgYPgqot1GDT0OtzuJD/K/fstlm1tpLXzEliO2niFgDQIBM9neRVg4dWLR06BusuptXNsuhDHqBBCQzT7kQrnI2D0EVojovm4YO8oOYsA==:KdSrwjRTRuhOjkDVadcaLBUj2fYyZgE5l/Jql4T/kCc=; __utmt=1; __utmb=22935970.7.10.1731262133; AWSALB=5DL2hwVbf3JjfePjTZnv72GdssFpcvPsG0L7Gc8haW0hCNO8jSXiUuqFCx5bEyalhOyvqC3oWgf9IkONQfvVYOp50MvTVRFKBIWlaI5MY8Jk5swpRCNPc8W/yMYG; AWSALBCORS=5DL2hwVbf3JjfePjTZnv72GdssFpcvPsG0L7Gc8haW0hCNO8jSXiUuqFCx5bEyalhOyvqC3oWgf9IkONQfvVYOp50MvTVRFKBIWlaI5MY8Jk5swpRCNPc8W/yMYG; __gads=ID=a7d0de6ad1d0a4aa:T=1729799059:RT=1731263862:S=ALNI_MbhsFJgqoPTX9mfSt-v_W4LUbjV8Q; __gpi=UID=00000f51e44fe2de:T=1729799059:RT=1731263862:S=ALNI_MZHb7rHXeVs_NJSKukbaOf8Xe0tyA; __eoi=ID=abcbeb0032f82513:T=1729799059:RT=1731263862:S=AA-AfjaVBXPdeYVq0vdWosNsGn7r; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222025-11-10T18%3A37%3A45.824Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Wa9ge5ANQl7QsMtzGSoG%22%2C%22expiryDate%22%3A%222025-11-10T18%3A37%3A45.828Z%22%7D'''
headers = {
    "User-Agent": str(useragent),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "es-ES,es;q=0.9,ca-ES;q=0.8,ca;q=0.7,en;q=0.6,fr;q=0.5",
    #"Cookie": cookie,
    "Accept-Encodning":"gzip, deflate, br, zstd",
    "Cache-Control":"max-age=0",
    "Connection" : "keep_alive",
    "Upgrade-Insecure-Requests":"1"
}


"""
import scrapy

class ListingSpider(scrapy.Spider):
    name = 'listing_spider'
    allowed_domains = ['habitaclia.com']  # or other relevant domain
    start_urls = ['https://www.habitaclia.com/viviendas-barcelona.html']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_DELAY': 2,  # adds a delay between requests to avoid rate limiting
        'CONCURRENT_REQUESTS': 2,  # limit the number of concurrent requests
        'ROBOTSTXT_OBEY': True,  # Respect robots.txt settings
        'COOKIES_ENABLED': False,  # If you don't need cookies for each request
    }

    def parse(self, response):
        listings = response.css('.listing-class')  # Replace with the correct selector
        for listing in listings:
            link = listing.css('a::attr(href)').get()  # Adjust as needed
            title = listing.css('a::text').get()  # Adjust as needed
            yield {
                'link': link,
                'title': title
            }

"""
# Make the request
#response = requests.get(url, headers=headers)

response = session.get(url)
response.html.render()

# Check response status
if response.status_code == 200:
    #print (response.text)
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')
    print (soup.prettify())

    # Find all property listing items
    listings = soup.find_all('article', class_="js-list-item list-item-container js-item-with-link gtmproductclick")

    # Extract data for each property
    print("*" * 50)

    for listing in listings:
        # Get the property title
        link = listing.get("data-href")
        print(link)


        ahref = listing.get("a href")
        title = ahref["title"]
        print(title)

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
    print('Failed to retrieve the webpage. Status code:',
          response.status_code)
