nome = input("Qual o seu nome? ")
dia = int(input("Você nasceu em que dia? "))
mes = int(input("Você nasceu em que mês? "))
ano = int(input("Você nasceu em que ano? "))
resultado = dia + mes

print('Olá,{}! Prazer em te conhecer!'.format(nome))
print("Você nasceu no dia {} de {} de {}. Correto?".format(dia, mes, ano))
print("A soma dos números é: {}".format(resultado))
print("A soma entre {} e {} vale: {}".format(dia, mes, resultado))
print(type(nome))
print(nome.isnumeric())
print(nome.isalpha())