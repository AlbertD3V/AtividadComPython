
def perfil(nome,idade,bairro,estado_civil):
    if idade >= 50:
        print(f'{nome} está perto da aposentadoria. ( Se você recolheu INSS ou investiu em uma previdencia privada)')
    else:
        print(f'{nome} planeje o seu futuro. Faça investimentos e aporte constante.(FUJA DA RENDA FIXA)')
    if bairro == 'Barra':
        print(f'{nome} esta morando em um bom bairro que é {bairro}')
    else:
        print(f'{nome} mora no bairro {bairro}')
    if estado_civil == 'solteiro':
        print(f'{nome} aproveita e estuda.')
    else:
        print(f'{nome} faça planejamento financeiro para o casal')

while True:
    x = input('Deseja completar o perfil? (Y/N) ')
    if x.upper() == 'Y':
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        bairro = input('Bairro: ')
        estado_civil = input('Estado civil: ')
        print('---'*6)
    elif x.upper() == 'N':
        perfil(nome,idade,bairro,estado_civil)
        print('Cadastro de perfil finalizado')
        break
    else:
        print('Digite direito.')
        continue

