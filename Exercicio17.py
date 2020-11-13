"""
Exercício 17

Nome: Par ou Ímpar: Funções
Objetivo: Escrever uma função chamada numero_par que recebe um número e torna True caso ele seja par ou False caso
        seja ímpar
Dificuldade: Principiante

Crie uma função chamada 'numero_par(numero)' que receba um número como argumento e retorne True caso ele seja par ou
    False caso seja ímpar
"""

def numero_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = float(input("Digite um numero: "))
print(numero_par(numero))
