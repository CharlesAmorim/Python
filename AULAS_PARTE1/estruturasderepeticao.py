#Existem for e while para estruturas de repetição
# for usa rquando se sabe quantas vezes vai repetir

texto = input("Informe um Texto: ")
vogais = "AEIOU"


for letra in texto:
    if letra.upper() in vogais:  #  upper deixa toda letra em maiuscula , in é estruturadeassociação faz a associação de uma variavel com outra.
        print(letra, end="")


print()#Adiciona uma quebra de linha


######## Bulit-in Raange
###REcebe 3 argumentos:   start (opcional), stop(obrigátorio) e step oppcional.

for numero in range(11):
    print(numero, end=" ")

for numero in range(50, 100, 10):
    print(numero, end=" ")


#####Comando While####

##utilizado quando não a certeza da quantidade de vezes que o bloco deve ser executado


opcao = -1

while   opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obirgado por usar nosso sistema bancário, até logo!")            


# o Break é utilizado para parar o while quanto ele atender uma condição especifica,
#  por exemplo, solicita um número para o cliente até ele colocar o número 10 
# quando ele coloca o numero 10 o break trava o código.
# você pode utilizar o Continue para pular uma execução.

