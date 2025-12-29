# Pybot

this thing is a hardcoded bot project i made because i was bored, now can run in Docker and released on Github

---

## what does it have

- NLTK-powered text processing (???)
- a fake MLP (TinyMLP)
- a text analyzer (text_analyzer.c)
- OpenWeather API integration (yes)
- docker available, devops is free

## structure

PyBot/
├─ main.py
├─ main_code.py
├─ pybot_memory.json
├─ command.py
├─ pybot.py
├─ pybot_code.py
├─ text_analyzer.c
├─ requirements.txt
├─ .gitignore
├─ .dockerignore
├─ Dockerfile
├─ .env (do not commit!!)
└─ README.md

## docker and stuff

build: docker build -t pybot .

run: docker run -it pybot

## requires

Python 3.12+
gcc
docker / docker desktop

## conclusion

this is just for my portfolio lmao
