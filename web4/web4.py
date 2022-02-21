# Se tentarmos acessar uma tag inexistente teremos um objeto None, que gera um AttributeError mas e se a tag não 
# apresentar exatamente aquilo que desejamos? Podemos tratar da seguinte maneira

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def vericarTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as errado:
        return None
    try:
        bs = BeautifulSoup(html,'html.parser')
        titulo = bs.body.h1
    except AttributeError as errado:
        return None
    return titulo

titulo = vericarTitulo('https://rollingstone.uol.com.br')
if titulo == None:
    print('Title could not be found')
else:
    print(titulo)
