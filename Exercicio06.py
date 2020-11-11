"""
Exercício 6

Nome: Catapulta
Objetivo: Receber o número de baterias e duração da bateria e calcular a quantidade de pedras que a catapulta irá soltar.
Dificuldade: Principiante

1 - Uma catapulta lançou 300 pedras em 5 baterias de 15 minutos, cada.
2 - Quantas pedras ela lançaria em 8 baterias de 7 minutos, cada?
3 - Crie um programa que receba os valores base para que a aplicação funcione de forma que, se alterarmos o número de
    baterias e a duração de cada bateria, o programa funcione sem precisar de mais modificações.
"""
def Exercicio06():
    lancamento_base = 300 / (5 * 15)

    bateria = int(input("Digite o numero de Bateria:"))
    tempo = int(input("Digite o tempo em minutos:"))

    lancamento = lancamento_base * bateria * tempo

    print(f"\nO numero de pedras lançada em {bateria} baterias de {tempo} minutos é {int(lancamento)}")

Exercicio06()