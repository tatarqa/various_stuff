import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PsqlTools:
    def __init__(self, con=None, configs={}):

        self.con=con
        self.configs=configs


    def config_entity(self,argz):

        conf_name,arguments=argz
        self.configs[conf_name] = []
        print(f'\n[*]Config - {conf_name}')
          for arg in arguments:
            self.configs[conf_name].append(input(f'[*]{arg} -> '))


    def conect_to_db(self):

        PSQL_DEFAULT_DB,PSQL_USER_NAME,PSQL_HOST,PSQL_PW = self.configs['conect_to_db']
        self.con = psycopg2.connect(f"dbname='{PSQL_DEFAULT_DB}' user='{PSQL_USER_NAME}' host='{PSQL_HOST}' password='{PSQL_PW}'")
        


    def create_user_and_db(self):
        
        NEW_DB_NAME,NEW_USER_NAME,NEW_USER_PW = self.configs['create_user_args']
        commands = (
            f"""
            CREATE DATABASE {NEW_DB_NAME};
            CREATE USER {NEW_USER_NAME} WITH PASSWORD '{NEW_USER_PW}';
            ALTER ROLE {NEW_USER_NAME} SET client_encoding TO 'utf8';
            ALTER ROLE {NEW_USER_NAME} SET default_transaction_isolation TO 'read committed';
            ALTER ROLE {NEW_USER_NAME} SET timezone TO 'UTC';
            GRANT ALL PRIVILEGES ON DATABASE {NEW_DB_NAME} TO {NEW_USER_NAME};
            """
            )
        
        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = self.con.cursor()
        for command in commands.strip().splitlines():
            cur.execute(command)
        cur.close()


    

if __name__ == '__main__':
    tooler=PsqlTools()
    #conect to db
    args=('conect_to_db',['PSQL_DEFAULT_DB_NAME','PSQL_USER_NAME','PSQL_HOST','PSQL_PW'])
    tooler.config_entity(args)
    tooler.conect_to_db()

    #create user/perm/db
    args=('create_user_args',['NEW_DB_NAME','NEW_USER_NAME','NEW_USER_PW'])
    tooler.config_entity(args)
    tooler.create_user_and_db()