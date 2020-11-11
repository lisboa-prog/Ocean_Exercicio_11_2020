lista = [1, 2]


def isNumber(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def pegar_numero(texto):
    try:
        numero = int(input(texto))
    except ValueError:
        return False
    return numero


def teste1():

    escala = pegar_numero("Digite o valor da Escala: ")
    new_escala = escala

    if escala != False:
        if escala in [1, 2]:
            new_escala = escala
            # teste()
            print(f"variavel escala if =  {new_escala} é {type(new_escala)}")
        else:
            new_escala = 0
            teste()
 #   print(f"variavel new_escala =  {new_escala[escala]} é {type(new_escala[escala])}")
 #    new_escala = escala
    new_escala = 0
    new_escala = escala
    print(f"variavel escala fim =  {new_escala} é {type(new_escala)}")
    return new_escala

def teste(lista=0):
    contador = 0
    escala = 0
    while contador == 0 :
        escala = pegar_numero("Digite o valor da Escala: ")
        if escala != False:
            if escala in lista:
                new_escala = escala
                contador = 1
            else:
                print("ERRO")
                contador = 0
    return new_escala


x = teste(lista)
print(f"variavel x = {x} é {type(x)}")
