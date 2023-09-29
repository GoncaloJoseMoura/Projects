# Get today date

import pandas as pd
import requests


start = '01/03/2019'
end = '9/06/2019'

daterange = pd.date_range(start= start, end=end)
loop = [date.strftime('%Y-%m-%d') for date in daterange]
dates = []
base_currency = [] 
rate = []

for item in loop:
    url = 'https://api.exchangerate.host/{}'.format(item)
    params = {
            "base": 'EUR'
        }
    response = requests.get(url, params = params).json()
    dates.append(response['date'])
    rate.append(response['rates']['INR'])

df = pd.DataFrame({'Date': dates, 'Rate': rate})
df['Base'] = 'EUR'
df['Rate_currency'] = 'INR'

df.to_csv('/DataBase/conversion.csv', index=False)
