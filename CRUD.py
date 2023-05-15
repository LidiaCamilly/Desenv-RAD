import psycopg2
class dtbase:
    def __int__(self):
        print('Método Construtor')

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user='postgres',
                                               password='080268',
                                               host='127.0.0.1',
                                               port='5432',
                                               database='db_aula')
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print('Falha ao se conectar ao Banco de Dados', error)
    def selecionar(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            print('Selecionando todos os produtos')
            sql_select_query = """select * from public. "agenda" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)
        except (Exception, psycopg2.Error) as error:
            print('Erro in select operation', error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print('A conexão com o PostgreSQL foi fechada.')
        return registros

    def inserir(self, nome, telefone):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public. "agenda" 
            ("nome", "telefone") VALUES (%s,%s)"""
            record_to_insert = (nome, telefone)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print (count, "Pessoa inserida com sucesso na tabela AGENDA")

        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print('Falha ao inserir registro na tabela AGENDA', error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print('A conexão com PostgreSQL foi fechada')

    def atualizar(self, nome, telefone):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            update = """Update public. "agenda" set "nome" = %s, "telefone"= %s where "telefone" = %s """
            cursor.execute(update, (nome, telefone))
            self.connection.commit()
            count = cursor.rowcount
            print(count,'Agenda atualizada com sucesso')
        except (Exception, psycopg2.Error) as error:
            print('Erro na atualizaçãoo', error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print('A conexão com o PostgreSQL foi fechada')
    def exluir(self, nome):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            delete = """Delete from public. "agenda" where "nome" = %s """
            cursor.execute(delete, (nome))
            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Pessoa excluída com sucesso')
        except (Exception, psycopg2.Error) as erro:
            print('Erro na exclusão')
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print('A conexão com o PostgreSQL foi fechada')
