"""
Exercício 7

Nome: Arredondando para Múltiplos
Objetivo: Receber dois números e arredondar o primeiro número para o número mais próximo do múltiplo do segundo número.
Dificuldade: Principiante

1 - Receba dois números, o primeiro na variável 'numero' e o segundo na variável 'multiplo'.
2 - Arredonde para baixo o valor do primeiro número levando em consideração que o resultado deve ser múltiplo do segundo
    número.
Exemplo:
    Supondo que o primeiro número seja 72 e o segundo número seja 10, o resultado será 70.
    Se o primeiro número for 97 e o segundo número for 10, o resultado será 90.
"""
def Exercicio07():
    import math

    numero1 = float(input("\nDigite o 1º valor: "))
    numero2 = float(input("Digite o 2º valor: "))

    if numero1 > numero2:
        num_arrendondado = round(numero1 / 10, 0)
        print(f"\nArredondamento: {num_arrendondado * 10}")
    elif numero1 < numero2:
        num_arrendondado = math.ceil(numero1 / 10)
        print(f"\nArredondamento: {num_arrendondado * 10}")
    else:
        print(f" erro valores identicos")

Exercicio07()