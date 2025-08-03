"""
Faça um programa que peça ao usuário para digitar um número do tipo inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
def print_titulo(texto, largura = 57):
    print('\n' * 6)
    print('-' * largura)
    print(texto.center(largura))
    print('-' * largura)
    print()

def atividade_1():
    while True:
        try:
            print_titulo('Validação e Classificação de Número Inteiro por Paridade')

            entrada = input('Digite um número: ')
            entrada_int = int(entrada)

            if entrada_int % 2 == 0:
                print(f'O número "{entrada_int}" é par')
                break
            else:
                print(f'O número "{entrada_int}" é ímpar')
                break

        except ValueError:
            print('Você digitou letra(s) ou caracteres inválido(s). Tente  Novamente')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

def atividade_2():
    while True:
        try:

            print_titulo('Saudação Condicional Baseada em Horário')

            horario = input('Que horas são agora? ')
            horario_int = int(horario)

            if horario_int >= 0 and horario_int <=11 :
                print('Bom Dia!!')
                break
            elif horario_int >= 12 and horario_int <= 17:
                print('Boa Tarde!!')
                break
            elif horario_int >=18 and horario_int <= 23:
                print('Boa Noite!!')
                break
            else:
                print('O horário que você digitou é invalido. O horário deve estar entre 0 e 23')
        except ValueError:
            print('Você digitou letra(s) ou caracteres inválido(s). Tente  Novamente')
        

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
def atividade_3():
    print_titulo('Análise e Classificação do Comprimento do Primeiro Nome')
    nome = input('Digite seu nome: ')
    tamanho_nome = len(nome)
    if tamanho_nome > 1:
        if tamanho_nome <= 4:
            print('Seu nome é curto')
        elif tamanho_nome >= 5 and tamanho_nome <= 6:
            print('Seu nome é normal')
        else:
            print('Seu nome é muito grande')
    else:
        print('Digite mais de uma letra.')
    

if __name__ == "__main__":
    while True:
        print()
        escolha = input("Digite o número da atividade que deseja executar (1, 2 ou 3): ")

        if escolha == "1":
            atividade_1()
        elif escolha == "2":
            atividade_2()
        elif escolha == "3":
            atividade_3()
        else:
            print("Atividade inválida. Escolha 1, 2 ou 3.")