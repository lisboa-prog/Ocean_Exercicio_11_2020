"""
Exercício 13
Nome: Convertendo Celsius/Farenheit
Objetivo: Escrever duas funções de conversão, uma de graus celsius em farenheit e a outra que faça o contrário.
Dificuldade: Principiante
1 - Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit.
2 - Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão
    escolhida é realizada.
3 - Se C é a temperatura em Celsius e F em Farenheit, as fórmulas de conversão são:
F = (9 * C / 5) + 32
C = 5 * (F - 32) / 9
K = C + 273
"""

def pegar_numero(texto):
    try:
        numero = float(input(texto))
    except ValueError:
        return False
    return numero


def escolha_escala(lista=0):
    contador = 0
    escala = 0
    while contador == 0:
        escala = pegar_numero("Digite o valor da Escala: ")
        if escala != False:
            if escala in lista:
                new_escala = escala
                contador = 1
            else:
                print("ERRO")
                contador = 0
    return new_escala


def escolha_temperatura():
    contador = 0
    temperatura = 0
    while contador == 0:
        temperatura = pegar_numero("\n\nDigite o valor da TEMPERATURA: ")
        if temperatura != False:
            new_temperatura = temperatura
            contador = 1
        else:
            print("\nERRO!!")
            contador = 0
    return new_temperatura


def Exercicio13():

    lista_de_escalas = [1, 2, 3]
    lista_de_saida = [0, 1]
    saida = 0

    T = escolha_temperatura()

    if escolha_escala(lista_de_escalas) == 1:
        print(f"Temperatura Convertida = {(9 * T / 5) + 32}ºF")
    elif escolha_escala(lista_de_escalas) == 2:
        print(f"Temperatura Convertida = {5 * (T - 32) / 9}ºC")
    elif escolha_escala(lista_de_escalas) == 3:
        print(f"\nTemperatura Convertida = {T + 273}ºK")

    saida = pegar_numero("\nDigite:\n[0]zero para SAIR\n[1]um para CONTINUAR'\nEscolha: ")

    if saida !=0 :
        Exercicio13()
    else:
        print("\n\nOBRIGADO!!\n")

Exercicio13()