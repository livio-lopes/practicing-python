import math


# Crie uma função que receba dois números e retorne o maior deles.
def higher_number(a, b):
    return a if a > b else b


# Calcule a média aritmética dos valores contidos em uma lista.
def average(list_numbers):
    accumulator = 0
    for number in list_numbers:
        accumulator += number
    return accumulator / len(list_numbers)


# Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:


def asterisk_multiplier(n):
    if n > 1:
        for number in list(range(n)):
            print(n * "*")


#  Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda".


def biggest_name(list_names):
    biggest = ""
    for name in list_names:
        if len(biggest) > len(name):
            pass
        else:
            biggest = name
    return biggest


test = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).


def calculate_cost_painting(square_meter, cost_can_paint=80, volume_can_paint=18):
    paint_yield = square_meter / 3
    number_cans_used = math.ceil(paint_yield / volume_can_paint)
    return f"""
Quantidade de latas necessárias: {number_cans_used},
Preço total: R$ {number_cans_used * cost_can_paint}
            """
test = 60


