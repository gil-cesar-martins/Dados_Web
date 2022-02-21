# Vamos tratar as exceções caso uma página não for encontrada (Error 404 Page not Found) ou o servidor possa 
# apresentar algum erro (500 Internal Server Error).

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('https://vouinventarumnomefalso.com.br')
except HTTPError as errado:
    print("The server returned an HTTP error")
except URLError as errado:
    print("The server could not be found")
else:
    print(html.read())