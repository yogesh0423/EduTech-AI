# 🎓 EduTech AI – Personalized Learning Intelligence Platform

> An AI-powered Personalized Learning Intelligence Platform that leverages Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), Semantic Search, and NLP to deliver personalized tutoring, intelligent question answering, automated assessments, and adaptive learning experiences.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

---

## 📖 Overview

EduTech AI is an intelligent learning platform that transforms traditional educational content into an interactive AI-powered learning experience.

Instead of manually searching through notes, PDFs, or recorded lectures, students can simply ask questions in natural language and receive accurate, citation-aware answers generated using a Retrieval-Augmented Generation (RAG) pipeline.

The platform also aims to provide AI-generated quizzes, personalized learning recommendations, progress analytics, and an intelligent tutoring experience.

---

# ✨ Features

### 🤖 AI Tutor
- Context-aware question answering
- Personalized tutoring
- Follow-up conversations
- Citation-aware responses

### 📚 Knowledge Base
- PDF Upload
- Lecture Notes
- Research Papers
- Video Lecture Processing
- Semantic Search

### 🧠 RAG Pipeline
- Whisper Speech-to-Text
- Document Chunking
- Metadata Extraction
- Vector Embeddings
- Semantic Retrieval
- Prompt Engineering

### 🎓 Learning Features
- AI Quiz Generation
- Personalized Learning Paths
- Performance Analytics
- Study Recommendations
- Progress Tracking

### 🔐 Authentication
- JWT Authentication
- Role-Based Access
- Student Dashboard
- Faculty Dashboard
- Admin Dashboard

---

# 🏗️ System Architecture

```
                      User
                        │
                        ▼
                React Frontend
                        │
                        ▼
                 FastAPI Backend
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
 Authentication     AI Services     PostgreSQL
                        │
                        ▼
                  RAG Pipeline
                        │
        ┌───────────────┼───────────────────┐
        ▼               ▼                   ▼
 Whisper STT     Chunking Pipeline     Metadata
                        │
                        ▼
                 Vector Embeddings
                        │
                        ▼
                 Semantic Retrieval
                        │
                        ▼
                    Prompt Builder
                        │
                        ▼
                  Large Language Model
                        │
                        ▼
                  AI Generated Answer
```

---

# 🛠️ Tech Stack

## Frontend

- React.js
- Tailwind CSS
- Axios
- React Router

## Backend

- FastAPI
- Python
- REST APIs
- JWT Authentication

## AI & NLP

- OpenAI Whisper
- LangChain
- OpenAI GPT
- Sentence Transformers
- HuggingFace
- Retrieval-Augmented Generation (RAG)

## Database

- PostgreSQL
- ChromaDB
- FAISS
- Redis (Planned)

## Libraries

- Pandas
- NumPy
- PyMuPDF
- PDFPlumber
- Joblib
- Scikit-learn

---

# 📂 Project Structure

```
EduTech-AI/

│── frontend/
│── backend/
│── rag/
│── embeddings/
│── uploads/
│── transcripts/
│── vector_db/
│── datasets/
│── notebooks/
│── docs/
│── requirements.txt
│── README.md
```

---

# 🚧 Development Progress

| Module | Status |
|---------|--------|
| 📋 Project Planning & Requirements | ✅ Completed |
| 🏗️ System Architecture Design | ✅ Completed |
| 🛠️ Project Setup | ✅ Completed |
| 🎥 Video to Text Transcription (Whisper) | ✅ Completed |
| 🌐 Video Translation & Transcription | ✅ Completed |
| 📄 JSON Transcript Generation | ✅ Completed |
| ✂️ Document/Video Chunking | ✅ Completed |
| 🏷️ Metadata Extraction | ✅ Completed |
| 🧠 Embedding Generation | ✅ Completed |
| 📦 Bulk Embedding Storage | ✅ Completed |
| 🔍 Semantic Similarity Search | ✅ Completed |
| 💾 Embedding Persistence | ✅ Completed |
| 📊 Retrieval Analysis | ✅ Completed |
| 🤖 RAG Prompt Engineering | ✅ Completed |
| 💬 LLM Response Generation | ✅ Completed |
| 📚 README Documentation | 🚧 In Progress |
| 👤 Authentication | ⬜ Planned |
| 📁 Multi-document Upload | ⬜ Planned |
| 🤝 Multi-Agent AI | ⬜ Planned |
| 📝 AI Quiz Generator | ⬜ Planned |
| 📈 Learning Analytics | ⬜ Planned |
| 🎯 Personalized Recommendations | ⬜ Planned |
| 👨‍🎓 Student Dashboard | ⬜ Planned |
| 👨‍🏫 Faculty Dashboard | ⬜ Planned |
| 🛡️ Admin Dashboard | ⬜ Planned |
| 🐳 Docker Deployment | ⬜ Planned |
| ☁️ Cloud Deployment | ⬜ Planned |

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/EduTech-AI.git

cd EduTech-AI
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn main:app --reload
```

## Run Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🎯 Future Roadmap

- Multi-Agent AI
- AI Flashcard Generator
- Voice-based AI Tutor
- AI Assignment Evaluation
- Personalized Study Plans
- AI Coding Tutor
- Real-time Chat
- OCR Support
- Mobile Application
- Gamification
- Docker Deployment
- Kubernetes Support
- CI/CD Pipeline
- AWS Deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Yogesh Patil**

Bachelor of Artificial Intelligence & Data Science

---

## ⭐ If you found this project helpful, don't forget to give it a Star!
