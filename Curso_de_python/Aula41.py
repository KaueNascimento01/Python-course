texto = 'aaaaooo'

i = 0
maior_quantidade = 0
letra_mais_frequente = ''

while i < len(texto):
    caractere = texto[i]

    if caractere == ' ':
        i += 1
        continue

    frequencia = texto.count(caractere)

    if maior_quantidade <= frequencia:
        maior_quantidade = frequencia
        letra_mais_frequente = caractere

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_frequente}" que apareceu '
    f'{maior_quantidade}x'
)
