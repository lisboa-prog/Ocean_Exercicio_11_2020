"""
Exercício 11

Nome: Votação: Zona Eleitoral
Objetivo: Receber a idade da pessoa e, caso seja maior ou igual a 16 anos, pergunta a zona onde a pessoa mora e exibe
        a escola de votação.
Dificuldade: Principiante

1 - Escreva um programa que:
2 - Pergunte a idade da pessoa e, caso tenha menos do que 16 anos, informe que a pessoa não vota.
3 - Caso contrário, pergunte a zona onde a pessoa mora (zona oeste, leste, norte, sul ou centro) e exibe o local de
    votação de acordo com as regras a seguir:
4 - Pessoas que moram na zona oeste e zona norte votam na escola A.
5 - Pessoas que moram na zona leste votam na escola B.
6 - Pessoas que moram na zona sul ou no centro votam na escola C.
7 - Certifique-se de que seu código funciona mesmo que a pessoa digite: 'Oeste, OESTE ou oeste', por exemplo.
"""


def Exercicio11():
    zonas_eleitoral = ('oeste', 'leste', 'norte', 'sul', 'centro')
    escolas = ('Escola A', 'Escola B', 'Escola A', 'Escola C', 'Escola C')

    idade = int(input("Digite o sua idade: "))

    if idade < 16:
        print("\nVocê não vota")
    else:
        zona_do_usuario = str(input("Digite sua ZONA eleitoral: ")).lower()

        if zona_do_usuario in zonas_eleitoral:
            i = 0
            while zona_do_usuario != zonas_eleitoral[i]:
                i += 1
            print(escolas[i])
        else:
            print("Zona eleitoral fora da lista")


Exercicio11()
