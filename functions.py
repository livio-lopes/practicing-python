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

# Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.


def type_triangule(a, b, c):
    if not a or not b or not c:
        return "Não é tringulo"
    if a == b and a == c:
        return "Triângulo Equilátero: três lados iguais"
    if a == b or a == c:
        return "Triângulo Isósceles: quaisquer dois lados iguais"
    return "Triângulo Escaleno: três lados diferentes"


test = [3, 3, 0]

# Dada uma lista, descubra o menor elemento. Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.

test = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]

def min(list_numbers):
    min_number = list_numbers[0]
    for number in list_numbers:
        if(number < min_number):
            min_number = number
    return min_number

# Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um triângulo retângulo com n asteriscos de base. Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:

def asterisk_triangule(n):
    if n > 1:
        for number in list(range(1,n+1,1)):
            print(number * "*")

# Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N. Por exemplo, para N = 5, o valor esperado será 15.

def sum(n):
    accumulator= 0
    for number in list(range(1,n+1)):
        accumulator+=number
    return accumulator

"""
    Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
    - Até 20 litros, desconto de 3% por litro;
    - Acima de 20 litros, desconto de 5% por litro.
    Gasolina:
    - Até 20 litros, desconto de 4% por litro;
    - Acima de 20 litros, desconto de 6% por litro.
    Escreva uma função que receba o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A - álcool, G - gasolina), e retorne o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço do litro do álcool é R$ 1,90.
"""

def fuel_sold(type, liters):
    price = {
        'gasoline': 2.5,
        'alcohol': 1.9
    }
    discount = {
        "alcohol": [0.03, 0.05],
        "gasoline": [0.04, 0.06]
    }
    MINIMUM_LITERS = 20
    
    match type:
        case 'A':
            if(liters > MINIMUM_LITERS):
                cost = liters * price['alcohol']*(1-discount['alcohol'][1])
                return f'{cost:.2f}'
            cost = liters * price['alcohol']*(1-discount['alcohol'][0])
            return f'{cost:.2f}'
        case 'G':
            if(liters > MINIMUM_LITERS):
                cost = liters * price['gasoline']*(1-discount['gasoline'][1])
                return f'{cost:.2f}'
            cost = liters * price['gasoline']*(1-discount['gasoline'][0])
            return f'{cost:.2f}'

test_fuel = 'G'
test_liters = 21
print(fuel_sold(test_fuel, test_liters))