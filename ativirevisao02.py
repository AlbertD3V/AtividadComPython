def menor(n1,n2):
    if n1<n2:
        return n1
    elif n2<n1:
        return n2
    else:
        return (f'Os valores são iguais: {n1}')


print(menor(5,5))
print(menor(6,8))
print(menor(9,10))