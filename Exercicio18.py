"""
Exercício 18

Nome: Praticando: Funções Matemáticas
Objetivo: Escrever diversas funções que utilizem as funções matemáticas como base para trabalhar com números e praticar
        a formatação de números e strings.
Dificuldade: Principiante

1 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_maior_valor' utilizando o método
    '*args' e retorne o maior deles utilizando a função max()
2 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_menor_valor' utilizando o método
    '*args' e retorne o menor deles utilizando a função min()
3 - Peça para o usuário digitar 3 números positivos e 3 números negativos, extraia o módulo (versão positiva) de cada
    número utilizando a função abs() e exiba na tela o maior e o menor número (utilize as funções criadas anteriormente
    no exercício 1 e 2).
4 - Declare uma função que recebe um número e o formata de acordo com o tipo de sua variável (utilize a função type())
    - Se a variável for um float, formate-a como moeda, exemplo:
    - Entra a variável float 20.0 e exibe na tela R$ 20,00. Regra de formatação: {:.2f}, onde 2 representa o número e
     casas decimais.
    - Se a variável for um int, formate-a deixando com pelo menos 5 dígitos (colocando zeros na frente).
    Regra de formatação: {:02d}, onde 2 representa o número de dígitos.
    - Se a variável for uma string, formata-a para que utilize 10 espaços adicionais à esquerda.
    Regra de formatação: {:>1}, onde 1 representa o número de espaços que irá utilizar.
    - Caso a variável não seja nenhuma dessas, exiba a mensagem "Esse tipo de variável não está mapeado."
"""


def pegar_maior_valor(*args):
    x = max(args)
    return x


# n1 = float(input("Informe o 1º numero: "))
# n2 = float(input("Informe o 2º numero: "))
# n3 = float(input("Informe o 3º numero: "))
#
# print(pegar_maior_valor(n1, n2, n3))

#============================================================
def pegar_menor_valor(*args):
    return min(args)

# print(pegar_menor_valor(n1, n2, n3))

# ===============================================

def modulo(*args):
    x = [abs(arg) for arg in args]
    return pegar_maior_valor(*x)

# n=[]
# for i in range(6):
#     n.append(int(input(f"\nDigite o {i+1}º numero: ")))
#
# print(modulo(*n))

valor = input("Digite o valor: ")

if type(valor) == float:
    print(f"\nR$ {valor:.2f}".replace('.',','))
elif type(valor) == int:
    print(f"\n {valor:05d}")
elif type(valor) == str:
    print(f"\n {valor:>10}")
else:
    print(f"\nEsse tipo de variável não está mapeado.")
