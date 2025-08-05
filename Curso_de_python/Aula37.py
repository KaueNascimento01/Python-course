entrada_nome = input('Digite um nome: ')
nome = entrada_nome  # Iterável (ou seja, pode ser percorrido caractere por caractere)

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'

print(novo_nome)