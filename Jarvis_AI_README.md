
# Jarvis AI

## Overview
Jarvis AI is a voice-controlled virtual assistant powered by Python and OpenAI's GPT API. This assistant can perform various tasks such as chatting, opening websites, playing music, managing applications, and splitting screens. The application leverages multiple libraries to integrate AI, voice recognition, text-to-speech, and system utilities.

## Features
- **Voice Recognition**: Recognizes spoken commands using Google Speech Recognition.
- **Text-to-Speech**: Converts AI responses and notifications into speech.
- **Chatbot Integration**: Handles user queries and conversations with OpenAI's GPT API.
- **Custom Greeting**: Responds based on the time of day.
- **Application Management**: Opens and closes applications.
- **Web Browsing**: Opens frequently visited websites.
- **Music Playback**: Plays a predefined music file.
- **Screen Management**: Splits windows for multitasking.
- **Time Announcements**: Tells the current time on request.
- **Reset Chat**: Resets the conversation history.

---

## Libraries and Modules

### Core Libraries
1. **datetime**: Used to fetch the current time for greetings and time announcements.
2. **os**: Provides file and directory management functionality.
3. **webbrowser**: Opens websites in the default web browser.
4. **pyttsx3**: Converts text responses to speech.
5. **speech_recognition (sr)**: Captures and processes voice commands.
6. **openai**: Interfaces with OpenAI's GPT models to handle AI-powered conversations.
7. **psutil**: Manages system processes for opening and closing applications.
8. **pyautogui**: Controls screen layout and window management.

### Additional Configuration
- **`config.py`**: Contains your OpenAI API key (`apikey`).
- Ensure the `apikey` variable is correctly set in this file to avoid API errors.

---

## Functions

### 1. `chat(query)`
Handles user queries by interacting with OpenAI's GPT API. It maintains a chat history and returns AI-generated responses.

- **Parameters**: `query` (string) - User's input query.
- **Returns**: AI-generated response (string).

---

### 2. `ai(prompt)`
Processes user commands involving AI tasks, saves the AI response to a file, and returns the result.

- **Parameters**: `prompt` (string) - AI prompt text.
- **Returns**: AI-generated response (string).
- **Side Effects**: Creates a folder named `Openai` and saves response files there.

---

### 3. `say(text)`
Converts text into spoken audio using `pyttsx3`.

- **Parameters**: `text` (string) - Text to be spoken.
- **Returns**: None.

---

### 4. `take_command()`
Captures and recognizes voice input using the microphone.

- **Parameters**: None.
- **Returns**: Recognized speech as a string.
- **Handles**: Errors in speech recognition.

---

### 5. `close_application(app_name)`
Closes an application by matching its name.

- **Parameters**: `app_name` (string) - Name of the application to close.
- **Returns**: None.

---

### 6. `split_screen()`
Arranges windows to split the screen for multitasking.

- **Parameters**: None.
- **Returns**: None.
- **Side Effects**: Moves windows to the left and right halves of the screen.

---

### 7. `get_greeting_response(user_greeting)`
Returns a greeting based on the time of day.

- **Parameters**: `user_greeting` (string) - User's greeting text.
- **Returns**: Corrected greeting text (string).

---

## Setup Instructions
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/jarvis-ai.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `config.py` file and add your OpenAI API key:
   ```python
   apikey = "your_openai_api_key"
   ```

4. Run the program:
   ```bash
   python jarvis.py
   ```

---

## Usage
- Speak commands into your microphone.
- Use phrases like:
  - "Good morning"
  - "Open YouTube"
  - "Play music"
  - "What is the time?"
  - "Using artificial intelligence, write a Python code to add two numbers."

---

## Supported Websites
- YouTube
- GitHub
- ChatGPT
- Google Colab
- Canva
- Amazon
- Google

---

## Troubleshooting
1. **API Errors**: Ensure your OpenAI API key is correct and you have sufficient quota.
2. **Voice Recognition Errors**: Check your microphone and system permissions.
3. **Music Playback Issues**: Verify the file path for the music file.

---

## Contribution
Feel free to fork this repository, create pull requests, or submit issues. Contributions are welcome!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

