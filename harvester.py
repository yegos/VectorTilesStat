import math
from tile import Tile
from mapbox import Mapbox
from statunit import Statunit
__name__ = "harvester"

class Harvester:
	def __init__(self, formats):
		self.mapbox = Mapbox()
		self.sunit = Statunit(formats)

	def fill(self, tile, amount):
		assert(isinstance(tile, Tile))
		step = tile.amount() / amount
		returnable = []
		for format in self.sunit.formats():
			counter = 0
			while counter < amount:
				diffx = 0
				x = tile.minx()
				while x <= tile.maxx():
					diffy = 0
					y = tile.miny()
					while y <= tile.maxy():
						if (x >= pow(2, tile.level()) or y >= pow(2, tile.level())):
							print(str(tile))
						self.sunit.push(format, self.mapbox.get(tile.level(), x, y, format))
						counter = counter + 1
						diffy = diffy + step
						y = tile.miny() + math.ceil(diffy)
					diffx = diffx + step
					x = tile.minx() + math.ceil(diffx)
			returnable.append(self.sunit.mean(format))
		return returnable

	def clean(self):
		self.sunit.clean()
