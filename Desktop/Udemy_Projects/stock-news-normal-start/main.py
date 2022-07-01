import requests
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


account_sid= os.environ.get("account_sid")
auth_token= os.environ.get("auth_token")

STOCK_ENDPOINT_API= "NHWLBD907BTBJ1D8"
NEWS_ENDPOINT_API="f555b0c66c324422a8cbe3535baccfba"


tsla_parameters={
"function": "TIME_SERIES_DAILY",
"symbol":STOCK_NAME,
"apikey":STOCK_ENDPOINT_API

}
r = requests.get(STOCK_ENDPOINT,params=tsla_parameters)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]
# print(data)
# print(data["Time Series (Daily)"])
# print(data["Time Series (Daily)"]["2021-12-31"])
# print(data["Time Series (Daily)"]["2021-12-31"]["1. open"])
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#getting data from time series (daily)
data_list=[value for (key,value) in data.items()]

#yesterdays data
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]

#Get day before yesterday closing price
day_before_yesterday_data= data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]

difference= abs(float(yesterday_closing_price) -float(day_before_yesterday_closing_price))
percent_diff= (difference/float(yesterday_closing_price)) * 100



if percent_diff >= 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_ENDPOINT_API,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]


formatted_articles= [f"Headline:  {article['title']}. \n Brief {article['description'] }" for article in articles]

client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages \
        .create(body=article,
                from_="+17067176672",
                to="+15166060942"
                )

print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

