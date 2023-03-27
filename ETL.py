import glob
import pandas as pd
import datetime
targetfile = './bank_market_cap_gbp.csv'
logfile = './log.txt'
#LOGGING
def log(message):
    format = '%d-%m-%Y %H:%M:%S'
    now = datetime.datetime.now()
    timestamp = now.strftime(format)
    with open(logfile,'a') as f:
        f.write(f'{message}, {timestamp}\n')

#Extract
def extract_json(file):
    dataframe = pd.read_json(file)
    return dataframe
def extract():
    extracted_data = pd.DataFrame(columns=['Name','Market Cap (US$ Billion)'])
    for i in glob.glob('datasource/*json'):
        extracted_data = extracted_data.append(extract_json(i),ignore_index=True)
    return extracted_data

#Transform
exrate = pd.read_csv('./datasource/exchange_rates_1.csv',index_col=0) #to have currencies name as the index // before, the index is index's number
exchange_rate = exrate.loc['GBP','rates']
def transform(file):
    file['Market Cap (US$ Billion)'] = file['Market Cap (US$ Billion)'] * exchange_rate
    file.rename({'Market Cap (US$ Billion)':'Market Cap (GBP$ Billion)'},axis=1,inplace=True)
    return file

#Load
def load(source,target):
    source.to_csv(target,index=False) #if not set index=False // when call this file, you have to set index_col=0 since it will have various of index

#RUN ETL
log("ETL Job Started")
log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
log("Transform phase Started")
transformed = transform(extracted_data)
log("Transform phase Ended")
log("Load phase Started")
load(transformed,targetfile)
log("Load phase Ended")
log("ETL Job Ended")