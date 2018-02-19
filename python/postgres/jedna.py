import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PsqlTools:
    def __init__(self, con=None, configs={}):

        self.con = con
        self.configs = configs

    def config_entity(self, **kwargs):

        conf_name = kwargs['conf_name']
        query_params = kwargs['sqlparams']
        self.configs[conf_name] = []
        print(f'\n[*]Config for - {conf_name}')
        for query_param in query_params:
            self.configs[conf_name].append(input(f'[*]{query_param} -> '))

    def conect_to_db(self):

        PSQL_DEFAULT_DB, PSQL_USER_NAME, PSQL_HOST, PSQL_PW = self.configs['conect_to_db']
        self.con = psycopg2.connect(f"dbname='{PSQL_DEFAULT_DB}' user='{PSQL_USER_NAME}' host='{PSQL_HOST}' password='{PSQL_PW}'")
        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    def clear_config(self, cfg_name):
        del self.configs[cfg_name]

    def create_user(self):

        NEW_DB_NAME, NEW_USER_NAME, NEW_USER_PW = self.configs['create_user']
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

        cur = self.con.cursor()
        for command in commands.strip().splitlines():
            cur.execute(command)
        cur.close()
        clear_config('create_user')

    def delete_db(self):
        DB_TO_DROP = self.configs['drop_db']
        cur = self.con.cursor()
        cur.execute(f"DROP DATABASE {next(iter(DB_TO_DROP))};")
        cur.close()
        clear_config('drop_db')


if __name__ == '__main__':
    tooler = PsqlTools()

    tooler.config_entity(conf_name='conect_to_db', sqlparams=[
                         'PSQL_DEFAULT_DB_NAME', 'PSQL_USER_NAME', 'PSQL_HOST', 'PSQL_PW'])
    tooler.conect_to_db()

    tooler.config_entity(conf_name='create_user', sqlparams=[
                         'NEW_DB_NAME', 'NEW_USER_NAME', 'NEW_USER_PW'])
    tooler.create_user()

    tooler.config_entity(conf_name='drop_db', sqlparams=['DB_TO_DROP'])
    tooler.delete_db()
