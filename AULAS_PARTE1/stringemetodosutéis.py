curso = "   PytHon   "

print(curso.upper()) # coloca todos os caracteres em maiuculos
print(curso.lower()) #coloca todos os caracteres em minusculos
print(curso.title()) # deixa apenas a primeira letra em maisculo
print(curso.strip()) #retira os espaços do começo e do final de uma string
print(curso.lstrip()) #retira os espaços em branco do começo da string da esquerda para direita
print(curso.rstrip()) #retira os espaços em branco do fim da string da edireita para esquerda

curso = "Python"
print(curso.center(10,"$")) # center alinha a string ao centro, tendo que informar dois parametros o primeiro é a quantidade de carcteres que ela vai ter esse sendo obrigátorio, e o segundo o caracter que você deseja por para completar o primeiro parametro esté é opcional
print(".".join(curso)) #join realiza junção o que esta entre aspas é o que o join vai colocar, join junta , parece com o for ele passa por toda a string carcter a carcter e coloca o . entre cada um conforme solicitado

