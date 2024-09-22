saldo = 1000
saque = 250
limite = 100
conta_especial = True

#And = para ser verdadeiro tudo tem que ser verdadeiro
#or = Para ser verdadeiro basta apenas 1 ser verdadeiro



print(True and True) 
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


exp1 = saldo >= saque and saque <=limite or conta_especial and saldo >=saque
exp2 = (saldo >= saque and saque <=limite) or (conta_especial and saldo >=saque)

print(exp1)
print(exp2)
