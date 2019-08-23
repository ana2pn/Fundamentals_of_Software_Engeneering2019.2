from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('test')

conversa = ['Oi','Olá','E aí, tudo bem?','tudo bem sim, e você?','Eu estou bem', 'Que bom!', 'O que você gosta de fazer?','Eu gosto de aprender a programar', 'Que linguagem de programação você mais gosta?', 'Eu gosto de python e gosto de Java','Quais filmes você mais gosta?']
trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    quest = input("Você: ")
    resposta= bot.get_response(quest)
    print('bot: ',resposta)
