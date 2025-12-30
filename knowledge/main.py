# main.py
from knowledge_sector import read_dataset
import sys

if __name__ == "__main__":
    isBotActive = True
    while isBotActive:
        user = input("user@scholar_pybot> ")
        if user.startswith("exit") or user.startswith("quit"):
            sys.stdout.write("scholar@scholar_pybot> goodbye.")
            break
        if user.startswith("ai"):
            sys.stdout.write(f"scholar@scholar_pybot> {read_dataset("ai.txt")}")
        elif user.startswith("blackhole"):
            sys.stdout.write(f"scholar@scholar_pybot> {read_dataset("blackhole.txt")}")
        else:
            sys.stdout.write("scholar@scholar_pybot> idk about that lmao")
