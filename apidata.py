import requests
import pandas as pd
import json

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=&base=USD"
payload = {}
headers= {
  "apikey": {apikey}
}
response = requests.get(url, headers=headers, data=payload).text
result = json.loads(response)
dataframe = pd.DataFrame(result,columns=['rates'])
dataframe.to_csv('./datasource/exchange_rates_1.csv')
