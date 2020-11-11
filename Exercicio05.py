"""
Exercício 5

Nome: Par ou Ímpar
Objetivo: Receber um número do usuário e informar se ele é par ou ímpar.
Dificuldade: Principiante

1 - Crie um programa que receba do usuário um número;
2 - Caso o número seja par, exibir a mensagem no console "O número {numero} é par.";
3 - Caso contrário, exibir a mensagem "O número {numero} é ímpar.".
"""
def Exercicio05():
    numero = int(input("Digite o numero: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

Exercicio05()