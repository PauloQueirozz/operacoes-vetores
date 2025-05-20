operacao = int(input('''[ 1 ] Adição/subtração
[ 2 ] Multiplicação por escala
[ 3 ] Produto interno
[ 4 ] Produto Vetorial
[ 5 ] Produto Misto
Qual operação você quer fazer? '''))

if operacao == 1:
   dimensao = int(input('''[ 1 ] Bidimensional
[ 2 ] Tridimensional
Qual é a dimensão dos vetores? '''))
   if dimensao == 1:
      a, b = (list(map(float, input('A, B: ').split())))
      d, e = (list(map(float, input('D, E: ').split())))
      print(f'''Adição: ({a+d:.2f}, {b+e:.2f})
Subtração: ({a-d:.2f}, {b-e:.2f})''')
   else:
      a, b, c = (list(map(float, input('A, B, C: ').split())))
      d, e, f = (list(map(float, input('D, E, F: ').split())))
      print(f'''Adição: ({a+d:.2f}, {b+e:.2f}, {c+f:.2f})
Subtração: ({a-d:.2f}, {b-e:.2f}, {c-f:.2f})''')

elif operacao == 2:
   dimensao = int(input('''[ 1 ] Bidimensional
[ 2 ] Tridimensional
Qual é a dimensão dos vetores? '''))
   vetor = float(input('Vetor: '))
   if dimensao == 1:
      a, b = (list(map(float, input('A, B: ').split())))
      print(f'Multiplicação por escala: ({a*vetor:.2f}, {b*vetor:.2f})')
   else:
      a, b, c = (list(map(float, input('A, B, C: ').split())))
      print(f'Multiplicação por escala: ({a*vetor:.2f}, {b*vetor:.2f}, {c*vetor:.2f})')

elif operacao == 3:
   dimensao = int(input('''[ 1 ] Bidimensional
[ 2 ] Tridimensional
Qual é a dimensão dos vetores? '''))
   if dimensao == 1:
      a, b = (list(map(float, input('A, B: ').split())))
      d, e = (list(map(float, input('D, E: ').split())))
      produto_interno = (a*d)+(b*e)
      print(f'Produto interno: {produto_interno:.2f}')
   else:
      a, b, c = (list(map(float, input('A, B, C: ').split())))
      d, e, f = (list(map(float, input('D, E, F: ').split())))
      produto_interno = (a*d)+(b*e)+(c*f)
      print(f'Produto interno: {produto_interno:.2f}')

elif operacao == 4:
   a, b, c = (list(map(float, input('A, B, C: ').split())))
   d, e, f = (list(map(float, input('D, E, F: ').split())))
   i = ((b*f)-(c*e))
   j = ((c*d)-(a*f))
   k = ((a*e)-(b*d))
   print(f'Produto Vetorial: ({i:.2f}, {j:.2f}, {k:.2f})')

elif operacao == 5: 
   a, b, c = (list(map(int, input('A, B, C: ').split())))
   d, e, f = (list(map(int, input('D, E, F: ').split())))
   g, h, i = (list(map(int, input('D, E, F: ').split())))
   produto_misto = (a*((e*i)-(f*h)))+(b*((f*g)-(d*i)))+(c*((d*h)-(e*g)))
   print(f'Produto Misto: {produto_misto}')
