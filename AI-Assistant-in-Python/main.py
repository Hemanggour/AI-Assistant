# import webbrowser
# import search
import speech_recognition as sr
import pyttsx3
import youtube
import apps
import ChatAI
# import AI
import parseCommand
import news

def speak(text):
    engine = pyttsx3.init()
    # voices = engine.getProperty("voices")
    # engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    print(command)
    command = parseCommand.commandParser(command)
    match command.split(" ")[0]:
        case "play":
            song = command.replace("play ", "")
            youtube.youtube_search(song)
            speak(f"Playing {song}")

        case "open":
            appName = command.replace("open ", "")
            apps.open_application(appName)
            speak(f"Opening {appName}")
        
        case "news":
           topic = command.replace("news", "")
           newsData = news.getNews(topic.strip(" "))
           if len(newsData["articles"]):
                i = 1
                for article in newsData['articles']:
                    print(f"{i} Source: {article["source"]["name"]}:\n\t{article['title']}")
                    speak(article['title'])
                    i += 1
                    # print(f"   Source: {article['source']['name']}")
                    # print(f"   URL: {article['url']}\n")
                else:
                    print("No articles found or an error occurred.\nCheck Spelling!!")

        case _:
            if(command == "exit code"):
                exit(0)
            else:
                speak(command)
                data = ChatAI.GenerateContent(command)
                # data = AI.GenerateContent(command)
                print(data)
                speak(data)

if __name__ == "__main__":
    speak("initializing Assistant...")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                print("Recognizing...")
                word = r.recognize_google(audio)
                print(word)

                if (word.lower() == "assistant"):
                    speak("Yes")
                    com = 1
                    # with sr.Microphone() as source:
                    while(com <= 3):
                        try:
                            print("Activated...")
                            audio = r.listen(source, timeout=5, phrase_time_limit=5)
                            print("Recognizing...")
                            command = r.recognize_google(audio)
                            print("Recognized!!")
                            processCommand(command)
                        except sr.UnknownValueError:
                            print("Dont Understand, say Again!!")
                            com += 1
                        except sr.WaitTimeoutError as e:
                            print(f"Error: {e}")
                            com += 1
                        except sr.RequestError:
                            print("Connection Error: NO internet Connection")
                        except Exception as e:
                            print(f"Error: {e}")
                        else:
                            com = 1

        except sr.UnknownValueError:
            print("Dont Understand, say Again!!")
        except sr.RequestError:
            print("Connection Error: No internet Connection")
        except Exception as e:
            print(f"Error: {e}")