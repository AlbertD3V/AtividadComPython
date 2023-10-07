def primo(n1):
    if n1<2:
        return (f'{n1} tem que ser maior ou igual a 2.')
    else:
        for i in range(n,1,-1):
            if (n % i)==0:
                return (f'{n1} não é primo')    

n = int(input('Digte um valor: '))
print(primo(n))

