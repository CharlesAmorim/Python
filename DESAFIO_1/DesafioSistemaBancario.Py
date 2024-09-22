#criar um sistema bancario com as funções de deposito, saque e extrato.
#operação de depósito deve ser possivel realizar depositos positivos e trabalha apenas com um usuario
#Os depositos devem ser armazenados em uma variavel e mostrados no extrato!
#depositar só valores positivos
#tem que armazenar todos os depositos
# o sistema deve permitir 3 saque diarios e saques com no maximo 500 reais caso a pessoa não tenha saldo deve proibir o saque e apresentar a mensagem saldo insuficiente
# Os saques devem ser apresentados no extrato.
#Extrato deve mostrar todos os saques e depositos e no fim apresenta o saldo atual da conta. deve ser exibido o saldo com $


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        deposito = float(input("Digite o Valor do Depósito: "))

        def dep(deposito):
            global saldo
            global extrato

            if deposito > 0:
                
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
                return saldo

            else:
                print("Só é permitido depósitos com valores positivos")

            
        dep(deposito)


    elif opcao == "s":
        print("Saque")


        saque = float(input("Digite o Valor do Saque: "))

        def dep(saque):
                    
            global saldo
            global extrato
            global numero_saques
            
            if numero_saques < LIMITE_SAQUES:
                
                if saque <= 500 and saldo >= saque:
                        
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Depósito: R$ {saque:.2f}\n"
                    
                    return saldo, numero_saques, extrato
                    
                elif saque <= 500 and saldo < saque:
                    print("saldo insuficiente")

                else:
                    print("Limite para saques é de R$ 500,00")
            else:
                print(f"O Limite de {LIMITE_SAQUES} saques por dia foi atingido, volte outro dia.")
            
        dep(saque)
        print(f"O Valor de saque foi de {saque} seu saldo é de {saldo}, você utilizou {numero_saques} e seu limite é {LIMITE_SAQUES}")


    elif opcao == "e":
        print('\n ########### EXTRATO ############')
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###############################")



    elif opcao == "q":
        print("Obrigado por usar nossos Serviços")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")