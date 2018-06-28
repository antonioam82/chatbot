import time
import win32com.client as wc
import random
from conversaciones import despedidas
#CHAT-BOT
speak=wc.Dispatch("Sapi.SpVoice")

a=input("Escribe algo: ")
momento=time.localtime()
if momento[3]>=12 and momento[3]<22:
    print("GOOD AFTERNOON");speak.Speak("good afternoon")
elif momento[3]>=1 and momento[3]<12:
    print("GOOD MORNING");speak.Speak("good morning")
elif momento[3]>=22 and momento[3]<=23:
    print("GOOD NIGHT");speak.Speak("good night")
texto=("")
while texto!=("see you") and texto!=("bye bye") and texto!=("good bye"):
    texto=input("Texto: ")
    texto=texto.lower()


despedida=random.choice(despedidas)
speak.Speak(despedida)
