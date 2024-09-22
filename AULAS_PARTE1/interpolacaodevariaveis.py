nome ="charles"
idade = 31
profissao = "Financeira"
linguagem = "Python"

#OLD STYLE
print ("Olá,  me chamo %s. Eu tenho %d anos de idade, Tabalho com %s e estou matriculado no curso de %s." % ( nome, idade, profissao, linguagem))


#Usando FORMAT, da forma que está abaixo ele traz na sequencia, contudo se você enumerar as Chaves ela vai trocar a palavra levando em conta o indice da varialvel no final da string depois do .format
print ("Olá,  me chamo {}. Eu tenho {} anos de idade, Tabalho com {} e estou matriculado no curso de {}." .format( nome, idade, profissao, linguagem))

print ("Olá,  me chamo {nome}. Eu tenho {idade} anos de idade, Tabalho com {profissao} e estou matriculado no curso de {linguagem}." .format( nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))


#f string é muito parecido com format mas no caso não precisa passar mais tantas informações, apenas informar o f no começo da string e depois colocar as variaveis entre as chaves nos pontos que voc~e quer.
print (f"Olá,  me chamo {nome}. Eu tenho {idade} anos de idade, Tabalho com {profissao} e estou matriculado no curso de {linguagem}.")

