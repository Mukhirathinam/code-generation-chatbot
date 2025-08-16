Code Generation Chatbot using Python

📌 Project Overview

This project is a Code Generation Chatbot built using Python. It leverages natural language processing (NLP) and machine learning techniques to generate code snippets based on user queries. The chatbot is designed with a Flask-based backend and an interactive frontend UI to provide seamless user interaction.

🚀 Features

💬 Chat-based interface for natural interaction

🧠 AI-powered code generation using transformer-based models

🖥️ Web-based UI for user-friendly access

🔐 User authentication and chat history management

🎤 Speech-to-text (STT) for voice input

🔊 Text-to-speech (TTS) for reading responses aloud

🗄️ MySQL database integration for storing user data, chats, edits, feedback, and favorites

🛠️ Tech Stack

Backend: Python (Flask)

Frontend: HTML, CSS, JavaScript

Database: MySQL

Machine Learning Model: CodeT5 (Base & Advanced versions)

Additional Libraries:

sqlalchemy for ORM

speechrecognition for speech-to-text

pyttsx3 for text-to-speech

transformers for model integration

📂 Project Structure
code_generation_chatbot/
│── app/  
│   ├── static/        # CSS, JS, images  
│   ├── templates/     # HTML templates  
│   ├── models/        # CodeT5 integration  
│   ├── routes/        # Flask routes  
│   ├── utils/         # Helper functions  
│   └── __init__.py    # Flask app setup  
│  
├── config.py          # App configuration  
├── requirements.txt   # Dependencies  
├── README.md          # Project documentation  
└── run.py             # Entry point  

⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/your-username/code_generation_chatbot.git
cd code_generation_chatbot


Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt


Set up MySQL database:

Create a database (e.g., chatbot_db)

Update config.py with your MySQL credentials

Run the application:

python run.py


Open your browser and go to:

http://127.0.0.1:5000

📊 Database Schema

The database stores:

Users (authentication details)

Chats (chat history with timestamps)

Edits (modified code snippets)

Feedback (user feedback for improvements)

Favorites (saved/generated code snippets)
