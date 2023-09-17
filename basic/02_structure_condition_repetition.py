"""
    O Fatorial de um número inteiro é representado pela multiplicação de todos os números predecessores maiores que 0. Por exemplo, o fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5. Escreva um código que calcule o fatorial de um número inteiro.
"""
number = 7
factorial = number
accumulator = 1
while factorial > 0:
    accumulator *= factorial
    factorial -= 1
print(accumulator)


"""
    Um sistema de avaliações registra valores de 0 a 10 para cada avaliação. Após algumas mudanças estes valores precisam ser ajustados para avaliações de 0 a 100. Dado uma sequência de avaliações ratings = [6, 8, 5, 9, 10]. Escreva um código capaz de gerar as avaliações após a mudança. Neste caso o resultado deveria ser [60, 80, 50, 90, 100].
"""
assessments = [6,8,5,9,10]
multiple = 10
for index, point in enumerate(assessments):
    assessments[index] = point*multiple
print(assessments)


# Percorra a lista do exercício 13 e imprima “Múltiplo de 3” se o elemento for divisível por 3.

for number in assessments:
    if number % 3 == 0:
        print(f'{number} é multiplo de 3')