""" from DB.Database import Database

banco = Database()

dados = banco.select_client()

print("Clientes Cadastrados: ")
for item in dados:
    print(item)

print("\n Selecione um cliente para editar!")
id_selecao = int(input("Digite o ID: "))

cli_selecionado = list(banco.select_client_by_id(id_selecao))

cli_selecionado[1] = input("Digite o novo nome: ")
cli_selecionado[2] = input("Digite o novo CPF: ")
cli_selecionado[3] = input("Digite o novo login: ")
cli_selecionado[4] = input("Digite o novo senha: ")
cli_selecionado[5] = input("Digite o novo fone: ")
cli_selecionado[6] = input("Digite o novo cidade: ")

atualiza = banco.update_client(cli_selecionado)
if atualiza:
    print("\n Cliente Atualizado com SUCESSO!") """