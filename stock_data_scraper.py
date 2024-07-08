import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def scrape(stock,exchange):
    home_url =f'https://eoddata.com/stockquote/{exchange}/'   #The URL Address of the webpage we will scrape, i.e. Stocks starting from A
    stock_url = f'{home_url}{stock}.htm'

    response = requests.get(stock_url)      #requests.get()
#     print(response.status_code)

    page_contents = response.text

    doc = BeautifulSoup(page_contents, 'html.parser')  #Now 'doc' contains entire html in parsed format

    tabels = doc.find_all('table')
    table_rows = tabels[7].find_all('tr')
    
    headers = table_rows[0]
    keys = [i.string.lower() for i in headers.find_all('th')]
    keys = keys[0:-1]
    
    row = table_rows[1].find_all('td')
    values = [i.string for i in row]
    values = values[0:-1]
    
    data = dict(zip(keys,values))
    data['date'] = datetime.strptime(data['date'], '%m/%d/%y').strftime('%Y-%m-%d')
    data['open'] = float(data['open'])
    data['high'] = float(data['high'])
    data['low'] = float(data['low'])
    data['close'] = float(data['close'])
    data['volume'] = int(data['volume'].replace(',', ''))
    
    return(data)


if __name__ == '__main__':
    # while True:
    stock = 'AMZN'
    exchange = 'NASDAQ'
    print(scrape(stock,exchange))
    
