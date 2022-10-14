#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não esta acessível no momento")
else:
    print("Consegui acessar o site Pudim com sucesso!")
    print(site.read()) #Pegar o conteudo HTML dentro do site que vc esta tentando acessar