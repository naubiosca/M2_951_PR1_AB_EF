import pandas as pd
import re
import time
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Create a session object
session = requests.Session()

# Set default headers
session.headers.update({
    'User-Agent': 'my-app/0.0.1',
    'Authorization': 'Bearer your_token_here'
})

# Set default cookies
session.cookies.set('sessionid', '123456789')

# Initialize variables
url='https://www.cuinacatalana.eu/ca/pag/receptes/?s=&pag='
page=0
links=[]

while True:
    # Initialize timer
    t0 = time.time()

    # Fetch HTML
    response = session.get(url+str(page))

    # Sleep for 2 times the estimated delay
    delay = time.time()-t0
    time.sleep(2 * delay)
    
    # Check response status
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        signoff = soup.find("div", class_="signoff")
        if signoff:
            print("No more results found")
            break  # Break the loop if this message is found

        # Find all listing items
        listings = soup.find_all("h2")
    
        for listing in listings:
            a_tag = listing.find("a")
            if a_tag and a_tag.get("href"):
                links.append(a_tag.get("href"))
   
        page = page + 1
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

df = pd.DataFrame()
for link in links:
    # Initialize timer
    t0 = time.time()


    # Set a number of retries
    #retries = Retry(total=2, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    #session.mount('https://', HTTPAdapter(max_retries=retries))

    # Fetch HTML
    response = session.get(link)

    # Sleep for 2 times the estimated delay
    delay = time.time()-t0
    time.sleep(2 * delay)

    # Check response status
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='title').text
        section = soup.find('div', class_='section').text
        container1 = soup.find('div', class_='inner')
        ingredients = container1.text.replace('Ingredients','').strip()
        container2 = container1.find_next('div', class_='inner')
        instructions = container2.text.replace('Elaboració','').strip()
        # Check if variation section exists
        try:
            variations = soup.find(string=re.compile('Variacions')).\
                find_next('div', class_='content-panel').text.strip()
        except:
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
        
        # Create DataFrame with the recipe data
        df1 = pd.DataFrame({'Title':[title],
                           'Section':[section],
                           'Ingredients':[ingredients],
                           'Instruction':[instructions],
                           'Variations':[variations],
                           'Nutrition Information':[nutrition_information]})
        # Concatenate previous data and new data
        df = pd.concat([df,df1])
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

# Open file in write mode and save the scraped data
with open('csv_data.csv', 'w') as csv_file:
    df.to_csv(path_or_buf=csv_file, index=False)
print(f'Data has been saved in{csv_file.name}')
