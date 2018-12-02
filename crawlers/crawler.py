import bs4
import requests, time

def getData(thread, source):
    soup = bs4.BeautifulSoup(source, 'lxml')  # Converte o HTML em uma classe da biblioteca beautifulsoup4

    final_result=[]
    temp_source = soup.find('p', class_='error')
    if temp_source is not None and 'doesn\'t seem' in temp_source.text: # Checa se a página é válida
        result = {}
        result['erro'] = '{} não é uma thread válida!'.format(thread)
        final_result.append(result)
        return final_result

    for div in soup.find_all('div', class_='thing'):
        votes = div.find('div', class_='score unvoted').get('title')  # Votos da thread
        
        if votes:
            votes = int(votes)
        else:
            votes = 0

        if votes > 5000:
            entry_voted = div.find('div', class_='entry unvoted')
            title = entry_voted.find('p', class_='title')  # Título da thread
            comments_link = entry_voted.find('li', class_='first')
            comments_link = comments_link.find('a').get('href')  # Link dos comentários da thread
            link = title.find('a').get('href') # Link da thread

            # Se o link pertencer ao próprio reddit o endereço do site não é mostrado
            if link.startswith('/r/'):
                link = 'https://old.reddit.com' + link

            if comments_link.startswith('/r/'):
                comments_link = 'https://old.reddit.com' + link

            result = {}
            result['erro'] = ''
            result['votos'] = str(votes)
            result['subreddit'] = thread
            result['titulo'] = title.text
            result['link_comentarios'] = comments_link
            result['link_thread'] = link
            final_result.append(result)
    
    return final_result

def returnInfos(threadList):
    if not threadList:       # Checa se a threadlist está vazia
        raise ValueError
    
    threadList = threadList.split(';')   # Separa as threads por ";"
    
    final_result = []
    for thread in threadList:
        thread = thread.replace(' ', '')  # Remove todos os espaços do nome da thread

        invalid_chars = [
            '!', '@', '#', '$', 
            '%', '&', '*', '(', 
            ')', 'ª', 'º', '§', 
            ':', ']', '[', '{', 
            '}', '?', '"', "'"
        ]
        for char in invalid_chars:
            if char in thread:      # Verifica se há caracteres inválidos no nome da thread
                raise ValueError  

        source = requests.get('https://old.reddit.com/r/{}/'.format(thread)) # O código da linha 60 até 63 é uma emulação do loop "do while" presente em linguagens como C# e Java
        while source.status_code == 429:
            time.sleep(3)
            source = requests.get('https://old.reddit.com/r/{}/'.format(thread))
            
        final_result.append(getData(thread, source.text))  # Pega as informações e adiciona na lista de respostas
    
    return final_result