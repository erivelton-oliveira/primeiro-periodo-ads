print('Bem vindo a loja do Erivelton Felipe de Oliveira')

# Variáveis que serão usadas em todos os blocos de IF e ELIF.
# Sendo que 'valor' receberá um input do valor do protudo e 'qtd' um input de sua quantidade.
valor = float(input('Entre com o valor do produto: '))
qtd = int(input('Entre com a quantidade do produto: '))
total = (valor * qtd)

# Nos blocos foi criada mais uma váriavel que se chama 'desconto', ela será usada para atribuir o desconto
# ao valor total dependendo da quantidade de produtos.
# Para exibir os valores na saída do 'print' eu usei 'f-string'.
if (qtd >= 2000):
    desconto = (total - (total * 0.15))
    print(f'O valor sem desconto: R${total}')
    print(f'O valor com desconto: R${desconto}')

elif (qtd >= 1000):
    desconto = (total - (total * 0.10))
    print(f'O valor sem desconto: R${total}')
    print(f'O valor com desconto: R${desconto}')

elif (qtd >= 200):
    desconto = (total - (total * 0.05))
    print(f'O valor sem desconto: R${total}')
    print(f'O valor com desconto: R${desconto}')

# Coloquei uma mensagem informando que não haveria desconto caso o pedido fosse menos que 200.
else:
    print(f'Você fez um pedido menor que 200, por isso não teve desconto.')
    print(f'O Valor total é: R${total}')