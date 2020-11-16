import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


# define user-agent
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Pragma': 'no-cache',
    'Referrer': 'https://google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


url_list = []
for i in range(1,6101,100): #until 6001
    url_list.append(i)

#url_list = [1,101]

# create an empty pd dataframe
movie_budget= pd.DataFrame()

for x in url_list:
    url = "https://www.the-numbers.com/movie/budgets/all/{}".format(x)
    page = requests.get(url, headers).text
    soup = bs(page, "lxml")
    table = soup.find_all('table')
    df = pd.read_html(str(table))[0]
    df = pd.DataFrame(df)
    df = df.loc[:, ["Movie","ProductionBudget","DomesticGross","WorldwideGross"]] #select needed columns

    movie_budget= pd.concat([movie_budget, df], ignore_index=True)

#clean up df
movie_budget = movie_budget.sort_values(by='ProductionBudget', ascending=False)
movie_budget = movie_budget.apply(lambda x: x.str.replace(',','')) #remove commas
movie_budget = movie_budget.apply(lambda x: x.str.replace('$','')) #remove $ sign
movie_budget.columns = [x.lower() for x in movie_budget.columns]

#export as csv
movie_budget.to_csv('movie_budget.csv',
             encoding='utf-8', index=False)
