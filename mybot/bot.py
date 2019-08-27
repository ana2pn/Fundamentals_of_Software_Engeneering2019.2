from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('NiceBot')

texto = open("conversa.txt",'r')
texto = texto.readlines()

trainer = ListTrainer(bot)
trainer.train(texto)

while True:
    try:
        print("Olá, meu nome é NiceBot estou aqui para te ajudar o que você gostaria de saber?")
        print("(Para sair do chat, pressione Ctrl+c)")
        for i in texto:
            quest = input("Você: ")
            resposta = bot.get_response(quest)
            print('Bot: ',resposta)
    except(KeyboardInterrupt, EOFError, SystemExit):break
