from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('test')

texto = open("conversa.txt",'r')
texto = texto.readlines()
trainer = ListTrainer(bot)
trainer.train(texto)

while True:
    for i in texto:
        quest = input("Você: ")
        resposta = bot.get_response(quest)
        print('Bot: ',resposta)
