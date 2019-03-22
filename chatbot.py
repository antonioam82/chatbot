from chatterbot import ChatBot
import win32com.client as wc
#from chatterbot.trainers import ChatterBotCorpusTrainer 
#from chatterbot.trainers import ListTrainer 
#chatbot = ChatBot( "Ejemplo de bot" ) 
#trainer = ChatterBotCorpusTrainer(chatbot) 
#trainer.train( "chatterbot.corpus.spanish" )
speak=wc.Dispatch("Sapi.SpVoice")
chatbot = ChatBot(

    "Ejemplo Bot",
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

while True:
    usuario = input(">>> ")
    respuesta = chatbot.get_response(usuario)
    speak.Speak(respuesta)
    print("BOT: "+str(respuesta))
