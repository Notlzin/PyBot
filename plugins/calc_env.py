# calc_env.py
from plugined_bot import library
"""
this is basically the place where these are happened:
    * math_plugin.dll
    * plugined_bot.py
    * and a whole lot other shit
"""
plugin = library

if __name__ == "__main__":
    isPluginBotActive = True
    while isPluginBotActive:
        user = input("user@pybot_with_plugin#true> ")
        if user.startswith("exit"):
            print("the_bot@pybot_with_plugin#true> bye bye")
            break
        if user.startswith("add"):
            try:
                _, a, b = user.split()
                result = plugin.add(float(a), float(b))
                print(f"the_bot@pybot_with_plugin#true> {result}")
            except Exception as e:
                print(f"the_bot@pybot_with_plugin#true> error: {e}")

        elif user.startswith("sub"):
            try:
                _, a, b = user.split()
                result = plugin.sub(float(a), float(b))
                print(f"the_bot@pybot_with_plugin#true> {result}")
            except Exception as e:
                print(f"the_bot@pybot_with_plugin#true> error: {e}")

        elif user.startswith("mul"):
            try:
                _, a, b = user.split()
                result = plugin.mul(float(a), float(b))
                print(f"the_bot@pybot_with_plugin#true> {result}")
            except Exception as e:
                print(f"the_bot@pybot_with_plugin#true> error: {e}")

        elif user.startswith("div"):
            try:
                _, a, b = user.split()
                result = plugin.divi(float(a), float(b))
                print(f"the_bot@pybot_with_plugin#true> {result}")
            except Exception as e:
                print(f"the_bot@pybot_with_plugin#true> error: {e}")
