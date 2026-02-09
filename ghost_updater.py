import os
import shutil
import sys
import time
import zipfile
import requests
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)

# ======================
# CONFIG
# ======================
GITHUB_REPO_ZIP = "https://github.com/BlackFalcon-cloud/ghost_framework_latest/archive/refs/heads/main.zip"
PROJECT_NAME = "Ghost_Framework"

CURRENT_DIR = os.getcwd()
TEMP_DIR = os.path.join(CURRENT_DIR, "_ghost_update_temp")
ZIP_PATH = os.path.join(CURRENT_DIR, "ghost_update.zip")

# ======================
# DANGER BANNER
# ======================
f = Figlet(font="slant")
print(Fore.RED + Style.BRIGHT + f.renderText("GHOST UPDATER"))

print(Fore.RED + Style.BRIGHT + "=" * 70)
print(Fore.RED + Style.BRIGHT + "  ☠  DANGER ZONE : AUTO UPDATE MODE  ☠")
print(Fore.YELLOW + Style.BRIGHT + "  This will REPLACE old framework files")
print(Fore.RED + Style.BRIGHT + "=" * 70 + "\n")

time.sleep(1)

# ======================
# CONFIRMATION
# ======================
choice = input(Fore.RED + Style.BRIGHT + "[!] Continue update? (y/n): ").lower()
if choice != "y":
    print(Fore.CYAN + "[*] Update cancelled.")
    sys.exit()

# ======================
# CLEAN TEMP
# ======================
if os.path.exists(TEMP_DIR):
    shutil.rmtree(TEMP_DIR)

os.makedirs(TEMP_DIR, exist_ok=True)

# ======================
# DOWNLOAD
# ======================
print(Fore.YELLOW + "[*] Downloading latest framework from GitHub...")
response = requests.get(GITHUB_REPO_ZIP, stream=True)

with open(ZIP_PATH, "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

print(Fore.GREEN + "[+] Download completed.")

# ======================
# EXTRACT
# ======================
print(Fore.YELLOW + "[*] Extracting update package...")
with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
    zip_ref.extractall(TEMP_DIR)

print(Fore.GREEN + "[+] Extraction done.")

# ======================
# REMOVE OLD FILES
# ======================
print(Fore.RED + "[!] Removing old framework files...")

for item in os.listdir(CURRENT_DIR):
    if item in ["ghost_updater.py", "_ghost_update_temp", "ghost_update.zip"]:
        continue
    item_path = os.path.join(CURRENT_DIR, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)
    else:
        os.remove(item_path)

print(Fore.GREEN + "[+] Old files removed.")

# ======================
# MOVE NEW FILES
# ======================
print(Fore.YELLOW + "[*] Installing new version...")

extracted_root = os.path.join(TEMP_DIR, "Ghost_Framework-main")

for item in os.listdir(extracted_root):
    src = os.path.join(extracted_root, item)
    dst = os.path.join(CURRENT_DIR, item)
    shutil.move(src, dst)

print(Fore.GREEN + "[+] Update installed successfully.")

# ======================
# CLEANUP
# ======================
os.remove(ZIP_PATH)
shutil.rmtree(TEMP_DIR)

print(Fore.CYAN + Style.BRIGHT + "\n[*] Ghost Framework is now up to date.")
print(Fore.RED + Style.BRIGHT + "[☠] Restart the tool to apply changes.\n")

