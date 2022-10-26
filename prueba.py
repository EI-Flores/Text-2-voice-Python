# pip install gTTS

from gtts import gTTS
tts = gTTS('Hola, mi nombre es Juan, y esta es una prueba de programación', lang='es', tld='com')
tts.save('hello.mp3')