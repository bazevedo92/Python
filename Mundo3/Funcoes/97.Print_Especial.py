#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                                                                        escreva(‘Olá, Mundo!’) Saída:                                                                                                                          ~~~~~~~~~                                                                                                                                                            Olá, Mundo!                                                                                                                                                          ~~~~~~~~~

def escreva(msg):
    tam = len(msg)
    print("-=" * tam)
    print(f"  {msg}")
    print("-=" * tam)


escreva("Beatriz Azevedo")
escreva("teste")
escreva("Beatriz Azevedo escreva Beatriz Azevedo")