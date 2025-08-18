"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'trabalho'
letras_acertadas = ''
tentativas = 0

while True:

    tentativas += 1

    pergunta_inicial = input('Digite uma letra: ')
    
    if len(pergunta_inicial) > 1:
        print('Digite apenas uma letra')
        continue
       
    if pergunta_inicial in palavra_secreta:
            letras_acertadas += pergunta_inicial

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
             palavra_formada += letra

        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
         os.system('clear')
         
         print(f'Parabéns!! você acertou todas as letras da palvra "{palavra_formada}".')
         print(f'O seu total de tentativas foi {tentativas}.')  
         
