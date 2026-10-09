import os 
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

parameters = {"function":"TIME_SERIES_DAILY",
              "symbol":STOCK_NAME,
              "apikey":API_KEY,
              }
response = requests.get(url=STOCK_ENDPOINT,params=parameters)

response.raise_for_status()

data = response.json()

date_keys = [key for key, value in data["Time Series (Daily)"].items()]

last_day_data = float(data["Time Series (Daily)"][date_keys[0]]['4. close'])





#TODO 2. - Get the day before yesterday's closing stock price
day_before_data = float(data["Time Series (Daily)"][date_keys[1]]['4. close'])


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diffrence = abs(last_day_data - day_before_data)
# print(diffrence)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = (diffrence /day_before_data ) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage >= 5:
    
        
    parameters = {"apikey":NEWS_API_KEY,
                "q":COMPANY_NAME}


    response1 = requests.get(url=NEWS_ENDPOINT,params=parameters)
    response1.raise_for_status()

    data1 = response1.json()
    data_articles = data1["articles"][0:3]

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    articles = [
        {
            "title": article["title"],
            "description": article["description"]
        }
        for article in data_articles
    ]

    print(articles)

#TODO 9. - Send each article as a separate message via Telegram. 
    for article in articles:
        message = f"""TSLA: {round(percentage,2)}%

    Headline: {article["title"]}

    Brief: {article["description"]}
    """

        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        parameters = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }

        response = requests.post(telegram_url, params=parameters)
        response.raise_for_status()


