"""
Exercício 3

Nome: Input de Informações
Objetivo: Receber dados do usuário, trabalhar com os valores e exibir para o usuário.
Dificuldade: Principiante

1 - Crie um programa que receba do usuário seu nome, idade e gênero;
2 - Exiba na tela seguinte mensagem: "Olá, {nome}, você possui {idade} anos de idade e é do gênero {genero}. Já pensou no que você fará no seu aniversário de {idade + 1} anos?".
"""

def Exercicio03():
    nome   = str(input("Digite o nome: \t "))
    idade  = str(input("Digite a idade:  "))
    genero = str(input("Digite o gênero: "))

    print(f"\nOlá, {nome}, você possui {idade} anos de idade e é do gênero {genero}")

Exercicio03()