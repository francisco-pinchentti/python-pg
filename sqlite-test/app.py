import sqlite3

conn = sqlite3.connect('sqlite3.dbexample')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS maps')
c.execute('CREATE TABLE maps (id int, grid_size int, rectangles_state text, bg text)')

with open('sampleB64.txt') as file:
	b64str = file.read()

# note that rectangle state needs to be converted to a CSV in order to store them:
tupleToInsert = (1, 32, '0,1,0', b64str)

c.execute('INSERT INTO maps (id, grid_size, rectangles_state, bg) VALUES (?,?,?,?)', tupleToInsert)

for r in c.execute('SELECT * FROM maps WHERE ID = 1'):
	for attr in r:
		print attr
c.close()
