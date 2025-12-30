# knowledge_sector.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIRECTORY = os.path.join(BASE_DIR, "data")

def read_dataset(filename: str) -> str:
    file_path = os.path.join(DATA_DIRECTORY, filename)
    if not os.path.exists(file_path):
        return f"[Error] File '{file_path}' does not exist."

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[Error] Could not read '{file_path}': {str(e)}"

# Example usage:
if __name__ == "__main__":
    ai_knowledge = read_dataset("ai.txt")
    blackhole_knowledge = read_dataset("blackhole.txt")

    print("AI Knowledge:\n", ai_knowledge[:200], "...")  # print first 200 chars
    print("\nBlackhole Knowledge:\n", blackhole_knowledge[:200], "...")
