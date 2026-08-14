import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = "NVDA"
COMPANY_NAME = "Nvidia Corporation"

STOCK_ENDPOINT = os.getenv("STOCK_URL")
NEWS_ENDPOINT = os.getenv("NEWS_URL")
STOCK_API_KEY = os.getenv("STOCK_KEY")
NEWS_API_KEY = os.getenv("NEWS_KEY")
EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")


def get_news():

    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "language": "en",
        "pageSize": 3,
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    data = response.json()
    return data["articles"][:3]


def send_mail(subject, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        message = f"SUBJECT:{subject}\n\n{body}".encode("utf-8")
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=message)


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}


response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()

stock_prices = data["Time Series (Daily)"]
dates = list(stock_prices)
yesterday = dates[0]
day_before = dates[1]
yesterday_ohlcv = stock_prices[yesterday]
day_before_ohlcv = stock_prices[day_before]
yesterday_closing_price = float(yesterday_ohlcv["4. close"])
day_before_closing_price = float(day_before_ohlcv["4. close"])
delta = abs(yesterday_closing_price - day_before_closing_price)
threshold = 0.05 * day_before_closing_price
percent_change = (delta / day_before_closing_price) * 100

if delta > threshold:
    if yesterday_closing_price > day_before_closing_price:
        arrow = "🔺"
    else:
        arrow = "🔻"
    print("circuit limit")

    articles = get_news()

    subject = f"{STOCK_NAME}: {arrow}{abs(percent_change):.2f}%"

    email_body = f"{STOCK_NAME}: {arrow}{abs(percent_change):.2f}%\n\n"

    for article in articles:
        title = article["title"]
        description = article.get("description", "No description available.")
        email_body += f"Headline: {title}\n" f"Brief: {description}\n\n"
    send_mail(subject, email_body)
    print("Email sent successfully!")

else:
    print("Stock movement less than 5%. No email sent.")
