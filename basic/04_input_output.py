import random
import json
import csv

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


# sum_input()

"""
    Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que:

    lê todas essas informações;
    aplique um filtro, mantendo somente as pessoas que estão reprovadas;
    escreva seus nomes em outro arquivo.
    Considere que a nota miníma para aprovação é 6.
"""


def select_approved(path_file="data/class_notes.txt"):
    list_approved = []
    with open(path_file, "r") as file:
        for line in file:
            name, note = line.split()
            if int(note) >= 6:
                list_approved.append(f"{name} {note}\n")
    with open("data/output/list_approved.txt", mode="w") as file:
        file.writelines(list_approved)


# Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida.


def print_inverted_staircase(word):
    for index in range(len(word)):
        print(word[: len(word) - index])


"""
    Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras e escolherá uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra. Ao final, a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo.

    🦜 Para embaralhar uma palavra faça: scrambled_word = "".join(random.sample(word, len(word)))

    🦜 O sorteio de uma palavra aleatória pode ser feito utilizando o método choice: random.choice(["word1", "word2", "word3"]) -> "word2".
"""


def scrambled_word(path_file):
    list_words = []
    if isinstance(path_file, str):
        with open(path_file) as file:
            list_words = file.read()
        list_words = list_words.split("\n")
    else:
        list_words = ["bode", "gigante", "amante", "batata"]
    drawn_word = random.choice(list_words)
    shuffle = "".join(random.sample(drawn_word, len(drawn_word)))
    maximum_attempts = 3
    correct_answer = False
    while maximum_attempts > 0 and not correct_answer:
        word = input(f"Qual é a palavra correta para {shuffle}? ")
        if word in list_words:
            print("Certa resposta!")
            correct_answer = True
            return
        maximum_attempts -= 1
        if maximum_attempts == 0:
            print("Fim do jogo")
            return
        print(f"Resposta errada, você ainda tem {maximum_attempts} tentivas")

"""
    Dado o seguinte arquivo no formato JSON (library.json), leia seu conteúdo e calcule a porcentagem de livros em cada categoria em relação ao número total de livros. O resultado deve ser escrito em um arquivo no formato CSV como o exemplo abaixo.
"""
#saida é uma lista de tuplas [(categoria, float)]


def calculate_books_by_category():
    with open('data/library.json') as file:
        contents = json.load(file)
    set_categories = []
    count_all_books = len(contents)
    for content in contents:
        set_categories.extend(content['categories'])
    set_categories = set(set_categories)
    category_and_counter = []
    for category in set_categories:
        list_by_categories = [book for book in contents if category in book['categories']]
        category_and_counter.append((category, len(list_by_categories)/count_all_books))
    # falta escrever em um arquivo CSV
    with open('data/output/books_counter.csv', mode='w') as file:
        writer = csv.writer(file)
        headers = ['categoriras', 'porcentagem']
        writer.writerow(headers)
        for item in category_and_counter:
            writer.writerow(list(item))

calculate_books_by_category()


"""

    	def reverse(numbers, last_index):
2	    if last_index < 0:
3	        return []
4	
5	    return [numbers[last_index]] + reverse(numbers, last_index - 1)
6	
7	
8	if __name__ == '__main__':
9	    my_numbers = [10, 20, 30, 40]
10	    my_reversed = reverse(my_numbers, len(my_numbers)-1)
11	
12	    print(my_numbers)
13	    print(my_reversed)
"""