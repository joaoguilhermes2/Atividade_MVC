import mysql.connector

class Database():
    def __init__(self, banco="syspython"):
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            database=self.banco,
            user='root',
            password=''
        )

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com Sucesso!!!",db_info)
        else:
            print("ERROR")

    def insert_client(self):
        self.connect()
        try:
            args = ("Anderson","74329434382","anderson@hotmail.com","34527","6729554134","São Paulo") # Tupla com os parâmetros para commitar no banco
            self.cursor.execute("INSERT INTO cliente (nome,cpg,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)",args)
            self.conn.commit()
            print("Cliente Cadastrado com Sucesso!!!")

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM cliente")
            clientes = self.cursor.fetchall()
            for cli in clientes:
                print(cli)

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
            cli = self.cursor.fetchone()
            return cli

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_client(self,id):
        self.connect()
        try:
            cliente = list(self.select_client_by_id(id))
            if not cliente:
                print("Cliente não encontrado!")
                return
            
            print(f"Dados atuais do Cliente: {cliente}")

            cliente[1] = input("Digite o novo nome: ")
            cliente[2] = input("Digite o novo CPF: ")
            cliente[3] = input("Digite o novo login: ")
            cliente[4] = input("Digite o novo senha: ")
            cliente[5] = input("Digite o novo fone: ")
            cliente[6] = input("Digite o novo cidade: ")

            self.cursor.execute(f"""
                                UPDATE cliente 
                                SET nome =  '{cliente[1]}', 
                                cpg = '{cliente[2]}', 
                                login = '{cliente[3]}', 
                                senha = '{cliente[4]}', 
                                fone = '{cliente[5]}', 
                                cidade = '{cliente[6]}' 
                                WHERE id = {cliente[0]}
                                """)
            self.conn.commit()
            cli_atualizado = self.select_client_by_id(cliente[0])
            print(cli_atualizado)

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
            self.conn.commit()
            print("Cliente Deletado com Sucesso!!!")

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão Encerrada com Sucesso!!!")

if __name__ == '__main__':
    db = Database()
    """ db.insert_client()
    db.select_client()
    db.select_client_by_id(3)
    db.delete_client(3)
    db.update_client(4)
    db.close_connection() """