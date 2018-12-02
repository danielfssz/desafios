from crawler import returnInfos
import telepot
bot = telepot.Bot("748982821:AAE4ETfCXsgLAicrjPzQP3SEgDdwS7q1fOA")

def recebendoMsg(msg):
    if '/nadaparafazer' in msg['text']:
        parameters = msg['text'][14:]

        chatID = msg['chat']['id']

        try:
            result = returnInfos(parameters)
            for subreddit in result:
                for thread in subreddit:
                    if thread['erro']:
                        bot.sendMessage(chatID, thread['erro'])
                    else:
                        response = "Votos: {}\nSubreddit: {}\nTítulo: {}\nLink dos comentários: {}\nLink da thread: {}".format(thread['votos'], thread['subreddit'], thread['titulo'], thread['link_comentarios'], thread['link_thread'])
                        bot.sendMessage(chatID, response)
        except ValueError:
            bot.sendMessage(chatID, 'Erro de síntaxe!')

bot.message_loop(recebendoMsg)

while True:
    pass