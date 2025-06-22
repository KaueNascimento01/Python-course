nota1 = input('Digite sua primeira nota: ')
nota2 = input('Digite sua segunda nota: ')
nota3 = input('Digite sua terceira nota: ')

float_nota_1 = (float (nota1))
float_nota_2 = (float (nota2))
float_nota_3 = (float (nota3))

resultado = (float_nota_1 + float_nota_2 + float_nota_3)/3

if resultado > 7:
    resultado = 10
    print(f'Parabéns!!, Você antingiu os "{resultado:.1f}" pontos e foi aprovado.')

else:
    print(f'Infelizmente sua nota de "{resultado:.1f}" não foi suficente para você ser aprovado')