from peeweedbevolve import evolve

from models.db import db_connection, MARIADB

def run_migrations():
  print(MARIADB['db_name'])
  evolve(db = db_connection, interactive = False, schema = MARIADB['db_name'], ignore_tables = None)

if __name__ == '__main__':
  run_migrations()