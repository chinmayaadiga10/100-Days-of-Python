# 🃏 Day 31 - Flash Card App

A desktop flash card application built with **Tkinter** and **Pandas** to help users learn French vocabulary. The app displays French words, automatically flips the card to reveal the English translation after a few seconds, and tracks learning progress by removing known words. This project is part of **Day 31** of the **100 Days of Code: Python Bootcamp**.

---

## 📂 Project Structure

```text
day031/
│── main.py
│── data/
│   ├── french_words.csv
│   ├── words_to_learn.csv
│── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
└── README.md
```

---

## 🚀 Features

- Displays random French words
- Automatically flips the flash card after 3 seconds
- Reveals the English translation
- Marks known words and removes them from future sessions
- Saves progress in `words_to_learn.csv`
- Clean Tkinter-based GUI

---

## 🛠️ Concepts Used

- Tkinter
- Pandas
- DataFrames
- CSV File Handling
- Exception Handling
- Random Module
- Event Scheduling (`after()`)
- Functions

---

## 📖 What I Learned

- Building interactive desktop applications with Tkinter
- Reading and updating CSV files using Pandas
- Persisting user progress between sessions
- Scheduling timed events with `after()`
- Managing application state in a GUI

---

⭐ Part of my **100 Days of Python** journey.
