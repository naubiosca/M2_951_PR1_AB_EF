#%% Installs
'''
%pip install pandas
%pip install codetiming
%pip install requests
%pip install bs4
'''

#%% Imports
import pandas as pd
import re
import time
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry
from fake_useragent import UserAgent


#%% Class definition
class Scraper:
    def __init__(self, domain='https://www.cuinacatalana.eu', route='/ca/pag/receptes/?s=&pag='):
        print("Initializing scraper")
        self.data = pd.DataFrame()
        self.links = []
        self.delay = 0.1
        self.domain = domain
        self.route = route
        self.url = f"{self.domain}{self.route}"
        self.retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
        self.session = requests.Session()
        self.session.cookies.set('sessionid', '9423')
        user_agent = UserAgent().random
        self.session.headers.update({
            'User-Agent': user_agent})
        print(f"User-Agent:",user_agent)
        self.session.mount('https://', HTTPAdapter(max_retries=self.retries))

    def __pull_html(self):
        print(f"Pulling html{self.url}")
        try:
            response = self.session.get(self.url, timeout=5)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None

    def __get_links(self):
        print("PUlling links")
        page = 0
        while True:
            response = self.__pull_html()
            if response is None:
                break
            
            time.sleep(2 * self.delay)
            
            soup = BeautifulSoup(response.content, 'html.parser')
            signoff = soup.find("div", class_="signoff")
            if signoff:
                print("No more results found")
                break

            listings = soup.find_all("h2")
            for listing in listings:
                a_tag = listing.find("a")
                if a_tag and a_tag.get("href"):
                    self.links.append(a_tag.get("href"))

            page += 1
            self.url = f"{self.domain}{self.route}{page}"
            
    def get_content(self):
        self.__get_links()
        print(self.links)
        for link in self.links:
            print("Pulling content")
            self.url = f"{link}"
            response = self.__pull_html()
            if response is None:
                continue
            time.sleep(2 * self.delay)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.find('h1', class_='title').text.strip()\
                    if soup.find('h1', class_='title') else ''
                section = soup.find('div', class_='section').text.strip()\
                    if soup.find('div', class_='section') else ''
                container1 = soup.find('div', class_='inner')
                ingredients = container1.text.replace('Ingredients', '')\
                    .strip() if container1 else ''
                container2 = container1.find_next('div', class_='inner')\
                    if container1 else None
                instructions = container2.text.replace('Elaboració', '')\
                    .strip() if container2 else ''
                
                variations = ''
                try:
                    variations = soup.find(string=re.compile('Variacions'))\
                        .find_next('div', class_='content-panel').text.strip()
                except AttributeError:
                    pass
                
                nutrition_information = {}
                # Check if the first table containing nutrition information
                # exists
                try:
                    table_in = soup.find(string=re.compile('Informació nutricional')).\
                    find_next('table')

                    headers = [th.get_text(strip=True) for th in table_in.\
                            find_all('tr')[0].find_all('td')]

                    for row in table_in.find_all('tr')[1:]:
                        # Find all data for each column
                        cols = [td.get_text(strip=True) for td in row.find_all('td')]
                        nutrition_information[cols[0]] = {headers[1]:cols[1],
                                                        headers[2]:cols[2]}
                except:
                    pass

                # Check if the second table containing nutrition information
                # exists        
                try:
                    table_mn = table_in.find_next('table')
                    headers = [th.get_text(strip=True) for th in table_mn.\
                            find_all('tr')[0].find_all('td')]
                    for row in table_mn.find_all('tr')[1:]:
                        # Find all data for each column
                        cols = [td.get_text(strip=True) for td in row.find_all('td')]
                        nutrition_information[cols[0]] = {headers[1]:cols[1],
                                                        headers[2]:cols[2]}
                except:
                    pass

                df1 = pd.DataFrame({
                    'Title': [title],
                    'Section': [section],
                    'Ingredients': [ingredients],
                    'Instruction': [instructions],
                    'Variations': [variations],
                    'Nutrition Information': [nutrition_information]
                })
                self.data = pd.concat([self.data, df1], ignore_index=True)
            else:
                print('Failed to retrieve the webpage. Status code:', response.status_code)

