"""
Exercício 10

Nome: A de Amor, B de Baixinho
Objetivo: Receber o nome, extrair a primeira letra e fazer comparações.
Dificuldade: Principiante

1 - Escreva um programa que receba o nome de uma pessoa;
2 - Extraia a primeira letra do nome;
3 - Compare a primeira letra de modo que, caso seja "A", exiba na tela "A de Amor", caso seja "B", exiba na tela
    "B de Baixinho", caso contrário, exiba na tela "Seu nome não é legal.";
4 - Faça com que o programa funcione independe se for digitado um nome com letras minúsculas ou maiúsculas.
"""

def Exercico10():
    nome = str(input("\nDigite o nome:")).lower()

    if nome[0] == 'a':
        print("\nA de Amor")
    elif nome[0] == 'b':
        print("\nB de Baixinho")
    else:
        print("\nSeu nome não é legal.")

Exercico10()