from datetime import datetime
import os
import webbrowser
import openai
import pyttsx3
import speech_recognition as sr
from config import apikey
import psutil  # For managing processes
import pyautogui  # For screen management

chatStr = ""


def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Dhruv: {query}\nJarvis: "
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Use 'gpt-3.5-turbo' or 'gpt-4'
            messages=[
                {"role": "system", "content": "You are a helpful assistant named Jarvis."},
                {"role": "user", "content": chatStr}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        reply = response.choices[0].message["content"]
        chatStr += f"{reply}\n"
        return reply
    except openai.OpenAIError as e:
        print(f"API Error: {e}")
        return "I'm sorry, there was an issue processing your request."



def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = openai.ChatCompletion.create(  # Corrected here
            model='gpt-3.5-turbo',  # Use 'gpt-3.5-turbo' or 'gpt-4'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        reply = response["choices"][0]["message"]["content"]  # Corrected here too
        text += reply
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{prompt[:30].strip().replace(' ', '_')}.txt", "w") as f:
            f.write(text)
        return reply
    except openai.OpenAIError as e:  # Corrected Exception type
        print(f"API Error: {e}")
        return "There was an issue processing your request."



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error:", e)
            return "some error occurred. Sorry from Jarvis."

def close_application(app_name):
    """Close an application by name."""
    for process in psutil.process_iter():
        try:
            if app_name.lower() in process.name().lower():
                process.terminate()
                say(f"Closed {app_name}.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    say(f"Couldn't find {app_name} running.")

def split_screen():
    """Arrange windows to split the screen."""
    say("Arranging windows for split screen.")
    try:
        # Maximize the current window to the left half
        pyautogui.hotkey('win', 'left')
        # Allow the user to select the second application for the right half
        say("Select the application for the right screen.")
        pyautogui.hotkey('win', 'right')
    except Exception as e:
        say("Sorry, I couldn't arrange the windows.")
        print(f"Error in splitting screen: {e}")


def get_greeting_response(user_greeting):
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        correct_greeting = "good morning"
    elif 12 <= current_hour < 17:
        correct_greeting = "good afternoon"
    else:
        correct_greeting = "good night"

    if user_greeting == correct_greeting:
        return f"{correct_greeting.capitalize()}, Dhruv! Hope you're having a great time!"
    else:
        return f"It's actually {correct_greeting} right now, Dhruv. But I'll say {user_greeting} back to you!"


if __name__ == '__main__':
    print('Welcome to Jarvis A I')
    say("i am Jarvis A I, how can i help you sir")
    while True:
        query = takeCommand()

        # Greet based on time of day
        if "good morning" in query.lower():
            response = get_greeting_response("good morning")
            say(response)
        elif "good afternoon" in query.lower():
            response = get_greeting_response("good afternoon")
            say(response)
        elif "good night" in query.lower():
            response = get_greeting_response("good night")
            say(response)

        print(f"Debug: Recognized query -> {query}")  # Debug print to check what was recognized

        # Check for greeting
        if "hello " in query.lower():
            print("Debug: Triggered 'hello jarvis' condition.")  # Debug print for condition
            say("Hello Dhruv! How can I assist you today?")
        # Sites to open
        sites = [
            ['YouTube', "https://www.youtube.com/"],
            ['GitHub', "https://github.com/"],
            ['ChatGPT', "https://chat.openai.com/"],
            ['Collab', "https://colab.research.google.com/"],
            ['Canva', "https://www.canva.com/"],
            ['Amazon', "https://www.amazon.in/"],
            ['Google', "https://www.google.com/"],
        ]
        # Open sites
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # Play music
        if "play music" in query.lower():
            musicPath = r"D:\Programming\Project\vlog-music-beat-trailer-showreel-promo-background-intro-theme-274290.mp3"
            os.startfile(musicPath)
            if os.path.exists(musicPath):
                os.startfile(musicPath)
            else:
                print("Music file not found. Please check the file path.")

        # Tell time
        elif "the time" in query.lower():
            strfTime = datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")


        # Open or close VS Code
        elif "open vs code" in query.lower():
            code_path = r"C:\Users\wwwdh\OneDrive\Desktop\Visual Studio Code.lnk"
            if os.path.exists(code_path):
                os.startfile(code_path)
                say("open VS code.")
            else:
                say("I couldn't find Visual Studio Code. Please check the path.")

        elif "close vs code" in query.lower():
            close_application("Code")  # VS Code is typically named "Code" in processes

        # Split screen
        elif "split screen" in query.lower():
            split_screen()

        elif "using artificial intelligence" in query.lower():
            response = ai(prompt=query)
            say(response)

        elif "close jarvis" in query.lower():
            say("Goodbye Dhruv! Have a great day!")
            exit()



        elif "reset chat" in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
