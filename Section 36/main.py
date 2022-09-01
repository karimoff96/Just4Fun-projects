import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_API_key = 'API_key'
news_api_key = 'API_key'

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': stock_API_key,
}
news_params = {
    'q': COMPANY_NAME,
    'apikey': news_api_key
}
url = STOCK_ENDPOINT
r = requests.get(url, params=params)
data = r.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]
yesterday_day = data_list[0]
yesterday_closing_price = float(yesterday_day['4. close'])


day_before_yesterday = data_list[1]
before_yesterday_closing_price = float(day_before_yesterday['4. close'])

difference = abs(yesterday_closing_price-before_yesterday_closing_price)
percentage = (difference/yesterday_closing_price)*100
up_down = None
if round(difference, 2)>0:
    up_down = '🔺'
else:
    up_down = '🔻'

if percentage < 1:
    news_url = requests.get(NEWS_ENDPOINT, params=news_params)
    news = news_url.json()['articles']
    latest_news = news[0:3]
    messages = [f"{STOCK_NAME}:{up_down}{round(percentage,2)}%\nHeadline:{a['title']}. \nBrief: {a['description']}" for a in latest_news]

    account_sid = 'Account_sid'
    auth_token = 'Auth tokern'
    client = Client(account_sid, auth_token)
    for message in messages:
        # print(message)
        send = client.messages.create(
            body=message, 
            from_='sender',
            to='reciever')  

