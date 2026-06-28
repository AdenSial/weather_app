# 🌤️ Weather App (Python)

A simple command-line Weather Application built with **Python** that fetches real-time weather data using the **OpenWeatherMap API**.

This project was created as a beginner-friendly learning project to understand how APIs work, how to make HTTP requests using Python, and how to structure a Python project using virtual environments and Git.

---

## 📌 Features

* Search weather by city name
* Display current temperature
* Show "Feels Like" temperature
* Display humidity
* Show wind speed
* Display weather condition
* Secure API key management using `.env`
* Error handling for invalid city names and network issues

---

## 🛠️ Technologies Used

* Python 3
* Requests
* Python Dotenv
* OpenWeatherMap API
* Git & GitHub

---

## 📂 Project Structure

```
weather-app/
│
├── app.py              # Main application
├── weather.py          # Weather API functions
├── config.py           # Loads API key
├── .env                # Environment variables (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project root and add:

```text
API_KEY=YOUR_OPENWEATHER_API_KEY
```

---

## ▶️ Run the Project

```bash
python app.py
```

Example:

```
========================================
      🌤️ Weather App
========================================

Enter city name: Islamabad

Current Weather
----------------------------------------
📍 City        : Islamabad, PK
🌡 Temperature : 41.02°C
🤗 Feels Like  : 48.02°C
💧 Humidity    : 42%
🌬 Wind Speed  : 3.9 m/s
☁ Condition    : Clear Sky
```

---

## 📚 What I Learned

This project helped me learn:

* Python project structure
* Virtual environments
* Installing packages with pip
* Using the Requests library
* Working with REST APIs
* Handling JSON responses
* Exception handling
* Environment variables using `.env`
* Git and GitHub workflow
* Writing reusable Python functions

---


This project is open-source and available for learning and educational purposes.
