"""
Exercício 9

Nome: Checando Múltiplos
Objetivo: Receber dois números e exibir se um é múltiplo do outro ou não.
Dificuldade: Principiante

1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Se o {numero1} for múltiplo do {numero2} exiba na tela: "O número {numero1} é múltiplo do número {numero2}.";
3 - Caso contrário, exiba na tela: "O número {numero1} não é múltiplo do número {numero2}.";
"""

def Exercicio09():

    numero1 = float(input("\nDigite o 1º valor: "))
    numero2 = float(input("Digite o 2º valor: "))

    if numero1 % numero2 == 0:
        print(f"\nO número {numero1} é múltiplo do número {numero2}.")
    else:
        print(f"O número {numero1} não é múltiplo do número {numero2}.")

Exercicio09()
