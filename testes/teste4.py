def somar(a,b):
    return int(a) + int(b)

a = input('Digite um valor do conjunto de números naturais: ')
b = input('Digite ou valor do conjunto de números naturais: ')

if a.isdigit() and b.isdigit():
    resultado = somar(a,b)
    print(f'O resultado da soma é {resultado}')

else:
    print('Você digitou letra(s) ou caracteres invalido(s)')