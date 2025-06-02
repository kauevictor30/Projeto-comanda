from menu import menu  
from produtos import *
from comanda import *
from caixa import registrar_pagamento, saldo_caixa


forma_de_pag = ['pix', 'credito', 'debito', 'dinheiro']
caixa = []

while True:
    menu()
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        if not Produtos:
            print('Nenhum produto cadastrado. Cadastre produtos antes de anotar comandas.')

        else:
            print('Produtos disponíveis:')
            for i, produto in enumerate(Produtos, 1):
                print(f"{i}  {produto['nome']} (Categoria: {produto['categoria']}, Preço: R${produto['preco']:.2f})")
            escolha = int(input('Escolha o número do produto: '))

            if 1 <= escolha <= len(Produtos):
                produto = Produtos[escolha - 1]['nome']
                quantidade = int(input('Quantidade: '))
                preco_unitario = Produtos[escolha - 1]['preco']
                valor_total = quantidade * preco_unitario
                anotar_comanda(produto, quantidade, preco_unitario, valor_total)
            else:
                print('Produto inválido!')

    elif opcao == '2':
        nome = input('Nome do produto: ')
        quantidade = int(input('Quantidade do produto: '))
        categoria = input('Categoria do produto: ')
        preco = float(input('Preço do produto: '))
        cadastrar_produto(nome, quantidade, categoria, preco)

    elif opcao == '3':
        if not Produtos:
            print('Nenhum produto encontrado.')
        else:
            print('Produtos disponíveis:')
            listar_produtos()

    elif opcao == '4':
        if not comandas:
            print('Nenhuma comanda registrada para pagamento.')
        else:
            valor_total = comandas[-1]['valor total']
            print(f"Valor a ser pago (última comanda): R${valor_total:.2f}")
            try:
                valor_pagamento = float(input('Valor pago: '))
            except ValueError:
                print('Valor inválido! Digite um número.')
                continue
            pagamento = input('Forma de pagamento: ').lower()
            if pagamento in forma_de_pag:
                registrar_pagamento(valor_pagamento, pagamento)
            else:
                print('Forma de pagamento inválida!')


    elif opcao == '5':
        saldo_caixa()

    elif opcao == '6':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')