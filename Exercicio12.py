"""
Exercício 12

Nome: Praticando Funções
Objetivo: Escrever diversas funções para reaproveitar trechos de código
Dificuldade: Intermediário

Escreva um código de modo que exiba o valor do x digitado pelo usuário e que seja
substituído nas funções.
1 - Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).
2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável de R$ 2,00 por unidade
    produzida. Sendo x o número de peças unitárias produzidas, determine o custo de produção de 100 peças.
3 - Crie uma função que receba 2 números e retorne o maior valor.
4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.
5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da soma de f(9) + g(2).
    Depois crie um código que retorne o valor da soma das duas funções com números digitados pelo usuário.
6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1. Qual é o valor da função composta g(f(3))?
    Depois crie um código que retorne o valor da soma das duas funções com números digitados pelo usuário.
7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6. Exiba 10 números sorteados
    utilizando a mesma função criada.
    Números aleatórios: random.randint(inicio, fim)
"""
# ============ 1 - Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).================================================
lista_x = (5, 0)

print(f"\nf(x) = 3 * x - 2")
for x in lista_x:
    print(f"\nf({x}) = 3 * {x} - 2")
    print(f"f({x}) = {3 * x - 2}")

# ================================ 2 - determine o custo de produção de 100 peças ======================================
custo_fixo = 30.00
custo_variavel = 2
x = 100

f = custo_fixo + x * custo_variavel
print(f"\nCusto de produção de {x} peças: {f:.2f}R$".replace('.', ','))


# ================================ 3 - Crie uma função que receba 2 números e retorne o maior valor.====================
def maior(n1=-99999999, n2=-9999999, n3=-999999):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n2 and n3 > n2:
        return n3
    else:
        return f"Os numeros são iguais"


n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 1º numero: "))
n_maior = maior(n1, n2)

print(f"\nO maior numero entre {n1} e {n2} é {n_maior}")

# ============ 4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.=============
n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
n3 = float(input("Digite o 3º numero: "))
n_maior = maior(n1, n2, n3)
print(f"\nO maior numero entre ({n1}, {n2}, {n3}) é {n_maior}")


# ===== 5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da soma de f(9) + g(2).===

def soma_funcao(x, x2):
    f = x - 5
    g = 3 * x2 + 1

    soma = f + g

    print(f"\nf(x) = x - 5")
    print(f"f({x}) = {x} - 5")
    print(f"f({x}) = {f}")

    print(f"\ng(x) = 3 * x + 1")
    print(f"g({x2}) = 3 * {x2} + 1")
    print(f"g({x2}) = {g}")

    print(f"\nf({x}) + g({x2}) = {soma}")


soma_funcao(9, 2)

x = float(input("\nDigite o valor de x para f(x): "))
x2 = float(input("Digite o valor de x para g(x): "))
soma_funcao(x, x2)


# === 6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1. Qual é o valor da função composta g(f(3))? =====

def soma_funcao2(x):
    f = x - 4
    g = 5 * f + 1

    print(f"\nf(x) = x - 4")
    print(f"f({x}) = {x} - 4")
    print(f"f({x}) = {f}")

    print(f"\ng(x) = 5 * x + 1")
    print(f"g(f(x)) = 5 * f(x) + 1")
    print(f"g(f{x}) = 5 * f{(x)} + 1")
    print(f"g(f{x}) = 5 * {f} + 1")
    print(f"g(f{x}) = {g}")


soma_funcao2(3)

x = float(input("\nDigite o valor de x para f(x): "))
soma_funcao2(x)


# ============== 7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6 ==============
def dado():
    import random

    return random.randint(1, 6)


i = 0
while i < 10:
    print(f"\nNumero sorteado: {dado()}")
    i += 1
