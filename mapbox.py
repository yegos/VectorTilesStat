import wget
import os
from clicker import Clicker
__name__ = "mapbox"

mapboxurl = "http://a.tiles.mapbox.com/v4/mapbox.mapbox-streets-v7"
mapboxtoken = "pk.eyJ1Ijoidm9sZ2FyZW5vayIsImEiOiJjamloYmdiemowMDBzM2tvMXJydXhneWZ4In0.cODw23Z8ss2Np17zXPBZCA"

format_dictionary = {
	"png": "png_tiles",
	"mvt": "mvt_tiles"
}

def applyToken(url, token):
	return url + "?access_token=" + token

def addDimention(url, dimention):
	return url + "/" + str(dimention)

def addFormat(url, format):
	return url + "." + format

class Mapbox:
	def __init__(self, url = mapboxurl, token = mapboxtoken):
		self.url = url
		self.token = token

	def get(self, z, x, y, format):
		assert(0 <= z <= 30)
		assert(x < pow(2, z))
		assert(y < pow(2, z))
		destination_dir = self.folder(format)
		url = addDimention(self.url, z)
		url = addDimention(url, x)
		url = addDimention(url, y)
		url = addFormat(url, format)

		url = applyToken(url, self.token)
		cl = Clicker()
		filename = wget.download(url, out = destination_dir)
		time = cl.get()
		os.remove(filename)
		return time

	def folder(self, format):
		assert(isinstance(format, str))
		return "geodata/" + format_dictionary[format]
		
