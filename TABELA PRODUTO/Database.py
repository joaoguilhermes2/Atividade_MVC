import mysql.connector

class Database():
    def __init__(self, banco="produto"):
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            database = self.banco,
            user = 'root',
            password = ''
        )

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com Sucesso!", db_info)
        else:
            print("Erro ao se conectar!")

    def insert_produts(self):
        self.connect()
        try:
            args = ("Arroz", "O arroz é uma planta da família das gramíneas.", "Alimentício", 10, 50, "10/01/2024", "SAC")
            self.cursor.execute("INSERT INTO produto (nome,descricao,categoria,preco,quantidade_estoque,data_adicao,fornecedor) VALUES (%s,%s,%s,%s,%s,%s,%s)", args)
            self.conn.commit()
            print("Produto cadastrado com Sucesso!")

        except Exception as err:
            print(err)

    def select_produts(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto")
            produtos = self.cursor.fetchall()
            for pro in produtos:
                print(pro)

        except Exception as err:
            print(err)

    def select_produts_by_id(self, id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE id_produto = {id}")
            pro = self.cursor.fetchone()
            return pro
        
        except Exception as err:
            print(err)

    def update_produts(self, id):
        self.connect()
        try:
            produto = list(self.select_produts_by_id(id))
            if not produto:
                print("Produto não encontrado!")
                return
            
            print(f"Dados atuais do Produto: {produto}")

            produto[1] = input("Digite o novo nome: ")
            produto[2] = input("Digite a nova descrição: ")
            produto[3] = input("Digite a nova categoria: ")
            produto[4] = input("Digite o novo preço: ")
            produto[5] = input("Digite a nova quantidade de estoque: ")
            produto[6] = input("Digite a nova data de adição: ")
            produto[7] = input("Digite o novo fornecedor: ")

            self.cursor.execute(f"""
                                UPDATE produto
                                SET nome = '{produto[1]}',
                                descricao = '{produto[2]}',
                                categoria = '{produto[3]}',
                                preco = '{produto[4]}',
                                quantidade_estoque = '{produto[5]}',
                                data_adicao = '{produto[6]}',
                                fornecedor = '{produto[7]}'
                                WHERE id_produto = '{produto[0]}'
                                """)
            self.conn.commit()
            pro_atualizado = self.select_produts_by_id(produto[0])
            print(pro_atualizado)

        except Exception as err:
            print(err)

    def delete_produts(self, id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto WHERE id_produto = {id}")
            self.conn.commit()
            print("Produto Deletado com Sucesso!")

        except Exception as err:
            print(err)

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão Encerrada com Sucesso!")

if __name__ == '__main__':
    db = Database()
    """ db.insert_produts() """
    db.select_produts()
    """ db.select_produts_by_id() """
    """ db.update_produts(1) """
    """ db.delete_produts(1) """
    db.close_connection()