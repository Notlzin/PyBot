# command.py
import subprocess

def run_command(cmd):
    safe_commands = ["dir","echo", "date", "whoami", "systeminfo"]
    if cmd.split()[0] in safe_commands:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return res.stdout
    else:
        return "access restricted"
