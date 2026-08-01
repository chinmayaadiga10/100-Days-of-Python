# 📧 Day 32 - Email Automation

This day's work includes two Python automation projects using **SMTP** and the **datetime** module:

- **Monday Motivation** – Automatically sends a motivational quote every Monday.
- **Automated Birthday Wisher** – Sends personalized birthday emails using templates and a CSV file of birthdays.

These projects are part of **Day 32** of the **100 Days of Code: Python Bootcamp**.

---

## 📂 Project Structure

```text
day032/
│── monday_motivation/
│   ├── main.py
│   └── quotes.txt
│
│── automated_birthday_wisher/
│   ├── main.py
│   ├── birthdays.csv
│   └── letter_templates/
│       ├── letter_1.txt
│       ├── letter_2.txt
│       └── letter_3.txt
│
└── README.md
```

---

## 🚀 Features

### Monday Motivation

- Sends a motivational quote via email every Monday
- Selects a random quote from a text file
- Uses the `datetime` module to check the current day
- Sends emails using Python's SMTP library

### Automated Birthday Wisher

- Reads birthdays from a CSV file
- Checks if today matches a birthday
- Selects a random birthday letter template
- Personalizes the letter with the recipient's name
- Sends the birthday email automatically

---

## 🛠️ Concepts Used

- SMTP (`smtplib`)
- Email Automation
- Datetime Module
- File Handling
- CSV Files
- Random Module
- String Manipulation
- Environment Variables

---

## 📖 What I Learned

- Sending emails using Python
- Working with SMTP servers
- Using the `datetime` module for scheduling tasks
- Reading and processing CSV files
- Automating repetitive tasks with Python
- Generating personalized emails from templates

---

⭐ Part of my **100 Days of Python** journey.
