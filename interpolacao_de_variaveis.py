#old style
nome = "Edmar"
idade = 28
profissao = "programador"
linguagem = "Python"
#dicionario para se colocado la embaixo
pessoa ={"nome": "Edmar", "idade": 28, "profissao": "programador", "linguagem": "Python"}

print("Nome: %s Idade: %d" % (nome, idade))
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
#foi feito com o dicionario
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")


PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")