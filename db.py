import os														#OS
import time														#TIME
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
cur.execute("CREATE TABLE kidz (id serial PRIMARY KEY, usr_id text UNIQUE, mono integer);")
cur.execute("ALTER TABLE kidz ADD daily bool")
conn.commit()
conn.close()

while True:
	time.sleep(1)
	clt = time.strftime("%H %M %S", time.localtime())
	if (clt == "23 59 59"):
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		cur.execute("UPDATE kidz SET isDailyClaimed = False;")
		conn.commit()
		conn.close()
		print("[SERVER] |\tResetting dailies...")

'''
cur.execute("SELECT * FROM kidz ORDER BY id ASC;")
cur.execute("UPDATE kidz SET mono = 1 WHERE id = 1;")
try:
	cur.execute("CREATE TABLE kidz (id serial PRIMARY KEY, usr_id text UNIQUE, mono integer);")
	print("\n\nCREATED TABLE NAMED kidz...\n\n")
except psycopg2.DatabaseError:
	conn.rollback()
	pass
cur.execute("ALTER TABLE kidz ADD daily bool")
conn.commit()
conn.close()
'''
