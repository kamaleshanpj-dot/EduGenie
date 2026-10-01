import subprocess
import platform
import socket
import requests
import pyautogui
import webbrowser as wb
def open_notepad():
    subprocess.Popen("notepad.exe")
    speak("Opening Notepad.")

def open_calculator():
    subprocess.Popen("calc.exe")
    speak("Opening Calculator.")

def google_search(query):
    query = query.replace("search google", "").strip()
    if query:
        wb.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching Google for {query}.")

def open_website(site):
    wb.open(f"https://www.{site}.com")
    speak(f"Opening {site}.")

def system_info():
    speak(f"You are using {platform.system()} {platform.release()}.")
    print(platform.system(), platform.release())

def ip_address():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    speak(f"Your IP address is {ip}.")
    print("IP Address:", ip)

def lock_pc():
    speak("Locking the computer.")
    os.system("rundll32.exe user32.dll,LockWorkStation")

def volume_up():
    for _ in range(5):
        pyautogui.press("volumeup")
    speak("Volume increased.")

def volume_down():
    for _ in range(5):
        pyautogui.press("volumedown")
    speak("Volume decreased.")

def mute_volume():
    pyautogui.press("volumemute")
    speak("Volume muted.")
while True:
    elif "open notepad" in query:
    open_notepad()

elif "open calculator" in query:
    open_calculator()

elif "search google" in query:
    google_search(query)

elif "open github" in query:
    wb.open("https://github.com")
    speak("Opening GitHub.")

elif "open whatsapp" in query:
    wb.open("https://web.whatsapp.com")
    speak("Opening WhatsApp.")

elif "system information" in query:
    system_info()

elif "my ip address" in query:
    ip_address()

elif "lock computer" in query:
    lock_pc()

elif "volume up" in query:
    volume_up()

elif "volume down" in query:
    volume_down()

elif "mute volume" in query:
    mute_volume()
