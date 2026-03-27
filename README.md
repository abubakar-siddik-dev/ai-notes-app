# 🧠 AI Smart Notes App

An intelligent note-taking application that automatically generates summaries using AI. Built with FastAPI (backend) and a lightweight frontend, this app helps users save time by summarizing long notes instantly.

---

## 🚀 Live Demo

🌐 Frontend: https://your-frontend.vercel.app  
🔗 Backend API: https://your-backend.onrender.com  

> ⚠️ Update these links after deployment

---

## ✨ Features

- 📝 Add notes  
- 🤖 AI-powered auto summary generation  
- 💾 Save notes with summaries  
- 📋 View all notes  
- ❌ Delete notes  
- ⚡ Fast API performance  

---

## 🛠 Tech Stack

Backend:
- FastAPI (Python)
- SQLAlchemy
- SQLite

AI Integration:
- Hugging Face Inference API (BART model)

Frontend:
- HTML, CSS, JavaScript (simple UI)

---

## 📁 Project Structure

ai-notes-app/

├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt

├── frontend/
│   └── index.html---

## ⚙️ Run Locally

### 🔹 Backend

cd backend
pip install -r requirements.txt
uvicorn main:app --reload👉 Runs on: http://127.0.0.1:8000

---

### 🔹 Frontend

Open frontend/index.html in your browser

---

## 🔗 API Endpoints

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| GET    | /notes/          | Get all notes       |
| POST   | /notes/          | Create note + AI summary |
| DELETE | /notes/{id}      | Delete note         |

---

## 🔑 Environment Setup

To enable AI summary, add your Hugging Face API key:

headers = {
  "Authorization": "Bearer YOUR_HF_API_KEY"
}Get API key from: https://huggingface.co

---

## ☁️ Deployment Guide

### 🔹 Backend (Render)

- Build:
pip install -r requirements.txt- Start:
uvicorn main:app --host 0.0.0.0 --port 10000---

### 🔹 Frontend (Vercel)

- Import repo
- Select frontend folder
- Deploy

---

## ⚠️ Connect Frontend & Backend

Update API URL in frontend:

const API = "https://your-backend.onrender.com";---

## 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=abubakar-siddik-dev&show_icons=true&theme=tokyonight)

---

## 🌟 Future Improvements

- 🔐 User authentication (JWT)
- 🔍 Search & filter notes
- 🎨 React-based UI
- 📱 Mobile responsive design
- 🧠 Advanced AI (GPT integration)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Abu Bakar Siddik  
GitHub: https://github.com/abubakar-siddik-dev
