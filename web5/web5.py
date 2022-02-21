# O CSS nos ajuda muito na estilização de páginas web e o uso das classes para distinguir uma propriedade de outra
# se encaixa como uma luva para que um web scraper separe as tags de acordo com as classes.add()

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html,'html.parser')

# Nessa página todas as frases ditas pelos personagens estão em vermelho e assim o desenvolvedor usou <span class="red"> na estilização
#vamos exibi-las

nameListRed = bs.findAll('span',{'class':'red'})
for frase in nameListRed:
    print('\n')
    print(frase.get_text())

print('\n-------------------------------------------------------------------------------\n')

# O desenvolvedor usou <span class="green"> para estilizar os nomes dos personagens de verde
#vamos exibi-los 

nameListGreen = bs.findAll('span',{'class':'green'})
for name in nameListGreen:
    print(name.get_text())
    
print('\n-------------------------------------------------------------------------------\n')

# Vamos descobrir quais são os títulos presentes na página

titulos = bs.find_all(['h1','h2','h3','h4','h5','h6'])
print([titulo for titulo in titulos])

print('\n-------------------------------------------------------------------------------\n')

# Vamos ver quantas vezes aparece o nome 'Anatole' em toda a página

nomes = bs.find_all(text='Anatole')
print(len(nomes))