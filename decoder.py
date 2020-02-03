import mapbox_vector_tile

filename = 'geodata/53.'
with open(filename + 'mvt', 'rb') as f:
	data = f.read()
decoded_data = mapbox_vector_tile.decode(data)
with open(filename + 'txt', 'w', encoding="utf-8") as f:
	f.write(repr(decoded_data))
