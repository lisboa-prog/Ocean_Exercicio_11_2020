"""
Exercício 19

Nome: Praticando: Listas/For (Loop)
Objetivo: Praticar a criação e a leitura básica de listas com números e textos.
Dificuldade: Intermediário

1 - Crie uma lista com alguns números inseridos manualmente (não há necessidade do usuário inseri-los).
2 - Crie um for que varra cada elemento da lista e exiba-o no console.
3 - Declare um novo for que exiba apenas os números maiores que 3.
4 - Declare um outro for que exiba apenas os números pares.
5 - Exiba na tela a soma de todos os elementos da lista sem a utilização de funções extras.
6 - Exiba a soma de todos os elementos utilizando a função sum().
7 - Crie uma nova lista a partir de números digitados pelo usuário, faça com que o usuário insira 10 números, porém,
    utilize o 'for' para isso, em vez de declarar 10 vezes o input de entrada de informação, declare apenas UMA vez e
    faça com que ele seja executado 10 vezes.
    A cada atualização da lista, exiba a quantidade de elementos que ela possui.
8 - Exiba apenas os três primeiros elementos da lista no console.
9 - Exiba apenas os três últimos elementos da lista no console.
10 - Declare uma nova lista vazia chamada 'nomes' e armazene 3 nomes digitados pelo usuário, ordene esses nomes por
    ordem alfabética e exiba-os na tela, um de cada vez.
"""
import heapq

lista = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]

for imp in lista:
    print(imp)

for imp in lista:
    if imp > 3:
        print(imp)
x = 0
for imp in lista:
    x = x + imp
print(x)

print(sum(lista))

lista2 = []
for imp in range(10):
    lista2.append(int(input("Digite um numero: ")))

print(lista2)

print(lista2[0:3])

print(lista2[7:])

lista3 = []
for imp in range(3):
    lista3.append(str(input("Digite um numero: ")))

for imp in sorted(lista3):
    print(imp)
