__name__ = "tile"

maxzoom = 30

class Tile:
	def __init__(self, z = 0, x = 0, y = 0):
		assert(0 <= z <= self.maxzoom())
		assert(x < pow(2, z))
		assert(y < pow(2, z))
		self.initz = z
		self.z = z
		self.minx_ = x
		self.maxx_ = x
		self.miny_ = y
		self.maxy_ = y

	def __str__(self):
		ret =  "(:amount " + str(self.amount())
		ret = ret + ":minx " + str(self.minx())
		ret = ret + ":maxx " + str(self.maxx())
		ret = ret + ":miny " + str(self.miny())
		ret = ret + ":maxx " + str(self.maxy()) + ")"
		return ret

	def zoomin(self):
		assert(self.z < self.maxzoom())
		self.minx_ = 2*self.minx_
		self.maxx_ = 2*self.maxx_ + 1
		self.miny_ = 2*self.miny_
		self.maxy_ = 2*self.maxy_ + 1
		self.z = self.z + 1

	def zoomout(self):
		assert(self.z > self.initz)
		self.minx_ = int(self.minx_ / 2)
		self.maxx_ = int((self.maxx_ - 1) / 2)
		self.miny_ = int(self.miny_ / 2)
		self.maxy_ = int((self.maxy_ - 1) / 2)
		self.z = self.z - 1

	def scalein(self, dz):
		assert(self.z + dz <= self.maxzoom())
		for i in range(0, dz):
			self.zoomin()

	def scaleout(self, dz):
		assert(self.z - dz >= self.initz)
		for i in range(0, dz):
			self.zoomout()

	def scale(self, dz):
		self.scalein(dz) if dz > 0 else self.scaleout(dz)

	def amount(self):
		return (self.maxx_ - self.minx_ + 1)*(self.maxy_ - self.miny_ + 1)

	def reset(self):
		self.scaleout(self.z - self.initz)

	def level(self):
		return self.z

	def ilevel(self):
		return self.initz

	def maxx(self):
		return self.maxx_

	def minx(self):
		return self.minx_

	def maxy(self):
		return self.maxy_

	def miny(self):
		return self.miny_

	def maxzoom(self):
		return maxzoom
