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

    def insert_client(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO cliente (nome,cpg,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)",tupla)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM cliente")
            clientes = self.cursor.fetchall()
            return clientes

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

    def update_client(self,lista):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE cliente 
                                SET nome =  '{lista[1]}', 
                                cpg = '{lista[2]}', 
                                login = '{lista[3]}', 
                                senha = '{lista[4]}', 
                                fone = '{lista[5]}', 
                                cidade = '{lista[6]}' 
                                WHERE id = {lista[0]}
                                """)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
            self.conn.commit()
            return True

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
    """ db.connect() """
    """ db.insert_client() """
    """ db.select_client() """
    """ db.select_client_by_id(3) """
    """ db.delete_client(3) """
    """ db.update_client(4) """
    """ db.close_connection() """