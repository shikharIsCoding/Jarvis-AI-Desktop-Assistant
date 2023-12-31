import datetime
from hidden import apikey
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
from openai import OpenAI

chatString = ""


def chat(query):
    global chatString
    client = OpenAI(api_key=apikey)
    chatString += f"Shikhar:{query}\n Jarvis:"

    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=chatString,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response_text = response.choices[0].text
        say(response_text)
        chatString += f"{response_text}\n"
    except Exception as e:
        print(f"Error in generating response: {e}")
        response_text = "I am sorry, I could not understand that."

    return response_text

def ai(userInput):
    client = OpenAI(api_key=apikey)
    text = f"OpenAi responses for userInput: {userInput}\n *************\n\n"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=userInput,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # wrap this inside of a try catch block
    print(response.choices[0].text)
    text += response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(userInput.split('AI')[1:]).strip()}.txt","w")as f:
        f.write(text)

def say(text):
    os.system(f"say '{text}'")  # Ensure the text is enclosed in quotes

# Function to listen and recognize speech
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Corrected the syntax here

        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print ("recognizing")
        # Using Google speech recognition
        query = r.recognize_google(audio, language="eng-in")
        print(f"User said: {query}\n")
    except Exception as e:
        # Handle the exception if the speech is unintelligible
        print("Google Speech Recognition could not understand the audio")
        return "Some Error Occured. Sorry from Jarvis"
    except sr.RequestError as e:
        # Handle the exception if there's a problem with the Google API
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    return query

if __name__ == '__main__':
    print('Initializing AI Assistant...')
    say("Hello, I am your A.I Assistant Jarvis")
      # Echo the command or replace with whatever functionality you want
    while True:
        print("listening")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
              say(f"Opening {site[0]} broski")
              webbrowser.open(site[1])# using site[1] to because we have list of list and for each list we are opening the second elemnet of that particular list

        if "the time" in query:
            Time = datetime.datetime.now().strftime("%H:%M")
            say(f'Sir the time is {Time}')


        elif "open music" in query:
            musicPath = "/Users/shikhar/Downloads/tvari-hawaii-vacation-159069.mp3"
            os.system(f"open '{musicPath}'")

        elif "stop the music" in query or "pause the music" in query:
            os.system("osascript -e 'tell application \"Music\" to pause'")




        apps = [["facetime", "/System/Applications/FaceTime.app"],["whatsapp","/Applications/WhatsApp.app"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]} broski")
                os.system(f"open '{app[1]}'")  # Note the use of f-string for the path


        if "Using AI".lower() in query.lower():
            ai(query)

        elif "exit".lower() in query.lower() or "quit".lower() in query.lower() or "bye".lower() in query.lower():
            say("Bye bye sir")
            exit()
        elif "reset chat".lower() in query.lower():

            chatString = ""


        else:
            chat(query)




