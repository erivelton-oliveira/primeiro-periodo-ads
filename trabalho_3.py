# Função para calcular o valor base com base no peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))
            if peso < 3:
                return 40
            elif (peso >= 3) and (peso < 10):
                return 50
            elif (peso >= 10) and (peso < 30):
                return 60
            elif (peso >= 30) and (peso < 50):
                return 70
            else:
                print("Peso inválido. O peso deve ser menor que 50 kg.")
        except ValueError:
            print("Por favor, digite um valor numérico válido para o peso.")

# Função para calcular o multiplicador com base no tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        pelo = input("Digite o tipo de pelo do cachorro (c/m/l): ")
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção de pelo inválida. Escolha c (curto), m (médio) ou l (longo).")

# Função para calcular o valor extra com base nos serviços adicionais
def cachorro_extra():
    extra = 0
    while True:
        try:
            print(' ')
            adicional = int(input('Escolha um serviço adicional:\n'+
                                  '1 - Cortar unhas (R$10)\n'+
                                  '2 - Escovar dentes (R$12)\n'+
                                  '3 - Limpar orelhas (R$15)\n'+
                                  '0 - Não querer mais nada\n'+
                                  'Opção: '
                                  ))
            if adicional == 1:
                extra += 10
            elif adicional == 2:
                extra += 12
            elif adicional == 3:
                extra += 15
            elif adicional == 0:
                return extra
            else:
                print("Opção de serviço adicional inválida. Escolha 0, 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite uma opção válida.")

# Função principal
def main():
    print("Bem-vindo ao PetShop do Erivelton Felipe de Oliveira")

    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    extra = cachorro_extra()
    
    total = base * multiplicador + extra
    print(f"Total a pagar: R${total:.2f}")

if __name__ == "__main__":
    main()
