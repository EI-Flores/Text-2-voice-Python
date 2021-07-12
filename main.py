#pip install gTTS
#https://gtts.readthedocs.io/en/latest/_modules/gtts/lang.html#tts_langs

# Importamos el paquete
from gtts import gTTS 
 
  
# Texto a convertir en audio 
 
mytext = "Hola, saludos desde Facialimi equipo"
 
  
# Realizamos la conversión del texto a voz 
tts = gTTS(text=mytext, lang=es-us, slow=False) 
 
  
# Finalmente guardamos el archivo de Audio
 
tts.save("facialix.mp3") 