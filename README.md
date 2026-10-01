🎓 EduGenie – AI-Powered Learning Assistant

An AI-powered educational assistant designed to help students learn, understand, practice, and improve their academic knowledge using Generative AI.

---

🚀 Project Overview

EduGenie is an AI-powered learning platform that provides personalized educational assistance to students.

The application allows students to ask questions, understand difficult concepts, generate learning content, practice through quizzes, and receive AI-powered study guidance.

EduGenie uses Google Gemini AI to process student queries and generate intelligent, context-aware educational responses.

The main goal of EduGenie is to provide students with an AI-powered personal learning companion that can assist them anytime with their studies.

---

✨ Features

🤖 AI Learning Assistant

Students can interact with the AI assistant and ask questions related to their studies.

The AI assistant can:

- Answer academic questions
- Explain difficult concepts
- Simplify complex topics
- Provide examples
- Give step-by-step explanations
- Clarify student doubts
- Provide revision assistance

---

📚 AI Topic Explanation

Students can enter a subject or topic and receive an AI-generated explanation.

For example:

«"Explain DBMS normalization in simple terms."»

EduGenie generates an understandable explanation with relevant examples.

---

📝 AI Question & Answer

Students can ask questions using natural language.

The system processes the question using AI and generates a relevant response.

Supports:

- Short answers
- Detailed answers
- Step-by-step answers
- Concept-based explanations
- Examples

---

🧠 AI Quiz Generation

EduGenie can generate quizzes based on selected subjects and topics.

Quiz features include:

- Multiple-choice questions
- Topic-based questions
- Practice questions
- AI-generated answers
- Answer explanations
- Difficulty-based questions

---

📖 Study Assistance

EduGenie helps students with their study and examination preparation.

It can provide:

- Important concepts
- Topic summaries
- Revision notes
- Exam preparation guidance
- Practice questions
- Concept explanations
- Study recommendations

---

🎯 Personalized Learning

EduGenie can provide learning assistance based on the student's requirements.

Personalization can be based on:

- Subject
- Topic
- Learning level
- Student questions
- Learning requirements
- Previous interactions

---

🔍 AI-Powered Content Generation

EduGenie can generate educational content using Generative AI.

Possible generated content includes:

- Explanations
- Examples
- Questions
- Quizzes
- Summaries
- Revision material
- Study guidance

---

🛠️ Technology Stack

Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy

AI

- Google Gemini API
- Google GenAI SDK
- Generative AI
- Natural Language Processing

Database

- SQLite
- SQLAlchemy ORM

Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

Development Tools

- Git
- GitHub
- VS Code
- PowerShell
- Python Virtual Environment

---

🏗️ Project Architecture

EduGenie/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── schemas.py
│   ├── gemini_generator.py
│   └── ai_service.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── quiz.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── models/
│
├── services/
│
├── edu-genie-env/
│
├── edugenie.db
├── requirements.txt
├── .gitignore
├── README.md
└── .env

---

🔄 Application Workflow

Student
   │
   ▼
Enter Question / Topic
   │
   ▼
EduGenie Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
AI Request Processing
   │
   ▼
Google Gemini AI
   │
   ▼
AI Generated Response
   │
   ▼
Educational Answer / Explanation
   │
   ▼
Student

---

🧠 AI Workflow

User Input
    ↓
Question Processing
    ↓
Context Understanding
    ↓
Prompt Generation
    ↓
Gemini API
    ↓
Response Generation
    ↓
Educational Response

---

⚙️ Installation

1. Clone the Repository

git clone https://github.com/your-username/EduGenie.git

2. Navigate to the Project

cd EduGenie

3. Create Virtual Environment

python -m venv edu-genie-env

4. Activate Virtual Environment

Windows PowerShell:

.\edu-genie-env\Scripts\Activate.ps1

5. Install Dependencies

pip install -r requirements.txt

---

🔐 Environment Configuration

Create a ".env" file in the project root:

GEMINI_API_KEY=your_gemini_api_key

«⚠️ Never upload your actual API key to GitHub.»

Add ".env" to ".gitignore".

---

▶️ Run the Application

Start the FastAPI server:

uvicorn app.main:app --reload

The application will be available at:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs

---

📦 Requirements

Example "requirements.txt":

fastapi
uvicorn
sqlalchemy
pydantic
python-dotenv
google-genai
jinja2

Install dependencies:

pip install -r requirements.txt

---

🗄️ Database

EduGenie uses SQLite with SQLAlchemy for local data management.

Database:

edugenie.db

The database can store:

- Student information
- Questions
- AI responses
- Quiz data
- Learning history
- Generated educational content

---

🔌 API Endpoints

EduGenie API
│
├── GET  /health
│
├── POST /ask
│      └── Ask an educational question
│
├── POST /explain
│      └── Explain a topic
│
├── POST /quiz
│      └── Generate an AI quiz
│
├── POST /summarize
│      └── Summarize educational content
│
└── GET  /learning
       └── Learning assistance

---

📸 Screenshots

Add project screenshots inside:

screenshots/
│
├── home.png
├── ai-assistant.png
├── question-answer.png
├── quiz.png
└── dashboard.png

Example:

![EduGenie Dashboard](screenshots/dashboard.png)

---

🎯 Project Goals

EduGenie aims to:

- 🎓 Make learning more accessible
- 🤖 Provide AI-powered educational assistance
- 🧠 Simplify difficult concepts
- 📚 Support personalized learning
- 📝 Help students practice through quizzes
- 📖 Support exam preparation
- 🚀 Build an intelligent digital learning companion

---

🔮 Future Enhancements

- 🎙️ Voice-based AI Assistant
- 🌐 Multi-language Learning
- 📱 Android & iOS Application
- 📄 PDF-based Question Answering
- 👨‍🏫 AI Teacher Assistant
- 📝 AI Exam Paper Generator
- 📚 AI Study Plan Generator
- 📊 Advanced Student Analytics
- 🧠 Adaptive Learning
- 🏆 Gamification & Achievements
- 🔔 Smart Study Reminders
- 📈 Student Performance Analytics

---

🔐 Security

The application follows basic security practices:

- Environment-based API keys
- ".env" protection
- Input validation
- Secure API configuration
- Protected application secrets

---

👨‍💻 Developer

Dhayanithi R

Engineering Student | Full Stack Developer | AI/ML Enthusiast

---

🤝 Contributing

Contributions are welcome.

git checkout -b feature/new-feature

git add .
git commit -m "Add new feature"
git push origin feature/new-feature

Then create a Pull Request.

---

📄 License

This project is developed for educational, research, and development purposes.

---

⭐ Support

If you find EduGenie useful, consider giving the repository a ⭐ on GitHub.

---

🎓 EduGenie

Learn Smarter • Understand Better • Grow Faster with AI
