def cadastrar_produto(estoque, id, nome, quantidade, preco, categoria, estoque_minimo):
    if id in estoque:
        return False
    else:
        estoque[id] = {'nome': nome, 'quantidade': quantidade, 'preco': preco, 'categoria': categoria, 'estoque_minimo': estoque_minimo}
        return True
    
def listar_produtos(estoque):
    return estoque

def buscar_produto(estoque, id):
    if id in estoque:
        return estoque[id]
    else:
        return None
    
def atualizar_quantidade(estoque, id, quantidade):
    if id in estoque:
        estoque[id]['quantidade'] += quantidade
        return True
    else:
        return False

def remover_produto(estoque, id):
    if id in estoque:
        estoque.pop(id)
        return True
    else:
        return False
    
def verificar_estoque_baixo(estoque):
    alertas = []

    for id, produto in estoque.items():
        if produto['quantidade'] <= produto['estoque_minimo']:
            alertas.append((id, produto))
    return alertas