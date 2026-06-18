from estoque import cadastrar_produto, listar_produtos, buscar_produto, atualizar_quantidade, remover_produto, verificar_estoque_baixo
from armazenamento import carregar_dados, salvar_dados
import os

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
        preco_protudo = float(input('Preço do produto a ser cadastrado: R$'))
        categoria_produto = input('Categoria a ser cadastrado:')
        estoque_minimo = int(input('Quantidade minima: '))

        resultado = cadastrar_produto(estoque, produto_id, nome_produto, quantidade_produto, preco_protudo, categoria_produto, estoque_minimo)
        salvar_dados(estoque)

        if resultado == True:
            print('Produto/Item cadastrado com sucesso!!!')
        else:
            print('Esté ID já está cadastrado, por favor tente outro.')

        input('Aperte ENTER para continuar...')
        os.system('cls') 
    
    elif opcao == '2':
        for id, produto in listar_produtos(estoque).items():
            print('ID:', id, 'Nome:', produto['nome'], 'Quantidade:', produto['quantidade'], 'Preço:', produto['preco'], 'Categoria:', produto['categoria'], 'Estoque Minimo:', produto['estoque_minimo'])
        input('Listagem total feita, pressione ENTER para continuar...')
        os.system('cls')  

    elif opcao == '3':
        id_busca = input('Qual ID deseja buscar: ')
        buscar = buscar_produto(estoque, id_busca)

        if buscar != None:
            print('ID:', id_busca, 'Nome:', buscar['nome'], 'Quantidade:', buscar['quantidade'], 'Preço:', buscar['preco'], 'Categoria:', buscar['categoria'], 'Estoque Minimo:', buscar['estoque_minimo'])
        else:
            print('Ocorreu um erro produto não encontrado, tente novamente com um valor valido!')

        input('Aperte ENTER para continuar...')
        os.system('cls')  

    elif opcao == '4':
        id_produto = input('Qual o ID do produto: ')
        quantidade = int(input('Informe a quantidade que deseja: '))

        atualizar = atualizar_quantidade(estoque, id_produto, quantidade)

        if atualizar == True:
            print('O produto foi atualizado com exatidão!')
            salvar_dados(estoque)
        else:
            print('Alguma coisa deu errado, tente novamente atentamente!')

        input('Aperte ENTER para continuar...')
        os.system('cls') 

    elif opcao == '5':
        id_do_produto = input('Qual o ID do produto que deseja remover: ')

        remover_produto(estoque, id_do_produto)
        salvar_dados(estoque)
        input('Item removido com sucesso, pressione ENTER para continuar...')
        os.system('cls') 

    elif opcao == '6':
        print(verificar_estoque_baixo(estoque))
        input('Pressione ENTER para continuar...')
        os.system('cls')  

    elif opcao == '7':
        break
    
    else: 
        print('Opção invalida!')  