def func_incluir(bd):
    id = input('Id do novo contato: ')
    nome = input('Nome do novo contato: ')
    email = input('E-Mail do novo contato: ')
    bd[id] = {'nome':nome,'email':email}
    print(f'{id}{nome} incluído com sucesso')

def func_excluir(bd):
    id = input('Id do contato a ser excluído: ')
    del bd[id]
    print(f'{id} excluído com sucesso')

def func_consultar_um(bd):
    id = input('Id do contato a ser consultado: ')
    print(f'ID: {id}')
    print('NOME:',bd[id]['nome'])
    print('E-MAIL',bd[id]['email'])
    print(f'Consulta executada com sucesso')

def func_consultar_todos(bd):
    for ident in bd:
        print(f'ID: {ident}')
        print('NOME:',bd[ident]['nome'])
        print('E-MAIL',bd[ident]['email'])
        print('----------------------------')
    print(f'Consulta executada com sucesso')

def func_alterar_contato(bd):


dados = {
    '1':{'nome':'fulano','email':'ful@qq.com'},
    '2':{'nome':'beltrano','email':'bb@qq.com'}
}

while True:
    print('''
        ==============================
        CONTATOS
        ==============================
        1. Incluir contato
        2. Excluir contato
        3. Consultar UM contato
        4. Consultar TODOS os contatos
        5. Encerrar aplicação
        ==============================
          ''')
    op = input('Informe a operação desejada: ')
    if op == '5':
        print('Aplicação encerrada')
        break
    elif op == '1':
        func_incluir(dados)
    elif op == '2':
        func_excluir(dados)
    elif op == '3':
        func_consultar_um(dados)
    elif op == '4':
        func_consultar_todos(dados)


print('fim')