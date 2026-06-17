from estoque import cadastrar_produto, listar_produtos, buscar_produto, atualizar_quantidade, remover_produto, verificar_estoque_baixo
from armazenamento import carregar_dados, salvar_dados

estoque = carregar_dados()

while True:
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Buscar Produto')
    print('4 - Atualizar Quantidade')
    print('5 - Remover Produto')
    print('6 - Ver alerta de estoque baixo')
    print('7 - Sair')

    opcao = input('Qual opção deseja escolher: ')

    if opcao == '1':
        produto_id = input('ID a ser cadastrado: ')
        nome_produto = input('Nome do produto a ser cadastrado: ')
        quantidade_produto = int(input('Quantidade a ser cadastrado: '))
        preco_protudo = float(input('Preço do produto a ser cadastrado:'))
        categoria_produto = input('Categoria a ser cadastrado:')
        estoque_minimo = int(input('Quantidade minima: '))

        cadastrar_produto(estoque, produto_id, nome_produto, quantidade_produto, preco_protudo, categoria_produto, estoque_minimo)
        salvar_dados(estoque)
    
    elif opcao == '2':
        print(listar_produtos(estoque))

    elif opcao == '3':
        id_busca = input('Qual ID deseja buscar: ')
        print(buscar_produto(estoque, id_busca))

    elif opcao == '4':
        id_produto = input('Qual o ID do produto: ')
        quantidade = int(input('Informe a quantidade que deseja: '))

        atualizar_quantidade(estoque, id_produto, quantidade)
        salvar_dados(estoque)

    elif opcao == '5':
        id_do_produto = input('Qual o ID do produto que deseja remover: ')

        remover_produto(estoque, id_do_produto)
        salvar_dados(estoque)

    elif opcao == '6':
        print(verificar_estoque_baixo(estoque))

    elif opcao == '7':
        break
    
    else: 
        print('Opção invalida!')