comandas = []

def anotar_comanda(produto, quantidade, preco_unitario, valor_total):
    comanda = {
        'produto': produto,
        'quantidade': quantidade,
        'preço unitário': preco_unitario,
        'valor total': valor_total
    }
    
    comandas.append(comanda)
    print(f'Comanda anotada: {comanda}')

def listar_comandas():
    if not comandas:
        print('Nenhuma comanda registrada.')
    else:
        for i, comanda in enumerate(comandas, 1):
            print(f"{i}. Produto: {comanda['produto']}, Quantidade: {comanda['quantidade']}, Preço unitário: R${comanda['preço unitário']:.2f}, Valor total: R${comanda['valor total']:.2f}")