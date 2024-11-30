import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import client
import apps
import parseCommand
import webbrowser
import datetime

listening = False  # Global flag for the listening state

API_KEY = '10'

def speak(text):
    """Use pyttsx3 to synthesize speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    """Process user commands and perform the appropriate action."""
    command = command.lower()
    displayLog(f"Command: {command}")
    command = parseCommand.commandParser(command)
    match command.split(" ")[0]:
        case "play":
            song = command.replace("play ", "")
            data = client.sendRequest(command='play', arg=song)
            speak(f"Playing {song}")
            displayLog(f"Playing: {song}")
            webbrowser.open(data['link'])

        case "open":
            appName = command.replace("open ", "")
            apps.open_application(appName)
            speak(f"Opening {appName}")
            displayLog(f"Opening: {appName}")

        case "news":
            topic = command.replace("news", "")
            newsData = client.sendRequest(command='news', arg=topic)
            if newsData['news']:
                newsData = newsData['news']
                if len(newsData["articles"]):
                        i = 1
                        for article in newsData['articles']:
                            source = article["source"]["name"]
                            title = article['title']
                            displayLog(f"{i}. Source: {source}\n   {title}")
                            speak(title)
                            i += 1
                else:
                    displayLog("No articles found or an error occurred. Check spelling!")

        case _:
            if command == "exit code":
                quitApp()
            else:
                speak(command)
                data = client.sendRequest(apikey=API_KEY, arg=command)
                displayLog(f"\nUser: {data['User']}\nAssitant: {data['Model']}")
                speak(data['Model'])
                saveChats(data)


def startListening():
    """Continuously listen for commands in a separate thread."""
    global listening
    listening = not listening  # Toggle listening state
    if listening:
        listen_button.config(text="🛑 Stop Listening", bg="red")
        threading.Thread(target=listenLoop, daemon=True).start()
    else:
        listen_button.config(text="🎤 Start Listening", bg="green")


def listenLoop():
    """Continuous listening loop."""
    global listening
    r = sr.Recognizer()
    while listening:
        try:
            with sr.Microphone() as source:
                displayLog("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                displayLog("Recognizing...")
                word = r.recognize_google(audio)
                displayLog(f"Trigger word: {word}")

                if word.lower() == "assistant":
                    speak("Yes")
                    processCommandLoop(r, source)

        except sr.UnknownValueError:
            displayLog("Don't understand, say again!")
        except sr.RequestError:
            displayLog("No internet connection.")
        except Exception as e:
            displayLog(f"Error: {e}")


def processCommandLoop(recognizer, source):
    """Process commands after activation."""
    global listening
    n = 1
    while listening and n <= 3:
        try:
            displayLog("Activated...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            displayLog("Command recognized!")
            processCommand(command)
            n=1
        except sr.UnknownValueError:
            displayLog("Don't understand, say again!")
            n=+1
        except sr.RequestError:
            displayLog("No internet connection.")
            break
        except Exception as e:
            displayLog(f"Error: {e}")
            break


def displayLog(message):
    """Display messages in the GUI log."""
    log_box.config(state=tk.NORMAL)
    log_box.insert(tk.END, f"{message}\n")
    log_box.see(tk.END)
    log_box.config(state=tk.DISABLED)


def quitApp():
    """Quit the application."""
    global listening
    listening = False  # Stop listening
    root.destroy()

def previousChats():
    try:
        with open('client/history.txt') as file:
            while chats:=file.readline():
                if chats:
                    displayLog(chats.strip())
    except:
        pass

def getTime():
    return datetime.datetime.now()

def saveChats(data):
    with open('client/history.txt', 'a') as file:
        file.write(f"{getTime()}\nUser: {data['User']}\nAssitant: {data['Model']}\n")


# Initialize Tkinter window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("500x410")
root.minsize(500, 410)
root.maxsize(500, 410)

# Log display area
log_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, width=60, height=20)
log_box.pack(pady=5)

# Buttons
listen_button = tk.Button(root, text="🎤 Start Listening", command=startListening, bg="green", fg="white", font=("Arial", 10))
listen_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=quitApp, bg="red", fg="white", font=("Arial", 10))
quit_button.pack(pady=5)

# Run the Tkinter main loop
displayLog("Initializing Assistant...")
speak("Initializing Assistant...")
previousChats()
root.mainloop()