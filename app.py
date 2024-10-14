from flask import Flask, render_template, request, jsonify
import pyttsx3
import datetime
import webbrowser

app = Flask(__name__)

# Initialize the speech engine
engine = pyttsx3.init()

# Set properties for the voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Select the voice (0 for male, 1 for female)

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def tell_time():
    """Function to tell the current time."""
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"The current time is {current_time}"

def tell_date():
    """Function to tell the current date."""
    today = datetime.datetime.today().strftime("%B %d, %Y")
    return f"Today's date is {today}"

def search_web(query):
    """Function to search the web."""
    url = f"https://www.google.com/search?q={query}"
    return url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    response = ""
    
    if "hello" in command:
        response = "Hello! How can I assist you today?"
    elif "time" in command:
        response = tell_time()
    elif "date" in command:
        response = tell_date()
    elif "search" in command:
        query = command.replace("search", "").strip()
        response = search_web(query)
    else:
        response = "I didn't catch that. Please try again."
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

