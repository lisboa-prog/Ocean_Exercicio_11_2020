"""
Exercício 8

Nome: Comparação de Números: Maior, Menor ou Igual
Objetivo: Receber dois números e exibir qual é maior, menor ou igual a quem.
Dificuldade: Principiante

1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Caso o {numero1} seja maior do que o {numero2}, exiba na tela: "O número {numero1} é maior do que o
    número {numero2}.";
3 - Caso contrário, se o {numero1} for menor, exiba: "O número {numero1} é menor que {numero2}.";
4 - Caso contrário, exiba: "O número {numero1} é igual ao número {numero2}.".
"""

def Exercicio08():

    numero1 = float(input("\nDigite o 1º valor: "))
    numero2 = float(input("Digite o 2º valor: "))

    if numero1 > numero2:
        print(f"\nO número {numero1} é maior que {numero2}")
    elif numero1 < numero2:
        print(f"\nO número {numero1} é menor que {numero2}.")
    else:
        print(f"O número {numero1} é igual ao número {numero2}")

Exercicio08()
