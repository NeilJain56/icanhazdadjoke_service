import os
import subprocess
import sys

def run_command(command):
    """Run a command and print the output in real-time."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in process.stdout:
        print(line.decode(), end="")
    process.wait()

def setup_backend():
    # Create a virtual environment
    print("Setting up the backend...")
    if not os.path.exists("backend/venv"):
        run_command("python3 -m venv backend/venv")
    
    # Activate the virtual environment and install requirements
    if sys.platform == "win32":
        run_command(".\\backend\\venv\\Scripts\\activate && pip install -r backend/requirements.txt")
    else:
        run_command("source backend/venv/bin/activate && pip install -r backend/requirements.txt")

def setup_frontend():
    # Install frontend dependencies
    print("Setting up the frontend...")
    run_command("cd frontend && npm install")

if __name__ == "__main__":
    setup_backend()
    setup_frontend()
