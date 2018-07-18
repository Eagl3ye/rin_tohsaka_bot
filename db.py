import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("SELECT * FROM kidz ORDER BY id ASC;")
#cur.execute("UPDATE kidz SET mono = 1 WHERE id = 1;")
#try:
#	cur.execute("CREATE TABLE kidz (id serial PRIMARY KEY, usr_id text UNIQUE, mono integer);")
#	print("\n\nCREATED TABLE NAMED kidz...\n\n")
#except psycopg2.DatabaseError:
#	conn.rollback()
#	pass

conn.commit()
conn.close()
