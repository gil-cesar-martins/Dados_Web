# Ao utilizar uma tecnica de rastreamento(crawling) estaremos exibindo o título, o primeiro parágrafo dos contéudos
# e caso, contenha um link para edição da página, ele também será exibido.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0]) # Imprime o primeiro parágrafo do texto
        print(bs.find(id='ca-edit').find('span')               # Imprime links para edição (páginas de artigos)
        .find('a').attrs['href'])
    except AttributeError:
        print('Esta página está faltando algo! Continuando a busca...')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #Encontramos uma página nova
                newPage = link.attrs['href']
                print('-'*20)
                print('\n')
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
                
getLinks('')