# AI-CRM-PROJECT
Sare 👍 final ga **clean & simple README** ivvanu — copy paste chesi use cheyyachu 👇

---

# 🏥 AI CRM - Doctor Interaction System

## 📌 Overview

This project is an AI-based CRM system for managing doctor interactions.
Users can enter interaction notes, and the system generates an AI summary and stores it for future reference.

---

## 🚀 Features

* Add doctor interaction notes
* Generate AI summary
* View interaction history
* Edit records
* Delete records

---

## 🛠️ Tech Stack

* Frontend: React.js
* Backend: FastAPI (Python)
* Database: SQLite
* AI: Groq API

---

## 📂 Project Structure

backend/

* main.py
* agent.py
* db.py
* models.py
* tools.py

frontend/

* src/
* public/
* package.json

---

## ⚙️ Setup

### Backend

```bash id="b1a2c3"
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Create `.env` file:

```id="d4e5f6"
GROQ_API_KEY=your_api_key_here
```

---

### Frontend

```bash id="g7h8i9"
cd frontend
npm install
npm start
```

---

## 🌐 Usage

1. Enter doctor name
2. Add notes
3. Click Submit
4. View AI summary
5. Check history

---

## 🔐 Note

API key is stored in `.env` file and not uploaded to GitHub.

---

## 👩‍💻 Author

Yamuna

