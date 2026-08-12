import speech_recognition as sr
import pyttsx3
import pyautogui
import os
import subprocess

# --- Initialize Voice Engine ---
engine = pyttsx3.init()

def speak(text):
    print(f"Shadow AI: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    r.energy_threshold = 300 
    r.dynamic_energy_threshold = True
    
    with sr.Microphone() as source:
        print("\n🎙️ Listening... (Boliye, main sun raha hoon)")
        r.adjust_for_ambient_noise(source, duration=0.8)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return ""
        
    try:
        print("🔄 Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"🗣️ Aapne kaha: {query}")
        return query.lower()
    except:
        return ""

# --- Main Program Loop ---
if __name__ == "__main__":
    speak("Shadow AI system is online, Tawkeer. Ready for your commands.")
    
    while True:
        command = listen_command()
        
        if not command:
            continue
            
        # 1. Apps Open Karna (Jaise Instagram, Chrome, Notepad)
        if "open instagram" in command:
            speak("Opening Instagram.")
            os.system("start https://www.instagram.com")
            
        elif "open chrome" in command or "open browser" in command:
            speak("Opening Google Chrome.")
            os.system("start chrome")
            
        elif "open notepad" in command:
            speak("Opening Notepad.")
            os.system("notepad")
            
        # 2. Wi-Fi Connect / Disconnect Karna
        elif "disconnect wifi" in command or "disconnect internet" in command:
            speak("Disconnecting from Wi-Fi.")
            # Windows command to disconnect Wi-Fi (Network name ki jagah aapke active network ka naam aa sakta hai)
            os.system('netsh wlan disconnect')
            
        elif "connect wifi" in command:
            speak("Connecting to your Wi-Fi network.")
            # Apne Wi-Fi ka naam yahan 'Your_WiFi_Name' ki jagah likh sakte hain
            os.system('netsh wlan connect name="Your_WiFi_Name"')
            
        # 3. System Controls
        elif "unlock" in command:
            speak("Unlocking your system now.")
            pyautogui.write("Your_Password_Here")
            pyautogui.press("enter")
            
        elif "shut down" in command or "shutdown" in command:
            speak("Shutting down your laptop. Goodbye!")
            os.system("shutdown /s /t 1")
            break
            
        elif "exit" in command or "stop" in command:
            speak("Shutting down Shadow AI. Goodbye!")
            break
            
        else:
            speak("Command samajh nahi aayi. Dubara boleing.")
