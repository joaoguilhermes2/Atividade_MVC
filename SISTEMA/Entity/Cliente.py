from DB.Database import Database

class Cliente:
    def __init__(self) -> None:
        self.nome = None
        self.cpg = None
        self.login = None
        self.senha = None
        self.fone = None
        self.cidade = None
        self.banco = Database()
    
    def cadastrar(self):
        tupla = (self.nome,self.cpg,self.login,self.senha,self.fone,self.cidade)
        cad = self.banco.insert_client(tupla)
        return cad
    
    def selecionar(self):
        clientes = self.banco.select_client()
        return clientes
    
    def selecionar_por_id(self, id):
        cliente = self.banco.select_client_by_id(id)
        return cliente
    
    def atualizar(self, lista):
        cli_atualizado = self.banco.update_client(lista)
        return cli_atualizado
    
    def deletar(self, id):
        cli_excluido = self.banco.delete_client(id)
        return cli_excluido