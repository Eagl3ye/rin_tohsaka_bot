import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()
try:
  cur.execute("CREATE TABLE kidz (usr_id text, money integer);")
except ProgrammingError:
  pass
#cur.execute("DROP TABLE test;")

conn.commit()

cur.close()
conn.close()
