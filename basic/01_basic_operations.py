"""
    No terminal, inicialize duas variáveis a e b, sendo a = 10 e b = 5. Mostre o resultado das 7 operações básicas (soma, subtração, multiplicação, divisão, divisão inteira, potenciação e módulo) envolvendo essas variáveis.
"""
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a / b)
print(a ** b)
print(b % a)
print()
print()
"""
    Declare e inicialize uma variável: hours = 6. Quantos minutos têm em 6 horas? E quantos segundos? Declare e inicialize variáveis minutes e seconds que recebem os respectivos resultados das contas. Depois, imprima cada uma delas.
"""
hours = 6
minutes = hours * 60
seconds = minutes * 60

print(f"{hours} hours has {minutes} minutes and {hours} hours has {seconds} seconds")
print()
print()

"""
    Suponha que o preço de capa de um livro seja R$ 24,20, mas as livrarias recebem um desconto de 40%. O transporte custa 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias? Escreva uma expressão que receba o custo total e a imprima.
"""

book = 'R$ 24,20'
BRL = 'R$ '
COMMA = ','
POINT= '.'
cost_book_on_cape = float(book.replace(BRL, "").replace(COMMA, POINT))
# print(cost_book)
bookstore_discount = '40%'
discount = int(bookstore_discount.replace('%', ""))/100
# print(discount)
cost_transport = {"firts": 3, "other":0.75}
number_copies_book = 60
cost_book_bookstore = cost_book_on_cape*(1-discount)
cost_book_1 =  cost_transport['firts'] + cost_book_bookstore
cost_books_other = cost_book_bookstore * (number_copies_book-1) + cost_transport['other']*(number_copies_book-1)
cost_total = cost_book_1 + cost_books_other
print(f"O custo para produzir 60 cópias de livro são: R$ {cost_total:.2f}")
print()
print()

#Adicione o elemento “Ciência da Computação” à lista.
trybe_course = ["Introdução", "Front-end", "Back-end"]
trybe_course.append('Ciência da Computação')
print(trybe_course)
#Acesse e altere o primeiro elemento da lista para “Fundamentos”.
trybe_course[0] = "Fundamentos"
print(trybe_course)
print()
print()

"""
    Um conjunto ou set pode ser inicializado utilizando-se também o método set(). Inicialize uma variável com essa função var = set() e adicione seu nome ao conjunto utilizando um dos métodos vistos acima. Depois, imprima a variável e confira se o retorno é: {‘seu_nome’}.
"""
var = set()
var.add('Lívio')
print(var)
print()
print()

"""
    Insira no objeto uma nova propriedade com o nome de chave “recorrente” e o valor “Sim”. Em seguida, imprima o objeto no console.
"""
info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}
info['recorrente'] = 'Sim'
print(info)
print()
print()

# Remova a propriedade cuja chave é “origem” e imprima o objeto no console.
info.pop('origem')
print(info)
print()
print()


"""
    Após uma consulta do banco de dados, temos linhas que contém nome, sobrenome e idade como: "Thiago", "Nobre", 29. Que estrutura vista anteriormente seria recomendada dado que após esta consulta somente exibimos estes valores?
"""
pessoa = ("Thiago", "Nobre", 29)
print(pessoa, type(pessoa))
print()
print()

"""
    Realizar a contagem de quantas vezes cada elemento aparece em uma sequência é uma técnica muito útil na solução de alguns problemas. Qual é a estrutura mais recomendada para o armazenamento desta contagem?
"""
my_array = [20, 20, 1, 2]

freq_dict = {}

for item in my_array:
    if (item in freq_dict):
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

for key, valor in freq_dict.items():
    print(f"{key} : {valor}")
