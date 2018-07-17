import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()
#try:
#  cur.execute("ALTER TABLE kidz (usr_id text, mono text);")
#except psycopg2.DatabaseError:
#  pass
  
conn.commit()

cur.close()
conn.close()
