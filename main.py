import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "DH40O164TFMIFCWS"
NEWS_API_KEY = "eac758f36bd5438fbb52614272b68601"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "AC54eaf9f436c566420931df8dbbb038a8"
TWILIO_AUTH_TOKEN = "0d8456dcb3755e650a5a8e30dc22bd29"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
y_data = data_list[0]
y_price = float(y_data["4. close"])

b_y_data = data_list[1]
b_y_price = float(b_y_data["4. close"])
diff = y_price - b_y_price
up_down = None
if diff > 0:
    up_down = "Up"
else:
    up_down = "Down"
percentage = round((diff / y_price)*100)

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

if abs(percentage) > 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    data = news_response.json()
    top3_news = data["articles"][0:3]
    news_list = [ f"{STOCK_NAME}: {up_down}{percentage}Hedaline: {article['title']}. \nBrief: {article['description']}" for article in top3_news]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in news_list:
        message = client.messages.create(
            body=article,
            from_="+13603287144",
            to="+886972988302"
        )

