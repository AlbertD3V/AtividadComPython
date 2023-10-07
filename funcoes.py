
def mult(n1,n2):
    total = n1*n2
    return total


x = input('Vamos tentar multiplicar?(Y/N)')
if x.upper ()== 'Y':
    n1= int(input('qual o numero? '))
    n2 = int(input('qual o outro numero? '))
    print (mult(n1,n2))
