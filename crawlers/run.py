from crawler import returnInfos

subreddits_list = input('Type a list of subreddits separated by ";"(programming;dogs;brazil):\n')
print('\n')

try:
    infos = returnInfos(subreddits_list)

    for subreddit in infos:
        for thread in subreddit:
            if thread['erro']:
                print(thread['erro'])
                print('______________________________________________________________________________________________\n')
            else:
                print('Votos: ' + thread['votos'])
                print('\nSubreddit: ' + thread['subreddit'])
                print('\nTítulo: ' + thread['titulo'])
                print('\nLink dos comentários: ' + thread['link_comentarios'])
                print('\nLink da thread: ' + thread['link_thread'])
                print('______________________________________________________________________________________________\n')
except ValueError:
    print("Erro de síntaxe!")