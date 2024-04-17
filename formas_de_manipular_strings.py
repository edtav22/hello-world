curso = "  Python   "

#converte todas a letras para maiuscula
print(curso.upper())
#converte todas as letras para minuscula
print(curso.lower())
#converte a primeira letra para maiuscula
print(curso.title())

#elimiando espaços em branco
#remove espaços em branco a esquerda e da direita
print(curso.strip())
#remove os espaços em branco da esquerda somente
print(curso.lstrip())
#remove os espaços brancos da direita somente
print(curso.rstrip())

#junções e centralização
#exibe o caracter dessa forma ##python## aqui voce passa a quantidade de caracters que voce quer
print(curso.center(10, "#"))
#esse join faz uma junçao dessa forma "P.y.t.h.o.n"
print(".".join(curso))