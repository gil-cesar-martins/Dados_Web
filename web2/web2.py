# Vamos extrair da página web a primeira instância de seu h1 e ver o que ele diz

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.maujor.com')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)