def selecao(a):   
   for nome in a:
      if nome[0].lower() == 'a':
         return nome

l = ['Albert','Rachel','Ana', 'Karol', 'Elena']

print(selecao(l))
