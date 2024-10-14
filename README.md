# Voice Assistant Web Application

This project is a web-based voice assistant built using **Flask** and **pyttsx3** for speech synthesis. It performs tasks such as telling the current time, providing today's date, and searching the web. Users interact with the assistant by sending voice commands through the web interface, which the assistant responds to with either text or actions like searching the web.

## Features

- **Text-to-Speech**: Converts the assistant's responses into speech.
- **Current Time**: Responds with the current time when asked.
- **Current Date**: Provides today's date on request.
- **Web Search**: Performs a Google search based on user queries.
- **Web Interface**: A simple UI to send commands and receive responses.

## Technologies Used

- **Flask**: Backend web framework for Python.
- **pyttsx3**: Text-to-speech conversion library.
- **JavaScript**: For capturing and sending commands asynchronously via the web interface.
- **HTML/CSS**: Basic front-end structure and design.

## Prerequisites

- **Python 3.x**
- **Flask**: Install via pip (`pip install Flask`).
- **pyttsx3**: Install via pip (`pip install pyttsx3`).

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your_username/voice-assistant-web-app.git
   cd voice-assistant-web-app
   ```

2. **Install Dependencies**:

   ```bash
   pip install Flask pyttsx3
   ```

3. **Run the Flask Application**:

   ```bash
   python app.py
   ```

4. **Access the App**: Open a browser and navigate to `http://localhost:5001/` to access the web interface.

## How to Use

1. **Start the Application**: Once the app is running, you can enter the following commands via the web interface:
   - **"hello"**: The assistant will greet you.
   - **"time"**: The assistant will tell you the current time.
   - **"date"**: The assistant will provide today's date.
   - **"search <query>"**: The assistant will perform a Google search based on your query.

2. **JavaScript Interaction**: The command input from the user is sent via JavaScript to the Flask backend, which processes the command and responds accordingly. The results are displayed on the page and may trigger speech synthesis.

## Project Structure

```
/voice-assistant-web-app
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html           # HTML page for the web interface
└── static/
    └── js/
        └── script.js        # JavaScript for handling frontend command input
```

## Example Commands

- **"Hello"**: The assistant will respond with "Hello! How can I assist you today?"
- **"What is the time?"**: The assistant will tell you the current time.
- **"What is the date?"**: The assistant will tell you today's date.
- **"Search Python Flask tutorials"**: The assistant will open a Google search for "Python Flask tutorials."

