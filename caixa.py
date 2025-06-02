caixa = []

def registrar_pagamento(valor, forma_de_pagamento):
    '''
        Registra um pagamento no caixa.
        
        :param valor: Valor do pagamento.
        :param forma_de_pagamento: Forma de pagamento utilizada.
    '''
    
    if forma_de_pagamento not in ['pix', 'credito', 'debito', 'dinheiro']:
        raise ValueError("Forma de pagamento inválida.")
    
    caixa.append({'valor': valor, 'forma': forma_de_pagamento})
    print(f"Pagamento de R${valor:.2f} registrado com sucesso na forma {forma_de_pagamento}.")

def saldo_caixa():
    '''
        Consulta o saldo total do caixa.
        :return: Saldo total do caixa.
    '''
    saldo = sum(pagamento['valor'] for pagamento in caixa)
    print(f'Saldo do caixa: R${saldo:.2f}')
    return saldo