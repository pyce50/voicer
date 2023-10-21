import gtts
from playsound import playsound

try:
    tts = gtts.gTTS("Hello, it's a simple voicer by Pyce", lang="en")
    tts.save("test.mp3")
    playsound("test.mp3")
except:
    print("error()")