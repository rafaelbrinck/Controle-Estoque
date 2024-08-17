import classes
import os
import time
import json

# Listas

listaProdutos = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getche():
    x = input("Pressione ENTER para continuar")
    

def adicionar():
    clear()
    categoria = input('Categoria (Rede, Toca, Forracao): ').strip()
    nome = input('Produto: ').strip()
    preco = input('Preço: ').strip()
    medidas = input('Medidas: ').strip()

    if not categoria or not nome or not preco or not medidas:
        print('Todos os campos devem ser preenchidos. Produto não adicionado!')
        return
    try:
        categoria = categoria.capitalize()
        preco = float(preco)
    except ValueError:
        print("Preço deve ser em número válido.")
        return
    produto = classes.Produto(nome, preco, medidas, categoria)
    listaProdutos.append(produto)
    clear()
    print(f'Produto {nome} adicionado com sucesso!\n')
    getche()

def mostrarCategorias():
    clear()
    print('-'*40)
    print('1 - Redes')
    print('2 - Tocas')
    print('3 - Forrações')
    print('-'*40)
    op = input('Qual deseja: ')

    if op == '1':
        clear()
        for produto in listaProdutos:
            if produto.getcategoria() == 'Rede':
                print(f'{produto.getcategoria()} {produto.getnome()} ({produto.getmedidas()})')
        print('\n')
        getche()
    elif op == '2':
        clear()
        for produto in listaProdutos:
            if produto.getcategoria() == 'Toca':
                print(f"{produto.getnome()} ({produto.getmedidas()}) - R${produto.getpreco()}")
        print('\n')
        getche()
    elif op == '3':
        clear()
        for produto in listaProdutos:
            if produto.getcategoria() == 'Forracao':
                print(f"{produto.getnome()} ({produto.getmedidas()}) - R${produto.getpreco()}")
        print('\n')
        getche()

def remover():
    clear()
    if not listaProdutos:
        print('Nenhum produto para remover.')
        time.sleep(2)
        return
    print('-'*40)
    for i, produto in enumerate(listaProdutos):
        print(f'{i} - {produto.getnome()}')
    print('-'*40)
    ind = input('\nQual numero do produto que deseja remover: ')
    if ind.strip() == '':
        clear()
        print("Nenhum número fornecido. Ação cancelada.")
        getche()
        return
    try:
        ind = int(ind)
        if 0 <= ind < len(listaProdutos):
            for i, produto in enumerate(listaProdutos):
                if i == ind:
                    listaProdutos.pop(ind)
            clear()
            print(f"Produto {produto.getnome()} removido com sucesso!\n")
            getche()
        else:
            clear()
            print('Índice inválido.')
            getche()
    except ValueError:
        clear()
        print('Entrada inválida.')
        getche()


# Json
def exportar():
    dict_json = [produto.to_dict() for produto in listaProdutos]
    with open('dados.json', 'w') as arquivo:
        json.dump(dict_json, arquivo, indent=4)
    clear()
    print("Dados exportados com sucesso!")
    time.sleep(1)


def importar():
    try:
        with open('dados.json', 'r') as arquivo:
            dados = json.load(arquivo)
        listaProdutos.extend([classes.Produto.from_dict(produto) for produto in dados])
        clear()
        print("Dados importados com sucesso!")
        time.sleep(1)
    except FileNotFoundError:
        clear()
        print("Arquivo 'dados.json' não encontrado.")
        time.sleep(1)
    except json.JSONDecodeError:
        clear()
        print("Erro ao decodificar o arquivo JSON")
        time.sleep(1)





