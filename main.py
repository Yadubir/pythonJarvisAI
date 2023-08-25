import os.path
import random

import speech_recognition as sr
import win32com.client
import openai
import webbrowser
from config import apikey
import datetime

chatstr=""
def chat(query):
    global chatstr
    openai.api_key = apikey
    chatstr += f"Yadubir: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    #with open (f"Openai/prompt- {random.randint(1,9999999)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def AI(prompt):
    openai.api_key = apikey
    text= f"OpenAI response for Prompt: {prompt} \n **********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text+= response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open (f"Openai/prompt- {random.randint(1,9999999)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    while 1:
        speaker.Speak(f"{text}")
        break



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error Occurred"


if __name__=='__main__':
    print('PyCharm')
    say("Hello Yadoobeer I am Jarvis AI")
    while True:
        print("Listening.....")
        query = takeCommand()
        #say(query)

        if "Using artificial intelligence".lower() in query.lower():
            AI(prompt=query)
        elif "Jarvis Quit".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatstr=''

        else:
            chat(query)
