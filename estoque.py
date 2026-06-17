def cadastrar_produto(estoque, id, nome, quantidade, preco, categoria, estoque_minimo):
    if id in estoque:
        return False
    else:
        estoque[id] = {'nome': nome, 'quantidade': quantidade, 'preco': preco, 'categoria': categoria, 'estoque_minimo': estoque_minimo}
        return True