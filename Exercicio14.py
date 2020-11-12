"""
Exercício 14

Nome: Média Escolar
Objetivo: Escrever uma aplicação utilizando funções que calcule a média de um aluno.
Dificuldade: Intermediário

1 - Um professor, muito legal, fez 3 provas durante um semestre mas só vai levar em conta as duas notas mais altas para
    calcular a média.
2 - Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as
    2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.
"""
import heapq # biblioteca de arvore binária
import statistics # biblioteca de estatisticas

n1 = float(input("Digite o valor da 1ª nota: "))
n2 = float(input("Digite o valor da 2ª nota: "))
n3 = float(input("Digite o valor da 3ª nota: "))

lst = [n1, n2, n3]

maior = heapq.nlargest(2,lst)
media = statistics.mean(maior)
print(f"maiores notas {maior}, a media é {media:.2f}".replace('.',','))

