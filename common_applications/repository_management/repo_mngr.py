import os
import sys
import shutil
import subprocess

# finding the anchor repo root point:
print("Stage 0, finding the anchor repo root point: ")
repo_root = "."
while True:
    files = os.listdir(repo_root)
    print(f"files {files}")
    if "dockerfile" in files and "requirements.txt" in files:
        break
    else:
        repo_root = "../" + repo_root

venv_path = os.path.join(repo_root, ".venv")  # Virtual environment location

# Step 1: Create virtual environment if it doesn't exist
if not os.path.exists(venv_path):
    print("Creating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", venv_path])
else:
    print("Virtual environment already exists.")

# Step 2: Determine path to Python inside venv
if os.name == "nt":  # Windows
    python_bin = os.path.join(venv_path, "Scripts", "python.exe")
else:  # macOS / Linux
    python_bin = os.path.join(venv_path, "bin", "python")

# Step 3: Install Black inside venv
print("Installing Black in virtual environment...")
subprocess.check_call([python_bin, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([python_bin, "-m", "pip", "install", "black"])

# Step 4: Use Black from venv to format Python files
for root, dirs, files in os.walk(repo_root):
    dirs[:] = [d for d in dirs if not d.startswith(".")]  # Skip hidden dirs
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            print(f"Formatting {path}...")
            subprocess.run([python_bin, "-m", "black", path])


print("Cleaning up ...")
venv_path = os.path.join(repo_root, ".venv")
if os.path.exists(venv_path):
    shutil.rmtree(venv_path)
    print(f"Removed virtual environment at {venv_path}\n")
    print("NOTE")
else:
    print("No .venv folder found, skipping cleanup.")
