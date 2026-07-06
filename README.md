# LearnMateAI

LearnMateAI is an AI-powered study assistant built with **Python**, **Streamlit**, and the **Groq API**. It provides an interactive web interface where students can ask questions, receive AI-generated explanations, and maintain conversation history throughout their learning session.

The project began as a terminal-based chatbot and was later transformed into a modern web application using Streamlit.

---

## Features

- AI-powered study assistant using Groq Llama 3.3 70B
- Interactive ChatGPT-style chat interface
- Conversation memory throughout the session
- Automatic chat history saving
- Save conversations to a text file
- View complete chat history
- Clear chat while preserving the system prompt
- Session statistics
  - Questions Asked
  - AI Responses
  - Total Messages
- Custom pastel-themed UI
- Gradient background and modern interface
- Responsive sidebar controls
- Typing animation while generating AI responses

---

## Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv
- HTML
- CSS

---

## Project Structure

```
LearnMateAI/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── config.toml
└── assets/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/LearnMateAI.git
```

### Navigate to the project folder

```bash
cd LearnMateAI
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Create a `.env` file

Create a file named `.env` in the project folder and add your own Groq API key.

```text
GROQ_API_KEY=your_groq_api_key
```

> **Note:** Do not upload your `.env` file to GitHub.

### Run the application

```bash
streamlit run app.py
```

---

## How to Use

1. Launch the application.
2. Ask questions about programming, mathematics, AI, university courses, or any topic you'd like to learn.
3. View previous conversations using the History button.
4. Save conversations to a text file.
5. Clear the current conversation.
6. View live session statistics from the sidebar.

---



## Future Improvements

- User authentication
- Multiple chat sessions
- Dark mode
- PDF upload and summarization
- Flashcard generation
- Quiz mode
- Voice input
- Image generation support
- Study planner integration

---

## Author

**Ayesha Nehal**

Built with Python, Streamlit, and the Groq API.

---

## License

This project is intended for educational and learning purposes.
