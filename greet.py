from gtts import gTTS
import os

#When face detect after 5am Then this function starts
def greet(username):
    tts = gTTS(text='Good morning ' + username, lang='en')
    tts.save("good.mp3")
    os.system("good.mp3")
