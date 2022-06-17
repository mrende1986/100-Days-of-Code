import requests
from datetime import datetime, timedelta
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

MY_API = "STOCK_API"
my_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':MY_API,
}

NEWS_API = "NEWS_API"
NEWS_PARAMS = {
    'q':COMPANY_NAME,
    'apiKey':NEWS_API,
}

account_sid = "TWILIO INFORMATION"
auth_token = "TWILIO INFORMATION"

response = requests.get('https://www.alphavantage.co/query',params=my_params)
apple = response.json()

todays_date = datetime.now()
todays_date = str(todays_date.date())

today_close = apple['Time Series (Daily)'][todays_date]['4. close']
print(f"Today Close: {today_close}")

yesterday_date = datetime.today() - timedelta(days=1)
yesterday_date = str(yesterday_date.date())

yesterday_close = apple['Time Series (Daily)'][yesterday_date]['4. close']
print(f"Yesterday Close: {yesterday_close}")

diff = float(yesterday_close) - float(today_close)
up_down = None
if diff > 0 :
    up_down = '☝🏻'
else:
    up_down = '📉'
print(f"Difference: {diff}")


diff_percent = round((diff / float(yesterday_close)) * 100,2)
print(f"Diff Percent: {diff_percent}")


if abs(diff_percent) > 5:
    news_response = requests.get('https://newsapi.org/v2/everything',params=NEWS_PARAMS)
    apple_news_data = news_response.json()['articles']
    three_articles = apple_news_data[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=article,
            from_="ENTER TWILIO PHONE NUMBER HERE",
            to="ENTER YOUR PHONE NUMBER HERE"
        )
        print(message.status)