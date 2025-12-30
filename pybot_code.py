# pybot_code.py
import random
import string

class PybotProgrammer:
    def __init__(self, name="PybotProgrammer", version="0.1.1"):
        self.name = name
        self.version = version
        self.intents = {
            "python": [
                "python code", "python code pls", "i want python code", "i need python code", "any python code", "yo you have python code", "do you have any python",
                "pls me need python code pls", "hello i want python code", "python code right now", "the python code", "the python code pls", "the python code please"
            ],
            "clang": [
                "give me C code", "i want C code", "hey i want C code", "give me a C code", "hello, i want C code", "me want C code", "C language code pls", "i wanna make a C code",
                "C snippet", "C snippet pls"
            ],
            "lua": [
                "me want lua code", "roblox code", "lua", "roblox", "lua snippet", "lua code", "roblox snippet", "roblox lua", "i want roblox lua code"
            ]
        }

    def matchBotIntent(self, userInputMessage):
        # normalize input
        userInputMessage = userInputMessage.lower()
        userInputMessage = userInputMessage.translate(str.maketrans("", "", string.punctuation))
        priorityIntent = ["python", "clang"]
        for intent in priorityIntent:
            for phrase in self.intents.get(intent, []):
                # normalize phrase
                phrase_clean = phrase.lower().translate(str.maketrans("", "", string.punctuation))
                if phrase_clean in userInputMessage:
                    return intent
        for intent, phrases in self.intents.items():
            for phrase in phrases:
                phrase_clean = phrase.lower().translate(str.maketrans("", "", string.punctuation))
                if phrase_clean in userInputMessage:
                    return intent
        return None
    def respondCode(self, userMsg):
        userMsg = userMsg.lower()
        intent = self.matchBotIntent(userInputMessage=userMsg)

        if intent == "python":
            return random.choice([
                "print(\"hello world!\")",
                "print('hello user.')",
                "import random",
                "import math",
                "def function(x): \n\treturn x",
                "import sys",
                "eval(shutdown -s)",
                "f\"echo {text_here}\"",
                "sys.stdout.write('hello the world')",
                "def add(a: int, b: int) -> int: \n\treturn a + b",
                "def HelloWorld(txt): \n\tprint(txt)",
                "if __name__ == \"__main__\": \n\tprint('hello')",
                "HelloWorld('print'), im just joking.",
                "print(1 + 1)",
                "print(2 + 2)",
                "print(40 // 3)",
                "x = 25",
                "abcd = \"efgh\"",
                "print(\"test\" * 10)",
                "eval(20 + 3)"
            ])
        elif intent == "clang":
            return random.choice([
                "printf(\"hello world\");",
                "int main() {\n\tprintf(\"hello world\");\n}",
                "int one = 1\nprintf(\"%d\", one)",
                "int num = 14;\nprintf(\"%p\", &num);",
                "int a = 10;\nint *p = &a;\nprintf(\"%p\", p)",
                "int add(int a, int b) {\n\treturn a + b\n}"
            ])
        elif intent == "lua":
            return random.choice([
                "print(\"Hello World!\")",
                "print(\"i am in Lua!\")",
                "local function add(a, b) then\n\treturn a + b\nend"
            ])
        else:
            return "sorry i only understand python and C. now stfu retard"
