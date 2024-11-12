from scraper_6 import Scraper

# Usage
def main():
#%% Run Scraper
    s = Scraper()
    #breakpoint()
    s.get_content()
    #%% Explore DataFrame
    s.data
    #%% Save to CSV
    s.data.to_csv('csv_data.csv', index=False)
    print('Data has been saved in csv_data.csv')

if __name__ == "__main__":
    main()