import bs4
import pandas as pd
import requests

url = 'https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks'
data = requests.get(url).text
soup = bs4.BeautifulSoup(data,'html.parser')
tables = soup.find_all('table')
dataframe = pd.DataFrame(columns=['Name','Market Cap (US$ Billion)'])
for i in tables[2].tbody.find_all('tr'):
    col = i.find_all('td')
    print(col)
    if col!=[]: #there is [] at the beginning, if call 'col[1]' it will out of range
        name = col[1].text
        markcap = float(col[2].text)
        dataframe = dataframe.append({'Name':name,'Market Cap (US$ Billion)':markcap},ignore_index=True)
dataframe.to_json('datasource/bank_market_cap.json')
