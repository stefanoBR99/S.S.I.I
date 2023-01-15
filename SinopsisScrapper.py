import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

file_path = "MovieLens/linkstest.csv"
HEADERS ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Content-Language': 'es', }

# open the csv file and read the data
with open(file_path, "r") as file:
    data = csv.reader(file)
    next(data)
    # create an empty list to store the plot summary text for each movie
    results = []
    
    # loop through the rows in the csv file
    for row in data:
        try:
            # get the value in the third column
            value = row[2]
            #print(value)
            #link = "https://www.themoviedb.org/movie/" + value
            #response = requests.get(link, headers=HEADERS)
            page = requests.get(f'https://www.themoviedb.org/movie/' + value + '?language=es-ES', headers=HEADERS )
            soup = BeautifulSoup(page.text, 'html.parser')

            plot_summary_div = soup.find('div', class_='overview')
            plot_summary_text = re.sub('<[^>]*>', '', str(plot_summary_div))
            plot_summary_text = re.sub(',', '', plot_summary_text)
            
            # append the plot summary text to the results list
            results.append(plot_summary_text)
        except:
            results.append("NaN")

# read the csv file into a pandas dataframe
df = pd.read_csv(file_path)


# add a new column called "plot_summary" to the dataframe and insert the results list as the values
df["plot_summary"] = results
#df["plot_summary"] = df["plot_summary"].fillna("NaN")
# write the updated dataframe to a new csv file or overwrite the existing file
df.to_csv("linkstest_new.csv", index=False)
