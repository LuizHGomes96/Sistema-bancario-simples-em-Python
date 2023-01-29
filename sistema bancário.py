saldo = 3500
saques_restantes = 3
limite_saque = 500
extrato = []
menu = '''
#### #### MENU #### ####

[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair

#### #### #### #### ####
'''

while True:
    operacao = int(input(menu))

    if operacao < 0 or operacao > 3:
        print('Opção inválida.')
    
    elif operacao == 1:
        deposito = input('Qual valor deseja depositar? ')
        if float(deposito) > 0:
            saldo += float(deposito)
            extrato.append('Depósito de R$ ' + str('%.2f' % float(deposito)))
        else:
            print('Valor inválido.')

    elif operacao == 2:
        if saques_restantes > 0:
            saque = input('Qual valor deseja sacar? ')
            if float(saque) < saldo:
                if float(saque) <= limite_saque:
                    if float(saque) > 0:
                        saldo -= float(saque)
                        saques_restantes -= 1
                        extrato.append('Saque de R$ ' + ('%.2f' % float(saque)))
                    else:
                        print('Valor inválido.')
                else:
                    print('Valor excede o limite de saque.')
            else:
                print('Valor solicitado é maior que o saldo disponível.')
        else:
            print('Você não pode fazer mais saques hoje.')

    elif operacao == 3:
        extrato.append('Saldo atual: R$ ' + str('%.2f' % saldo))
        for item in extrato:
            print(item, sep='\n')
        del extrato [-1]       

    else:
        print('Obrigado por usar nosso sistema.')
        break
    