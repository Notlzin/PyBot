# main_code.py
from pybot_code import PybotProgrammer

if __name__ == "__main__":
    isBotActive = True
    bot = PybotProgrammer()
    while isBotActive:
        user = input("user@pybot #code> ")
        if user in ["quit","stop","halt","exit","exit()"]:
            print("bot@pybot#code> exit()")
            break
        print(f"bot@pybot #code> {bot.respondCode(userMsg=user)}")
