nome = input("Informe seu nome: ")
sobrenome = input("informe seu sobrenome: ")
idade = input("informe a sua idade: ")

print (nome, sobrenome ,idade)

#o end coloca no final da impressão o que você colocar entre "" e o \n  realiza uma quebra de linha
print(nome, sobrenome, idade, end="...\n")

# o sep coloca um separador entre as variaveis, o valor é definido por você usando as "" apos o sep.
print(nome, sobrenome, idade, sep="#")