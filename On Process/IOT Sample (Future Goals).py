import speech_recognition as sr
import requests
import txttospeech 
def process_speech(text):
    if "hey skynet it's sweating" in text.lower() or "hey skynet its sweating" in text.lower():  
        print("I'll turn on the fan.")
        response = requests.post("https://www.skynetbee.com/internet-of-things/switch-from-voice-assist.php", data={'pinno': '1','sts':'1'})
        print(response)
    elif "hey skynet it's cold" in text.lower() or "hey skynet its cold" in text.lower():
        print("I'll turn off the fan.")
        response = requests.post("https://www.skynetbee.com/internet-of-things/switch-from-voice-assist.php", data={'pinno': '1','sts':'0'})
        print(response)
    elif "light on" in text.lower() or "lights on" in text.lower():
        txttospeech.tts("Pushpa")
        response = requests.post("https://www.skynetbee.com/internet-of-things/switch-from-voice-assist.php", data={'pinno': '2','sts':'1'})
        print(response)
    elif "light off" in text.lower() or "lights off" in text.lower():
        print("I'll turn off the fan.")
        response = requests.post("https://www.skynetbee.com/internet-of-things/switch-from-voice-assist.php", data={'pinno': '2','sts':'0'})
        print(response)
    elif "bulb on" in text.lower() or "bulb on" in text.lower():
        print("I'll turn off the fan.")
        response = requests.post("https://www.skynetbee.com/internet-of-things/switch-from-voice-assist.php", data={'pinno': '3','sts':'1'})
        print(response)
    elif "bulb off" in text.lower() or "bulb off" in text.lower():
        print("I'll turn off the fan.")
        response = requests.post("https://www.skynetbee.com/internet-of-things/switch-from-voice-assist.php", data={'pinno': '3','sts':'0'})
        print(response)
def recognize_continuous():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                audio_data = recognizer.listen(source, timeout=5)
                print("Recognizing...")
                text = recognizer.recognize_google(audio_data)
                print(f"You said: {text}")
                if process_speech(text):
                    break
            except sr.WaitTimeoutError:
                print("Speech recognition timed out. No speech detected.")

            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")

            except sr.RequestError as e:
                print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    recognize_continuous()