from ex115.lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome, "rt")    #rt = read and text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, "wt+") #WT+ = Write Text criar
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print("Arquivo criado com sucesso")


def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(a.read())


