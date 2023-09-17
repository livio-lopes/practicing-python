# Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical. Exemplo:


def input_name():
    name = input("Escreva o seu nome: ")
    for letter in name:
        print(letter)


# get_name_input()

"""
    Escreva um programa que receba vários números naturais e calcule a soma desses valores. Caso algum valor da entrada seja inválido (por exemplo uma letra), uma mensagem deve ser exibida na saída de erros no seguinte formato: “Erro ao somar valores, {valor} é um valor inválido”. Ao final, você deve imprimir a soma dos valores válidos.

    🦜 Receba os valores em um mesmo input, solicitando à pessoa usuária que separe-os com um espaço. Receba os valores no formato str e utilize o método split para pegar cada valor separado. O método isdigit, embutido no tipo str, pode ser utilizado para verificar se a string corresponde a um número natural.
"""


def sum_input():
    numbers = input("Digite a lista de numeros separando por espaço: ")
    numbers = numbers.split()
    accumulator = 0
    for number in numbers:
        if number.isdigit():
            accumulator += int(number)

        else:
            print(f"Erro ao somar valores, {number} é um valor inválido")
    print(accumulator)


sum_input()
