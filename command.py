# command.py
import subprocess

def run_command(cmd):
    safe_commands = ["dir", "echo", "date", "whoami", "systeminfo"]
    parts = cmd.split()
    if not parts:
        return None
    if parts[0].lower() in safe_commands:
        try:
            # shell=True is required on Windows for commands like 'dir' to work
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return res.stdout.strip() or "command executed, but no output"
        except Exception as e:
            return f"something went wrong while executing code: {e}"
    else:
        return None
