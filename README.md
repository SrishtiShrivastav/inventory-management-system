# 📦 Inventory Management System

## 📖 About

This is a simple Inventory Management System built using FastAPI.

## 🚀 Features

* Add items
* View items
* Delete items
* Uses SQLite database

## 🛠 Tech Stack

* FastAPI
* SQLAlchemy
* SQLite

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📍 API Documentation

After running, open:
http://127.0.0.1:8000/docs

## 📂 Project Structure

```
app/
 ├── database/
 ├── models/
 ├── routers/
 ├── schemas/
 ├── services/
main.py
requirements.txt
