#Ler 2 números de um alunos. Calcular a média e exibir se o aluno foi aprovado ou reprovado ou aonde se está de exame. Se a média for maior ou igual a 6,0 o aluno estará aprovado, caso contrário se a média for igual a 4,0 mas menor que 6,0 então o aluno estará de exame. Caso contrário estará reprovado.


print("=" * 30)
print("Média dos Alunos")
print("=" * 30)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2) / 2

if media < 4:
    print("O aluno está reprovado")
elif media >= 4 and media < 6:
    print("O aluno está de exame")
else:
    print("Aluno Aprovado")

