operacao = int(input('''[ 1 ] Adição/subtração
[ 2 ] Multiplicação por escala
[ 3 ] Produto interno
[ 4 ] Produto Vetorial
[ 5 ] Produto Misto
Qual operação você quer fazer? '''))

if operacao == 1:
   a, b, c = (list(map(float, input('A, B, C: ').split())))
   d, e, f = (list(map(float, input('D, E, F: ').split())))
   print(f'''Adição: ({a+d:.2f}, {b+e:.2f}, {c+f:.2f})
Subtração: ({a-d:.2f}, {b-e:.2f}, {c-f:.2f})''')

if operacao == 2:
   vetor = float(input('Vetor: '))
   a, b, c = (list(map(float, input('A, B, C: ').split())))
   print(f'Multiplicação por escala: ({a*vetor:.2f}, {b*vetor:.2f}, {c*vetor:.2f})')

if operacao == 3:
   a, b, c = (list(map(float, input('A, B, C: ').split())))
   d, e, f = (list(map(float, input('D, E, F: ').split())))
   produto_interno = (a*d)+(b*e)+(c*f)
   print(f'Produto interno: {produto_interno:.2f}')
   
if operacao == 4:
   a, b, c = (list(map(float, input('A, B, C: ').split())))
   d, e, f = (list(map(float, input('D, E, F: ').split())))
   i = ((b*f)-(c*e))
   j = ((c*d)-(a*f))
   k = ((a*e)-(b*d))
   print(f'Produto Vetorial: ({i:.2f}, {j:.2f}, {k:.2f})')

# FALTA IDENTIFICAR OS SINAIS
# if operacao == 5: 
#    a, b, c = (list(map(int, input('A, B, C: ').split())))
#    d, e, f = (list(map(int, input('D, E, F: ').split())))
#    g, h, i = (list(map(int, input('D, E, F: ').split())))
#    soma1 = ((a*e*i)(f*b*g)(c*h*d))
#    soma2 = ((c*e*g)(b*d*i)(f*h*a))
#    produto_misto = soma1-soma2
#    print(f'Produto Misto: {produto_misto}')
