# ChatFriend 🧸💬

**ChatFriend** is a friendly, animated AI chatbot powered by **FastAPI** and **Mistral-7B-Instruct via Ollama**.
It runs **locally** and requires **no API keys** — *free of cost hehe ;>* 🎉

---

## ✨ Features

*  **Local AI responses** using open-source LLM (Mistral-7B-Instruct via Ollama)
*  **Profanity filter** with `better_profanity` (ensures sweet & respectful chats)
*  **Whimsical HTML/CSS frontend** with avatars, animations, and speech bubbles
*  **FastAPI backend + JS frontend** for smooth async communication

---

## 🛠 Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* HTML / CSS / JavaScript
* [Mistral-7B-Instruct via Ollama](https://ollama.com/)

---

## 📁 Folder Structure

```
ChatFriend/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── index.html
└── README.md
```

---

## Run Locally

### 1️⃣ Backend (FastAPI + Ollama):

Make sure you have **Python 3.9+** and **[Ollama](https://ollama.com/)** installed with **Mistral** pulled.

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --port 5003
```

To pull and run the model in Ollama:

```bash
ollama pull mistral:7b-instruct
ollama run mistral:7b-instruct
```

---

### 2️⃣ Frontend:

Just open the file in your browser:

```bash
cd frontend
start index.html
```

Or simply drag and drop `index.html` into your browser window.

---

## Model Used

* **Mistral-7B-Instruct** (via Ollama)
* Works **100% offline** after setup
* No OpenAI or third-party APIs involved

---

## Screenshots

>

---

## Author 

Made with love by **Ishita Pradhan**
Let’s build fun, free, and friendly AI ✨

---

## Credits

* Images: [Unsplash ](https://unsplash.com/)
* Mistral Model: [Mistral AI](https://mistral.ai/)
* Chat UI design inspired by classic messenger themes 💌

> All visual assets are used for non-commercial, educational, or placeholder use only.

---

## 🔒 License

This project is **private and not licensed for redistribution or commercial use**.
Please **do not copy, clone, or distribute** without permission.

---
