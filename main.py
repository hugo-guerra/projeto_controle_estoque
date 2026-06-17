from estoque import cadastrar_produto, listar_produtos, buscar_produto, atualizar_quantidade, remover_produto, verificar_estoque_baixo
from armazenamento import carregar_dados, salvar_dados

estoque = carregar_dados()

while True:
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Buscar Produto')
    print('4 - Atualizar Produto')
    print('5 - Remover Produto')
    print('6 - Ver alerta de estoque baixo')
    print('7 - Sair')

    opcao = input('Qual opção deseja escolher: ')