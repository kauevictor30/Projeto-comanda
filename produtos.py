Produtos = []

def cadastrar_produto(nome, quantidade, categoria, preco):
    produto =  {
        'nome': nome,
        'quantidade': quantidade, 
        'categoria': categoria,
        'preco': preco
    }

    Produtos.append(produto)
    print(f'{produto}')

def listar_produtos():
        if not Produtos:
            print('nenum produto encontrado')
        else:
            for i, produto in enumerate(Produtos, start=1):
                print(f'{i} - {produto['nome']}, Categoria: {produto['categoria']}, Preço: R${produto['preco']:.2f}')