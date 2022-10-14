#Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    if resposta == 1:
        #opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)