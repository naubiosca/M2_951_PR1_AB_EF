import pandas as pd
import re
import time
import requests
from bs4 import BeautifulSoup

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
    t0 = time.time()
    response = session.get(url+str(page))
    delay = time.time()-t0
    time.sleep(2 * delay)
    print('While slept')

    # Check response status
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        signoff = soup.find("div", class_="signoff")
        if signoff:
            print("No more results found")
            print(links)

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

    # Get the HTML from the link
    response = session.get(link)

    # Sleeps for 10 times the estimated delay
    delay = time.time()-t0
    time.sleep(2 * delay)
    print('Just slept')

    # Check response status
    if response.status_code == 200:
        # # Parse the page content
        # soup = BeautifulSoup(response.content, 'html.parser')
        # title = soup.find('h1', class_='title').text
        # section = soup.find('div', class_='section').text
        # container1 = soup.find('div', class_='inner')
        # ingredients = container1.text.replace('Ingredients','').strip()
        # container2 = container1.find_next('div', class_='inner')
        # steps = container2.text.replace('Elaboració','').strip()
        # recipes = recipes
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='title').text
        section = soup.find('div', class_='section').text
        container1 = soup.find('div', class_='inner')
        ingredients = container1.text.replace('Ingredients','').strip()
        container2 = container1.find_next('div', class_='inner')
        instructions = container2.text.replace('Elaboració','').strip()
        try:
            variations = soup.find(string=re.compile('Variacions')).\
                find_next('div', class_='content-panel').text.strip()
        except:
            pass
        nutrition_information = {}
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
        try:
            table_mn = table_in.find_next('table')
            headers = [th.get_text(strip=True) for th in table_mn.\
                       find_all('tr')[0].find_all('td')]
            print('hello')
            for row in table_mn.find_all('tr')[1:]:
                # Find all data for each column
                cols = [td.get_text(strip=True) for td in row.find_all('td')]
                nutrition_information[cols[0]] = {headers[1]:cols[1],
                                                  headers[2]:cols[2]}
        except:
            pass
        print(nutrition_information)
        df1 = pd.DataFrame({'Title':[title],
                           'Section':[section],
                           'Ingredients':[ingredients],
                           'Instruction':[instructions],
                           'Variations':[variations],
                           'Nutrition Information':[nutrition_information]})
        df = pd.concat([df,df1])
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

with open('/Users/eferr/Downloads/csv_data.csv', 'w') as csv_file:
    csv = df.to_csv(path_or_buf=csv_file, index=False)
