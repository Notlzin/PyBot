# pybot.py
import random, string
import time
import json, nltk
import os, requests
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import subprocess
from dotenv import load_dotenv
from tinymlp import runMLP
import requests

# load .env variable
load_dotenv()

nltk.download('punkt')
nltk.download('wordnet')

# forcing python to fucking see the dictionary key because python is blind as fuck.
class AlwaysExistsDict(dict):
    def __getitem__(self, key):
        if key not in self:
            self[key] = "user"
        return super().__getitem__(key)

# helper function
def analyze_text(text):
    try:
        result = subprocess.run(
            ["./text_analyzer.exe"],
            input=text,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"[C Analyzer Error] {e}")

class Pybot:
    def __init__(self, name="pybot", ver="1.0.0-release", memory_file="pybot_memory.json"):
        self.name = name
        self.version = ver
        self.memory = AlwaysExistsDict()
        self.memory_file = memory_file or os.path.join(os.path.dirname(__file__), "pybot_memory.json")
        self.loadUserMemories()
        self.open_weather_key = os.getenv("OPEN_WEATHER_KEY")
        self.lemmatizer = WordNetLemmatizer()
        self.intents = {
            "greeting": [
                "hello", "hi", "wsg", "hey", "yo", "hoi", "hiya", "whats up", "good morning",
                "good evening", "good afternoon", "whats happening", "hola", "howdy",
                "halo", "hallo", "heylo", "henlo", "hilo", "heya", "heyo", "wsp", "hey yo",
                "sup",
            ],
            "farewell": [
                "bye bye", "goodbye", "cya", "later", "later hater", "goodbye goodbye", "bad bye", "see you", "gtg", "i gotta go", "yo me go", "im gone", "i'm gone",
                "disappears", "peace", "adios", "adios amigos", "good to the bye", "bye good", "yo gtg", "yo me gtg", "yo i gtg", "hey i need to go", "heyya i needa go",
                "bye", "see ya"
            ],
            "insults": [
                "i hate you", "mid bot", "trash bot", "retard", "retarded bot", "i fucking hate you", "fuck off chatbot", "very mid bot", "you're garbage", "piece of shit",
                "useless piece of shit", "go fuck yourself", "boohoo waa now go fuck yourself", "hate. i fucking hate you", "garbage bot", "useless piece of metal", "artificial stupidity",
                "technologically reversed ai", "you're killing all the water retard", "stupid", "dumbass", "braindead", "deadass stupid bot", "fuck you", "stfu cunt"
            ],
            "time": [
                "whats the time", "what time is it", "what is the time", "what the time now", "yo whats the time", "time?", "whats the time?", "hello, whats the time",
                "hello, whats the time?", "whats the time?", "vro whats the time", "bro the time pls"
            ],
            "weather": [
                "whats the weather currently", "whats the weather", "yo what is the weather rn", "hey, weather?", "what is the current weather", "yo whats the weather",
                "pybot, whats the weather", "hey, weather pls", "the weather please", "the weather plsplspls"
            ]
        }
    def saveUserMemories(self):
        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(self.memory, file, indent=4)

    def readWikipediaPages(self, page_title: str) -> str:
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"
            res = requests.get(url=url)
            data = res.json()
            return data.get("extract", "no content found..")
        except Exception as e:
            return f"error fetching the wikipedia page: {e}"

    def loadUserMemories(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if isinstance(data, dict):
                        self.memory =  data
            except json.JSONDecodeError:
                print("[WarningDecodeError] memory corrupted, starting fresh...")
                self.memory = {}
        else:
            with open(self.memory_file, "w", encoding="utf-8") as file:
                json.dump({}, file)
            self.memory = {}

    def getWeather(self, city="Jakarta"):
        if not self.open_weather_key:
            return "the API key is not set. cannot get weather data."
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.open_weather_key}&units=metric"
            response = requests.get(url=url)
            data = response.json()
            if data.get("cod") != 200:
                return f"couldnt fetch the weather: {data.get('message')}"
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"current weather in {city}: {weather_description}, {temperature} degrees."
        except Exception as e:
            return f"error fetching the weather: {str(e)}"

    def normalize(self, text):
        text = text.lower().translate(str.maketrans("", "", string.punctuation))
        tokens = word_tokenize(text, preserve_line=True)
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def matchBotIntent(self, userInputMessage):
        tokens = self.normalize(userInputMessage)
        if "weather" in tokens or "forecast" in tokens or "temperature" in tokens:
            return "weather"
        for intent in ["greeting","farewell","insults","time"]:
            for phrase in self.intents[intent]:
                phrase_tokens = self.normalize(phrase)
                if all(tok in tokens for tok in phrase_tokens):
                    return intent
        return None, None

    def respond(self, userInputMessage):
        analyze_text(text=userInputMessage)
        runMLP(text=userInputMessage)

        userInputMessage = userInputMessage.lower()
        intent = self.matchBotIntent(userInputMessage=userInputMessage)
        print(f"[DEBUG] matched intent: {intent}")

        HardcodedUserNameInput = ["my name is", "hi im", "hi my name is"]
        for trigger in HardcodedUserNameInput:
            if trigger in userInputMessage:
                name = userInputMessage.split(trigger, 1)[-1].strip().split()[0]
                if name == self.name.lower():
                    return f"yo you cant use my name, you tried input this: {self.name}, very clever."
                self.memory["users_name"] = name
                return random.choice([
                    f"hey nice to meet you, {name}",
                    f"yo! nice to meet ya, {name}",
                    f"nice to meet you too, {name}",
                    f"nice to meet you {name}",
                    f"hey nice to meet ya to {name}!"
                ])

        AskUsersNameInput = [
            "what's my name", "whats my name", "what is my name",
            "yo what is my name?", "whats my name?"
        ]
        for trigger in AskUsersNameInput:
            if trigger in userInputMessage:
                if "users_name" in self.memory:
                    return random.choice([
                        f"you're: {self.memory['users_name']}, ofcourse!",
                        f"hey, you're {self.memory['users_name']}!",
                        f"yes. i still remember you. you're {self.memory['users_name']}."
                    ])
                else:
                    return "who the fuck are you??? whats your name"

        MyAgeIsInput = [
            "my age is", "im this old", "hey yo my age is this",
            "hey my age is this", "my age is probably"
        ]
        for trigger in MyAgeIsInput:
            if trigger in userInputMessage:
                try:
                    age = int("".join(filter(str.isdigit, userInputMessage)))
                    if age > 100:
                        return f"holy fuck your age is: {age} thats basically impossible"
                    elif age < 0:
                        return f"keep racing them lmao, no way you're this age: {age}"
                    else:
                        self.memory["users_age"] = age
                        return random.choice([
                            f"yoooo you're {age} years old",
                            f"ok age remembered, you're age is: {age}",
                            f"got it. age: {age}"
                        ])
                except ValueError:
                    return f"please enter a valid integer, you just gave us this: {userInputMessage}"

        UserAsksAgeField = [
            "whats my age", "hey whats my age again?", "yo whats my age, i forgot"
        ]
        for trigger in UserAsksAgeField:
            if trigger in userInputMessage:
                if "users_age" in self.memory:
                    return f"you're uhh this old: {self.memory['users_age']} yeah yeah like that"
                else:
                    return "fuck no i dont know your age, how old are you though??"

        if intent == "greeting":
            return random.choice([
                "hello!!",
                "hi what can i do for you",
                "echo hello > my_hello.txt",
                "yo whats poppin",
                "hey, hows life :/",
                "im doing all good",
                "hello, im pybot.",
                "yo whats up user",
                "hey what up user, whats happening",
                f"hello, {self.memory.get('users_name', 'user')}."
            ])
        elif intent == "farewell":
            return random.choice([
                "bye!!",
                "bye",
                "good bye",
                "goodbye",
                "later hater too",
                "later hater",
                "yo see you on the flipside",
                "me too, bye",
                f"goodbye {self.memory["users_name"]}!",
                "yo bye user",
                "exit()",
                "goodbye bye",
                "bye bye",
                "me too, so cya",
                "see ya",
                "later",
                "later homie"
                f"later {self.memory["users_name"]}."
            ])
        elif intent == "insults":
            return random.choice([
                "you can go fuck yourself too",
                "now that aint nice, fucking cunt.",
                f"fuck yourself too, {self.memory["users_name"]}!",
                "fuck you shithead",
                "you're brained writing this.",
                f"stop that, you're fucking with me, {self.memory["users_name"]}.",
                "shut your fucking mount, shut the fuck up you cunt."
            ])
        elif intent == "time":
            return random.choice([
                f"the time is... uh {time.ctime()}",
                time.ctime()
            ])
        elif intent == "weather":
            city = "Jakarta" # fallback
            lowercaseMsg = userInputMessage.lower()
            if " in " in lowercaseMsg:
                index = lowercaseMsg.index(" in ")
                city = userInputMessage[index + 4 :].strip()
            return self.getWeather(city=city)
        else:
            return random.choice([
                "what the fuck do you mean by that??",
                "uhhh sorry i dont have the capability of understanding that.",
                f"hey, stop fucking with me, {self.memory["users_name"]}. i got telemetry."
            ])

    def initializeBot(self):
        print(f"welcome back, {self.memory["users_name"]}.")
        time.sleep(0.66)
        print("initializing Pybot....")
        time.sleep(0.62)
        print("handling intents...")
        time.sleep(0.62)
        print("initializing programming functions for pybot...")
        time.sleep(0.62)
        print("finished completing the intent processor function.")
        time.sleep(0.62)
        print("source ~/.botrc")
        time.sleep(0.62)
        print("echo \"training_data_here\" > pybot_intent.txt.")
        time.sleep(0.62)
        print("initializing memory array...")
        time.sleep(0.62)
        print("adding cuss words to pybot...")
        time.sleep(0.62)
        print("#include <llama.h>")
        time.sleep(0.62)
        print("setting up OpenWeather API key.")
        time.sleep(0.62)
        print("halting processes.")
        time.sleep(0.62)
        print("and... finished the initialization.")
        time.sleep(0.62)
