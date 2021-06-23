def mostrar_menu():
    print('''    [1] Cadastrar produto
    [2] Alterar produto
    [3] Excluir produto
    [4] Listar estoque de peças
    [5] Comprar produto
    [6] Vender Produto
    [7] Sair''')
    global opcao
    opcao = int(input('Qual é a sua opção? '))


def verificar_senha(valor):
    # O limite de tentativas para acesso, em caso de senha incorreta, é de 3 tentativas.

    global tentativas
    if valor == senha:
        tentativas = 2
        return True
    else:
        while tentativas >= 0:
            print("Senha incorreta. Você possui mais ", tentativas, " tentativas.")
            if tentativas == 0:
                print("Seu acesso foi bloqueado. Contate seu administrador.")
                exit()
            tentativas -= 1
            return False


def alterar_produto():
    senha = input('Para alterar o produto, por favor digite sua senha: ')
    if senha == "yN1825*a":
        print('>>>>ACESSO PERMITIDO<<<<')
        tentativas = 2
        acesso_alteracao()
    else:
        tentativa = 0
        while senha != 'yN1825*a' and tentativa < 2:
            print('Senha incorreta. Você possui {} tentativa(s) antes de bloquear o seu acesso.'.format(
                2 - tentativa))
            mostrar_menu()
            senha = input('Para alterar o produto, por favor digite sua senha: ')
            tentativa += 1
            if senha == 'yN1825*a':
                print('>>>>ACESSO PERMITIDO<<<<')
                acesso_alteracao()
        else:
            print('SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR')
            exit()


def acesso_alteracao():
    # b) Se o usuário entrar com a senha correta (ao acessar a opção alterar ou excluir produto), não deve ser solicitada mais até o usuário sair do programa.
    # O limite de tentativas para acesso, em caso de senha incorreta, é 3 tentativas.
    # c) Não permitir quantidade de produto menor ou igual a 0 (zero) nas opções 1, 2, 5 e 6.
    # d) O programa somente pode ser finalizado se o usuário escolher a opção 7 ou se digitar 3 vezes a senha de acesso a opção 2 e 3 incorretamente.

    codigo_do_produto = int(input('Informe o código do produto que será alterado: '))
    if codigo_do_produto not in codigos_dos_produtos:
        print('>PRODUTO NÃO CADASTRADO<.')
    else:
        indice = codigos_dos_produtos.index(codigo_do_produto)
        print(codigos_dos_produtos[indice], " ", descricoes_dos_produtos[indice], " ", quantidades_em_estoque[indice])
        nova_quantidade = int(input('Informe a quantidade atualizada do produto: '))

        while nova_quantidade <= 0:
            nova_quantidade = int(input('Valor não permitido. Informe uma quantidade válida: '))
        if nova_quantidade > 0:
            nova_descricao = input('Informe descrição atualizada do produto: ')

            if nova_quantidade != quantidade_do_produto:
                quantidades_em_estoque[indice] = nova_quantidade

            if nova_descricao != "" and nova_descricao != descricao_do_produto:
                descricoes_dos_produtos[indice] = nova_descricao

            print('>ALTERAÇÃO REALIZADA COM SUCESSO<')


def excluir_item(codigo):
    #  b) Se o usuário entrar com a senha correta (ao acessar a opção alterar ou excluir produto), não deve ser solicitada mais até o usuário sair do programa.
    #  O limite de tentativas para acesso, em caso de senha incorreta, é 3 tentativas.
    # d) O programa somente pode ser finalizado se o usuário escolher a opção 7 ou se digitar 3 vezes a senha de acesso a opção 2 e 3 incorretamente.
    if codigo in codigos_dos_produtos:
        indice = codigos_dos_produtos.index(codigo)
        resp = int(input("Deseja excluir este item? Para 'sim', digite 1, e para 'não', digite 2: "))
        print(codigos_dos_produtos[indice], " ", descricoes_dos_produtos[indice], " ", quantidades_em_estoque[indice])
        while resp != 1 and resp != 2:
            resp = int(input("Código inválido. Para 'sim', digite 1, e para 'não', digite 2: "))
        if resp == 1:
            del codigos_dos_produtos[indice]
            del descricoes_dos_produtos[indice]
            del quantidades_em_estoque[indice]
            print("Produto excluido com sucesso")
        else:
            print("Produto não excluído")
    else:
        print("Produto não cadastrado.")


def estoque_data():
    # Juntar as tabelas
    data = codigos_dos_produtos, descricoes_dos_produtos, quantidades_em_estoque

    # Calcular total de itens no estoque
    estoque_total = quantidades_em_estoque
    soma_estoque = sum(estoque_total)

    print("----------------------------------RELATÓRIO DO ESTOQUE:-----------------------------------------")
    print("-------------------------CÓDIGO-------------------DESCRIÇÃO---------------------QUANTIDADE------")

    # Exibir itens das tabelas juntas com intervalo de "30"
    row_format = '{:>30}' * len(data)
    for i in zip(*data):
        print(row_format.format(*i))
    print("")

    print("Total de produtos cadastrados: ", len(codigos_dos_produtos))  # exibir total de itens cadastrados
    print("Quantidade de itens em estoque: ", soma_estoque)

    index = 0
    for i in quantidades_em_estoque:
        if i < 100:
            produtos_abaixo_de_100.append(codigos_dos_produtos[index])
            index += 1
        else:
            index += 0
    print("Produtos com estoque abaixo do mínimo permitido (100 unidades): ", index)

    print("-------------------------------------------------------------------------------------------------")
    print("")
    print("")


tentativas = 2
produtos_abaixo_de_100 = []
codigos_dos_produtos = [0]
descricoes_dos_produtos = [0]
quantidades_em_estoque = [0]
senha = "yN1825*a"

while True:
    print('-' * 36)
    print('                XPTO')
    print('-' * 36)
    mostrar_menu()
    if opcao == 1:
        # Caso o usuário escolha a opção 1, o programa deve solicitar o código do produto,
        # descrição do produto e quantidade do produto em estoque.
        # Verificar se o código já existe no cadastro, pois não pode ter código duplicado.
        # Depois retorna para o Menu.
        # c) Não permitir quantidade de produto menor ou igual a 0 (zero) nas opções 1, 2, 5 e 6.
        codigo_do_produto = int(input("Digite o código numérico do produto: "))
        while codigo_do_produto in codigos_dos_produtos:
            codigo_do_produto = input("Código já existente no cadastro. Digite um novo código: ")
        indice = 0
        for i in codigos_dos_produtos:
            if i > codigo_do_produto:
                codigos_dos_produtos.insert(indice, codigo_do_produto)
                break
            elif indice+1 == len(codigos_dos_produtos):
                if codigos_dos_produtos[0] == 0:
                    codigos_dos_produtos[0] = codigo_do_produto
                    indice = 0
                    break
                else:
                    codigos_dos_produtos.append(codigo_do_produto)
                    indice = len(codigos_dos_produtos)
                break
            indice += 1
        descricao_do_produto = input("Digite a descrição do produto: ")
        if descricoes_dos_produtos[0] == 0:
            descricoes_dos_produtos[0] = descricao_do_produto
        else:
            descricoes_dos_produtos.insert(indice, descricao_do_produto)
        quantidade_do_produto = int(input("Digite a quantidade do produto em estoque: "))
        while quantidade_do_produto <= 0:
            quantidade_do_produto = int(
                input("A quantidade deve ser maior do que 0. Digite a quantidade do produto em estoque: "))
        if quantidades_em_estoque[0] == 0:
            quantidades_em_estoque[0] = quantidade_do_produto
        else:
            quantidades_em_estoque.insert(indice, quantidade_do_produto)

    elif opcao == 2:
        alterar_produto()

    elif opcao == 3:
        if verificar_senha(input("Por favor, digite sua senha: ")):
            excluir_item(int(input("Por favor, digite o código do produto que deseja excluir: ")))

    elif opcao == 4:
        estoque_data()

    elif opcao == 5:
        # Caso o usuário escolha a opção 5, o programa deve solicitar código do produto.
        # Se o código existir no cadastro, mostrar na tela a descrição e a quantidade atual em estoque.
        # Solicitar a quantidade de produtos que deseja comprar.
        # A quantidade digitada pelo usuário deve somar com o estoque atual do produto em questão.
        # Se o código não existir, mostrar a seguinte mensagem: “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu
        # c) Não permitir quantidade de produto menor ou igual a 0 (zero) nas opções 1, 2, 5 e 6.

        codigo_do_produto = int(input("Digite o código do produto: "))
        if codigo_do_produto in codigos_dos_produtos:
            indice_codigo_do_produto = codigos_dos_produtos.index(codigo_do_produto)
            print("Descrição do produto: ", descricoes_dos_produtos[indice_codigo_do_produto])
            print("Quantidade em estoque: ", quantidades_em_estoque[indice_codigo_do_produto])
            quantidade_para_compra = int(input("Quantas unidades você deseja comprar? "))
            if quantidade_para_compra <= quantidades_em_estoque[indice_codigo_do_produto]:
                quantidades_em_estoque[indice_codigo_do_produto] += quantidade_para_compra
                print("Produto comprado com sucesso.\nQuantidade em estoque: ",
                      quantidades_em_estoque[indice_codigo_do_produto])
            else:
                print("Compra não permitida. Estoque insuficiente.")
        else:
            print("PRODUTO NÃO CADASTRADO.")


    elif opcao == 6:
        # Caso o usuário escolha a opção 6, o programa deve solicitar código do produto.
        # Se o código existir no cadastro, mostrar na tela a descrição e a quantidade atual em estoque.
        # Solicitar a quantidade de produtos que deseja vender.
        # A quantidade digitada pelo usuário deve subtrair com o estoque atual do produto em questão.
        # Importante: A quantidade em estoque não pode ficar negativa.
        # Caso o usuário digite uma quantidade maior do que a que tem em estoque não permitir a venda.
        # Se o código não existir, mostrar a seguinte mensagem: “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu
        # c) Não permitir quantidade de produto menor ou igual a 0 (zero) nas opções 1, 2, 5 e 6.
        codigo_do_produto = int(input("Digite o código do produto: "))
        if codigo_do_produto in codigos_dos_produtos:
            indice_codigo_do_produto = codigos_dos_produtos.index(codigo_do_produto)
            print("Descrição: ", descricoes_dos_produtos[indice_codigo_do_produto])
            print("Quantidade em estoque: ", quantidades_em_estoque[indice_codigo_do_produto])
            quantidade_para_venda = int(input("Quantas unidades você deseja vender? "))
            if quantidade_para_venda <= quantidades_em_estoque[indice_codigo_do_produto]:
                quantidades_em_estoque[indice_codigo_do_produto] -= quantidade_para_venda
                print("Produto colocado à venda com sucesso.\nQuantidade em estoque: ",
                      quantidades_em_estoque[indice_codigo_do_produto])
            else:
                print("Venda não permitida. Estoque insuficiente.")
        else:
            print("PRODUTO NÃO CADASTRADO.")

    elif opcao == 7:
        print('>>>>ACESSO ENCERRADO<<<<')
        break

    else:
        print('Código inválido.')