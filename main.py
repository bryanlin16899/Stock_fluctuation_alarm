import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "DH40O164TFMIFCWS"
NEWS_API_KEY = "eac758f36bd5438fbb52614272b68601"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

time = datetime.date.today()
y_day = time - datetime.timedelta(days=1)
b_y_day = y_day - datetime.timedelta(days=1)

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()
y_price = float(data["Time Series (Daily)"][f"{y_day}"]["4. close"])
b_y_price = float(data["Time Series (Daily)"][f"{b_y_day}"]["4. close"])
diff_abs = abs(y_price - b_y_price)
percentage = (diff_abs / y_price)*100
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then int("Get News").
if percentage > 5:

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



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

