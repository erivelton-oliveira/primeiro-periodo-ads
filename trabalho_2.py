print('------------- Bem-vindo a Sorveteria do Erivelton Felipe de Oliveira -------------')
print('-------------------------------------CARDÁPIO-------------------------------------')
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1      |        R$ 6,00         |      R$ 7,00       |       R$ 8,00       |')
print('|      2      |        R$ 11,00        |      R$ 13,00      |       R$ 15,00      |')
print('|      3      |        R$ 15,00        |      R$ 18,00      |       R$ 21,00      |')
print('----------------------------------------------------------------------------------')

total = 0 # Varável onde os valores dos pedidos serão acumulados

while True:

# As variáveis 'sabor' e 'quantidade' foram criadas para receber os inputs dos clientes
# Logo em seguida a condicional 'if' já verifica se foram digitados inputs corretos
# Caso tenha digitado algo errado na quantidade ou sabor o 'continue' faz o loop reiniciar 
    sabor = input('Entre com o sabor desejado ( tr / pr / es ): ')
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Sabor inválido. Tente novamente!')
        continue
    
    quantidade = int(input('Entre com a quantidade de bolas ( 1 / 2 / 3 ): '))
    if quantidade != 1 and quantidade != 2 and quantidade != 3:
        print('Número de bolas de sorvete inválido. Tente novamente!')
        continue

# Nesse bloco são usadas as condicionais 'if', 'elif' e 'else' para defininir o preço de acordo com o sabor e quantidade
    if sabor == 'tr':
        if quantidade == 1:
            preco = 6
        elif quantidade == 2:
            preco = 11
        else:
            preco = 15
    elif sabor == 'pr':
        if quantidade == 1:
            preco = 7
        elif quantidade == 2:
            preco = 13
        else:
            preco = 18
    else:
        if quantidade == 1:
            preco = 8
        elif quantidade == 2:
            preco = 15
        else:
            preco = 21

    total += preco
    
    # Atribui os nomes completos na variável 'sabor' pra na hora do print do que o cliente pediu sair o nome inteiro
    if sabor == 'tr':
        sabor = 'Tradicional'
    if sabor == 'pr':
        sabor = 'Premium'
    if sabor == 'es':
        sabor = 'Especial'

    print(f'Você pediu {quantidade} bolas de sorvete no sabor {sabor}: Valor acumulado de R${total:.2f}')
    continuar = input('Deseja mais algum sorvete? ( s / n ): ')
    print('')
    if continuar != 's':
        break # Caso o cliente não queira pedir mais nada o 'break' encerrará o loop

print(f'O valor total a ser pago é de R${total:.2f}')