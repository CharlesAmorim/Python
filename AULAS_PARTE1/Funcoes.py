def exibir_mensagem():
    print("Hello Word")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="charles")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Chappie")


def retorna_antecessor_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor # EM uma função se você não declarar o Return automaticamente ele ira retornar none

print("calcular_total([10, 20, 34])") #64
print(retorna_antecessor_sucessor(10)) #(9, 11)

def exibir_poema(data, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data}\n\n{texto}\n\n{meta_dados}"

    print(mensagem)

exibir_poema(
    "SEXTA FEIRA, 25 de setembro 2025",

    "teste1",
    "teste2",
    "teste3",

    autor = "timpeters",
    ano = 1999,
)


def somar (a, b):
    return a + b

def subtrair(a, b):
    return a * 2 + b * 3

def exibir(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir(10, 10, somar) # Passado o parametro A e B , o somar é a função somar que é renomeada para funcao na função exibir.
exibir(10, 10, subtrair)


salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)

print(salario_com_bonus)


