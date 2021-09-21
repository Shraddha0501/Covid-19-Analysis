#Importing Pandas
import pandas as pd
#Library used to fetch the data from web
import requests                             

#Data collection/scraping from url(wikipedia)
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
request_url = requests.get(url)
#The desired data will be filtered and stored in req_data
req_data = pd.read_html(request_url.text)   
#Data frame is fetched by assigning the variable and index in which it exists
df = req_data[10]                           


#Data cleaning
#Renaming column names
df.columns = ['column0', 'Country name' , 'Total Cases', 'Total Deaths','Total Recoveries','column5']

#Removing unnecessary columns, column0 and column5 in this case from the dataframe
df = df[['Country name' , 'Total Cases', 'Total Deaths','Total Recoveries']]

#Removing irrelevant rows from data, i.e row index 243 and 244(last 2 rows)
rem_index = df.index[-1]
df = df.drop([rem_index,rem_index-1])

#Removing strings inside the brackets in the Country name column and Total Deaths column using regular expression
df['Country name'] = df['Country name'].str.replace('\[.*\]','')
df['Total Deaths'] = df['Total Deaths'].str.replace('+','')

#Replacing 'no data' in Total Recoveries column with 0
df['Total Recoveries'] = df['Total Recoveries'].str.replace('No data','0')

#Changing data type of 'Total Cases', 'Total Deaths','Total Recoveries' to int
df['Total Cases'] = pd.to_numeric(df['Total Cases'])
df['Total Deaths'] = pd.to_numeric(df['Total Deaths'])
df['Total Recoveries'] = pd.to_numeric(df['Total Recoveries'])


#Data Organization
#Exporting data set
#df.to_csv(r'covid19 analysis.csv')
df.to_excel(r'covid19 analysis.xlsx')
