    # 'Calculadora com while'
while True:
    
    linhas_1 = 3

    print('\n'* linhas_1)
    sair = input('Você quer sair?').lower()

    if sair.startswith('sim') or sair.startswith('yes') is True:
        print('saindo...')
        break
    else:
        print('\n'* linhas_1)
        print('Digite novamente')