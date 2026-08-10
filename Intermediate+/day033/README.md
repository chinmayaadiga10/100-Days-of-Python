# 🛰️ Day 33 - APIs & GUI Projects

Day 33 contains two Python projects focused on working with **APIs**, processing JSON data, and building a simple GUI with **Tkinter**.

### Projects

- 🛰️ **ISS Overhead Tracker** — Checks whether the ISS is near your location at night and sends an email notification.
- 💬 **Kanye Quotes** — Fetches a random Kanye West quote from an API and displays it in a Tkinter GUI.

---

## 📂 Project Structure

```text
.
└── day033/
    ├── main.py
    ├── satellite_detection.py
    ├── kanye-quotes-project/
    │   ├── kanye_quotes.py
    │   ├── background.png
    │   └── kanye.png
    └── README.md
```

---

## 🛰️ ISS Overhead Tracker

- Fetches the current ISS position using an API
- Checks whether the ISS is close to your location
- Checks whether it is currently nighttime
- Sends an email notification when the ISS is overhead

### Concepts Used

- APIs
- `requests`
- JSON data
- `datetime`
- Conditional logic
- `smtplib`
- Functions

---

## 💬 Kanye Quotes

A simple Tkinter application that retrieves a random quote from the **Kanye REST API** and displays it in a graphical interface.

### Features

- Tkinter GUI
- Random quote generation
- API requests
- Displays fetched quote on the screen
- Button-based interaction

### Concepts Used

- Tkinter
- APIs
- `requests`
- JSON
- Functions
- Event handling

---

## 📖 What I Learned

- Making API requests using Python
- Working with JSON responses
- Using API data inside a GUI
- Combining APIs with existing Python applications
- Sending automated emails
- Handling user interaction with Tkinter

---

⭐ Part of my **100 Days of Python** journey.
