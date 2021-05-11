import pyttsx3
#https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice

# Caminho do seu arquivo 
f = open('../files/test.txt', 'r', encoding="utf8")
texto = f.read()

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')

for voice in voices:
    print(voice, voice.id)
    
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-1000) 

print(texto)
speaker.say(texto) 
speaker.runAndWait() 
f.close() 
