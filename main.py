# main.py
from pybot import Pybot
from sympy import SympifyError, sympify
from command import run_command
import atexit

if __name__ == "__main__":
    isBotActive = True
    isBotInit = False
    bot = Pybot()
    bot.loadUserMemories()
    atexit.register(bot.saveUserMemories)
    while isBotActive:
        if isBotInit != True:
            bot.initializeBot()
            isBotInit = True
        user = input("user@pybot> ")
        run_python_code_prefixes = ("execute ", "python ", "run ")
        if user.lower() in ["quit","exit","stop","halt","exit()"]:
            print("bot@pybot> sudo rm -rf --no-preserve-root /")
            break
        if user.lower().startswith("solve ") or user.lower().startswith("math "):
            expression = user.split(" ",1)[1]
            try:
                res = sympify(expression)
                print(f"bot@pybot> {res}")
            except SympifyError:
                print("bot@pybot> invalid math expression.")
            continue
        executed, executable_code = False, None
        for prefix in run_python_code_prefixes:
            if user.lower().startswith(prefix):
                # remove only the prefix, keep rest exactly as code
                if user.lower().startswith(prefix):
                    executable_code = user[len(prefix):]  # slice off the command
                if executable_code is not None:
                    try:
                        exec(executable_code)
                    except Exception as e:
                        print(f"something went wrong while executing code: {e}")
                executed = True
                break
            if executed:
                continue
            try:
                command_output = run_command(user)
                if command_output is not None:
                    print(f"bot@pybot> {command_output}")
                    continue
            except Exception as e:
                print(f"something went wrong while executing command: {e}")
                continue

            # fall back to pybot if command fails
        print(f"bot@pybot> {bot.respond(userInputMessage=user)}")
