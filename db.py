import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

#cur.execute("DELETE FROM kidz WHERE usr_id = '@Konev#6479';")
try:
	cur.execute("CREATE TABLE kidz (id serial PRIMARY KEY, usr_id text UNIQUE, mono integer);")
	print("\n\nCREATED TABLE NAMED kidz...\n\n")
except psycopg2.DatabaseError:
	pass

conn.commit()
conn.close()
