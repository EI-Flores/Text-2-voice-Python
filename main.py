# pip install gTTS
# https://gtts.readthedocs.io/en/latest/_modules/gtts/lang.html#tts_langs

# Importamos el paquete
from gtts import gTTS 
 
  
# Texto a convertir en audio 
 
mytext = "Hola, ¿Cómo estás?, mi nombre es Juan y este es un ejemlo de texto a voz"
 
  
# Realizamos la conversión del texto a voz 
tts = gTTS(text=mytext, lang=es-ar, slow=False) 
 
  
# Finalmente guardamos el archivo de Audio
 
tts.save("facialix.mp3") 