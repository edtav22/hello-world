curso = "Curso de python"
nome_curso = curso
saldo, limite = 200, 200
#ocupa a mesma região de memoria
print(curso is nome_curso)
#não ocupa a mesma região de memoria
print(curso is not nome_curso)
#feito com valores inteiros
print(saldo is limite)


