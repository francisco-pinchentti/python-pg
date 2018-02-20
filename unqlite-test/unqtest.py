from unqlite import UnQLite

db = UnQLite('unqlite.dbexample')	# Leave empty to create an in-memory database
db['foo'] = 'bar' 			# Use as a key/value store.

with open('sampleB64.txt') as file:
	b64str = file.read()

map_entry = {
	"gridSize": 32,
	"rectangles": [ 0, 1, 0],
	"bg": b64str
}

exportedMaps = db.collection('exportedMaps')
exportedMaps.create()
exportedMaps.store(map_entry)
e = exportedMaps.fetch(0)
print e['bg'].strip()

