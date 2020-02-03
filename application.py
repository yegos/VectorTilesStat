from mapbox import Mapbox
from harvester import Harvester
from tile import Tile
from clicker import Clicker

mapbox = Mapbox()
print("png-z0: " + str(mapbox.get(0, 0, 0, "png")))
print("mvt-z0: " + str(mapbox.get(0, 0, 0, "mvt")))
print("png-z30: " + str(mapbox.get(30, 0, 0, "png")))
print("mvt-z30: " + str(mapbox.get(30, 0, 0, "mvt")))

harvester = Harvester(["png", "mvt"])
tile = Tile(7, 25, 53)
cl = Clicker()
while tile.level() != 31:
	print(str(tile))
	results = harvester.fill(tile, 1000)
	print(tile.level(), end=": ")
	print(results)
	tile.zoomin()
	harvester.clean()
print(cl.get())

