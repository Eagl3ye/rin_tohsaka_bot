import os														#OS
import time														#TIME
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

while True:
	time.sleep(1)
	clt = time.strftime("%H %M", time.localtime())
	if (clt == "10 6"):
		cur.execute("UPDATE kidz SET isDailyClaimed = False;")
		conn.commit()
		print("[SERVER] |\tResetting dailies...")

#cur.execute("SELECT * FROM kidz ORDER BY id ASC;")
#cur.execute("UPDATE kidz SET mono = 1 WHERE id = 1;")
#try:
#	cur.execute("CREATE TABLE kidz (id serial PRIMARY KEY, usr_id text UNIQUE, mono integer);")
#	print("\n\nCREATED TABLE NAMED kidz...\n\n")
#except psycopg2.DatabaseError:
#	conn.rollback()
#	pass
#cur.execute("ALTER TABLE kidz ADD daily bool")
#conn.commit()
#conn.close()