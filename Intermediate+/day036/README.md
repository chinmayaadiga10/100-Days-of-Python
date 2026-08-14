# 📈 Day 36 - Stock Trading News Alert

A Python automation project that monitors **NVIDIA (NVDA)** stock price movement and sends an email containing the latest company news when the stock price changes by more than **5%**.

---

## 🚀 Features

- Fetches daily NVIDIA stock data using the Alpha Vantage API
- Compares the latest two closing prices
- Calculates the percentage change
- Detects whether the stock moved by more than 5%
- Determines whether the stock price increased or decreased
- Fetches the latest 3 NVIDIA news articles
- Sends the stock movement and news through email
- Uses environment variables to store API keys and email credentials

---

## 🛠️ Concepts Used

- REST APIs
- `requests`
- JSON data
- API parameters
- `smtplib`
- `python-dotenv`
- Environment variables
- Functions
- HTTP status codes
- `raise_for_status()`
- Percentage calculations
- String formatting
- Conditional statements

---

## 🔄 How It Works

```text
Alpha Vantage API
       ↓
Get daily stock prices
       ↓
Compare latest 2 closing prices
       ↓
Calculate percentage change
       ↓
Is change > 5%?
    ↙        ↘
  No          Yes
  ↓            ↓
No email    Get latest news
                 ↓
          Create email content
                 ↓
             Send email

```

## 📖 What I Learned

- Working with multiple APIs in a single Python project
- Fetching and processing stock market data
- Calculating percentage changes between stock prices
- Using conditional logic to trigger actions
- Fetching news articles using an API
- Sending automated emails using SMTP
- Using .env files to keep API keys and credentials secure
- Combining data from different APIs into a useful automation workflow

---

⭐ Part of my **100 Days of Python** journey.
