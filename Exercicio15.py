"""
Exercício 15

Nome: Gastos da Viagem
Objetivo: Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e
        gastos extras de uma viagem para uma determinada cidade.
Dificuldade: Intermediário

Hospedagem
1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total
    do hotel, sendo que 1 noite custa R$ 140,00.

Passagem
2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que
    passagem para:
- São Paulo custa R$ 312,00;
- Porto Alegre custa R$ 447,00;
- Recife custa R$ 831,00;
- Manaus custa R$ 986,00.

Aluguel de Carro
3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
- Calcule o custo do aluguel do carro sendo que:
- A cada dia o carro custa R$ 40,00;
- Alugando 7 dias ou +: R$ 50,00 de desconto;
- Alugando 3 dias ou +: R$ 20,00 de desconto;
- Você pode receber apenas um desconto;
- Retorne o custo.

Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo
    total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!

Gastos Extras
5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da
    viagem.
Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.
"""


# Hospedagem
def custo_hotel(noites):
    diaria = 140
    return diaria * noites


# Passagem
def custo_aviao(cidade):
    lista_cidade = {'são Paulo': 312.00, 'porto alegre': 447.00, 'recife': 831.00, 'manaus': 986.00}

    if cidade in lista_cidade:
        return lista_cidade[cidade]
    else:
        return f"0.00R$, Cidade Invalida"


# Aluguel de Carro
def custo_carro(dias):
    custo_diaria = 40
    desc_2d = 20
    desc_7d = 50

    if dias < 3:
        return dias * custo_diaria
    elif dias < 7:
        return dias * custo_diaria - desc_2d
    elif dias > 7:
        return dias * custo_diaria - desc_7d
    else:
        return f"00,00R$ - dias invalidos"


# Cálculo Total
noites = int(input("Noites: "))
cidade = str(input("Digite o nome da cidade:")).lower()
dias = int(input("Digite a quantidade de dias: "))

custo_total_hotel = custo_hotel(noites)
custo_total_aviao = custo_aviao(cidade)
custo_total_carro = custo_carro(dias)

custo_total_viagem = custo_total_hotel + custo_total_aviao + custo_total_carro
print(
    f"\nConta 1:\nHotel: {custo_total_hotel:.2f}R$\nAvião: {custo_total_aviao:.2f}R$\nCarro: {custo_total_carro:.2f}R$"
    f"\n\n"f"Total: {custo_total_viagem:.2f}R$\n\n".replace('.', ','))

# Gastos Extras
gastos_extras = int(input("Digite os gastos_extras: "))
custo_total_viagem = custo_total_hotel + custo_total_aviao + custo_total_carro + gastos_extras

print(
    f"\n\nConta com gasto extra:\nHotel: {custo_total_hotel:.2f}R$\nAvião: {custo_total_aviao:.2f}R$"f"\nCarro: {custo_total_carro:.2f}R$\ngastos_extras: {gastos_extras:.2f}R$\n\nTotal: {custo_total_viagem:.2f}R$ ".replace(
        '.', ','))
