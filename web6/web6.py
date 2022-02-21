# Vamos usar uma re (regular expression) para localizar imagens em uma página web
# Ao inspeiconar a página (Ctrl + Shift + i) localizei que em cada linha<tr> da tabela, possui 
# no final uma coluna <td> com uma imagem <img src="../img/gifts/img.jpg "> 
#Assim ficará mais fácil localizar por meio de uma re

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'html.parser')
imagens = bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for imagem in imagens:
    print(imagem['src'])



