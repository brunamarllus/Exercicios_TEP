import time

bd_filmes = [
    ['Interestelar', 2015],
    ['Titanic', 1997],
    ['Star Wars: Episódio 6', 2022]
]

# Listar Filmes
def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} - {bd[i][1] } - {bd[i][0]}')


# Cadastrar filmes
def cadastrar_filme(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd


# Alterar filmes
def alterar_filme(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd


while True:
    print('Bem-vindo ao Cadastro de Filmes')
    print('1 - Cadastrar Filme')
    print('2 - Alterar Filme')
    print('3 - Listar Filmes')
    print('0 - Sair')
    try:
        op = int(input('Digite a opcao desejada: '))
    except Exception as e:
        print(f'Error: {e}')
        op = -1

    time.sleep(1)

    if op == 1:
        print(f'---- CADASTRO DE FILMES ----')
        titulo = input('Digite o titulo do novo filme: ')
        ano = int(input('Digite o ano do filme: '))
        bd_filmes = cadastrar_filme(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano
        )
        print(f'---- CADASTRO DE FILMES ----')

    elif op == 2:
        print(f'---- ALTERAR FILME ----')
        listar_filmes(bd=bd_filmes)
        i = int(input('Qual filme deseja alterar? '))

        n_titulo = input('Digite o novo titulo: ')
        n_ano = int(input('Digite o novo ano: '))


        print(f'---- ALTERAR UM FILME ----')
    elif op == 3:
        print(f'---- LISTAGEM DE FILMES ----')
        listar_filmes(bd=bd_filmes)
        print(f'---- LISTAGEM DE FILMES ----')

    elif op == 0:
        print('Saindo do programa...')
        break
    else:
        print('Opcao invalida! Tente novamente!')

    time.sleep(2)