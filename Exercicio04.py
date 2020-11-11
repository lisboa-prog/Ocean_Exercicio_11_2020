"""
Exercício 4

Nome: Data e Hora
Objetivo: Formatar a Data e Hora baseado em valores obtidos da biblioteca datetime e também valores informados pelo usuário.
Dificuldade: Intermediário

1 - Declare as variáveis para obter a data e a hora atual (dia, mês, ano, hora, minuto e segundo);
2 - Exiba essa informação para o usuário, devidamente formatada no formato "{DD}/{MM}/{AAAA} - {HH}h{MM}'{SS}".
3 - Peça para o usuário informar separadamente um dia, mês e ano e exiba no console
4 - Utilizando as informações digitadas pelo usuário, construa um objeto do tipo datetime.
5 - Exiba o a data fornecida, juntamente com o dia da semana correspondente, exemplo: {DD}/{MM}/{AAAA} - Dia da Semana:
    {data.weekday()}. OBS.: O dia da semana será exibido em inteiro, onde Segunda = 0 e Domingo é 6.
6 - Calcule a diferença entre as duas datas e exiba a quantidade em dias, exemplo: 'diferenca = data1 - data 2',
    print(diferenca.days)

Dica: Consulte a documentação em caso de dúvidas na manipulação do objeto datetime, como por exemplo a criação de um
    objeto datetime baseado em um dia, mês e ano personalizado.
    Link para a Documentação do Datetime: https://docs.python.org/3/library/datetime.html
    É possível criar um objeto do tipo datetime personalizado usando a seguinte declaração:
    data_personalizada = datetime(ano, mes, dia, hora, minuto, segundo)
    OBS.: Caso você tenha importado da seguinte maneira 'from datetime import datetime', a declaração acima funcionará.
    Caso você tenha importado apenas com 'import datetime', você precisará declarar 'data_personalizada = datetime.
    datetime(ano, mes, dia, hora, minuto, segundo)'.
    Você também pode criar uma data personalizada sem informar a hora, minuto e segundo, apenas informando os três
    primeiros parâmetros.
"""


def Exercicio04():
    # ======================== Declaração da biblioteca de datas e hora = datetime==========================================

    import datetime as dt

    # ========================1 a 3 - Declarar e exibir data de agora no formato "{DD}/{MM}/{AAAA} - {HH}h{MM}'{SS}"========

    agora = dt.datetime.now()

    print(f"\nData atual: {agora.day}/{agora.month}/{agora.year} - {agora.hour}h{agora.minute}'{agora.second}\n")

    # ========================4 - Objeto tipo datas ========================================================================

    DD = int(input("Informe a Data\nDia: "))
    MM = int(input("Mês: "))
    AA = int(input("Ano: "))

    data_usuario = dt.datetime.strptime(f"{DD}/{MM}/{AA}", '%d/%m/%Y')
    print(f"\nData informada pelo usuario: {data_usuario}\n")

    # ========================5 - Diferenças de datas ======================================================================
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    data = dt.datetime.today()
    print(f"Hoje é: {dias[data.weekday()]}\n")

    # ========================6 - Diferenças de datas ======================================================================
    DD = int(input("Informe a Data\nDia: "))
    MM = int(input("Mês: "))
    AA = int(input("Ano: "))
    data1 = dt.datetime.strptime(f"{DD}/{MM}/{AA}", '%d/%m/%Y')

    DD = int(input("Informe a Data\nDia: "))
    MM = int(input("Mês: "))
    AA = int(input("Ano: "))
    data2 = dt.datetime.strptime(f"{DD}/{MM}/{AA}", '%d/%m/%Y')

    diferenca_days = abs((data2 - data1).days)
    print(f"QDT dias: {diferenca_days}")


Exercicio04()
