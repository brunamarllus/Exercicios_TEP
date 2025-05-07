# Esse e o programa originale 


import time

bd_filmes = [
    ['initerstellar', 'Christopher Nolan', 2014, 'Ficção Científica', 8.6],
    ['titanic', 'James Cameron', 1997, 'Romance', 7.8],
    ['star wars', 'George Lucas', 1977, 'Ficção Científica', 8.6],
]
#Listar filmes
def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} - {bd[i][1]} - {bd[i][0]}')

#Cadastrar filme
def cadastrar_filme(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd 

while True:
    print("bem-vindo CardFilmes")
    print("1. Cadastrar filme")
    print("2. Alterar filmes")
    print("3. Listar filmes")
    print("0. sais")
    try:
        op = int(input("Digite a opção desejada: "))
    except Exception as e:
        print(f'error: {e}')
        op = -1

    time.sleep(1)

    if op == 1:
        print("-----CADASTRO DE FILMES-----")
        titulo = input("Digite o título do filme: ")
        ano = input("Digite o ano do filme: ")  
        bd_filmes = cadastrar_filme(
            bd = bd_filmes,
            titulo = titulo,
            ano = ano
        )

        print("Filme cadastrado com sucesso!")

    elif op == 2:
        print("-----ALTERAR FILMES-----")
        listar_filmes(bd=bd_filmes)
        i = int(input("Digite o número do filme que deseja alterar: "))
        n_titulo = input("Digite o novo título do filme: ")
        n_ano = input(input("Digite o novo ano do filme: "))
        bd_filmes[i-1][0] = n_titulo

        print("Filme alterado com sucesso!")  
    elif  op == 3:
        print("-----LISTA DE FILMES-----")
        listar_filmes(bd=bd_filmes)
        print("-----LISTA DE FILMES-----")
    elif op == 0:
        print("Saindo...")
        break

        
