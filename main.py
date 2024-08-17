import functions
import time

functions.importar()
while True:
    functions.clear()
    print('-'*40)
    print('1 - Adicionar Produtos')
    print('2 - Mostrar Produtos')
    print('3 - Remover Produtos')
    print('9 - Sair')
    print('-'*40)
    op = input('Qual deseja: ').strip()

    if op == '1':
        functions.adicionar()
    elif op == '2':
        functions.mostrarCategorias()
    elif op == '3':
        functions.remover()
    elif op == '9':
        functions.exportar()
        break
    else:
        functions.clear()   
        print('Escolha uma opção válida!')
        time.sleep(1)



