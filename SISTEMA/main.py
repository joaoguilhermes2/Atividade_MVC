from Entity.Cliente import Cliente

### Cadastro de Cliente ###
cli1 = Cliente()

clientes = cli1.selecionar()
for cliente in clientes:
    print(cliente)

print("\n Selecione um cliente para editar!")
id_selecao = int(input("Digite o ID: "))

cli_selecionado = list(cli1.selecionar_por_id(id_selecao))

cli_selecionado[1] = input("Digite o novo nome: ")
cli_selecionado[2] = input("Digite o novo CPF: ")
cli_selecionado[3] = input("Digite o novo login: ")
cli_selecionado[4] = input("Digite o novo senha: ")
cli_selecionado[5] = input("Digite o novo fone: ")
cli_selecionado[6] = input("Digite o novo cidade: ")

atualiza = cli1.atualizar(cli_selecionado)
if atualiza:
    print("\n Cliente Atualizado com SUCESSO!")

""" print("\n Deseja deletar alguem?")
id_deletar = int(input("Digite o id do caboclo: "))
cli_deletado = cli1.deletar(id_deletar)

if cli_deletado == True:
    print("Cliente Deletado com Sucesso!")
    clientes = cli1.selecionar()
    for cliente in clientes:
        print(cliente)
else:
    print("Erro ao Deletar!")

print("\n Cadastrar um Cliente?")
cli1.nome = input("Digite o novo nome: ")
cli1.cpg = input("Digite o novo CPF: ")
cli1.login = input("Digite o novo login: ")
cli1.senha = input("Digite o novo senha: ")
cli1.fone = input("Digite o novo fone: ")
cli1.cidade = input("Digite o novo cidade: ")

cadastro = cli1.cadastrar()
if cadastro == True:
    print("NO FRONT, CLIENTE CADASTRADO COM SUCESSO!") """