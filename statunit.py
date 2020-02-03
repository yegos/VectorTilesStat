import statistics
__name__ = "statunit"

class Statunit:
	def __init__(self, formats = ["png", "mvt"]):
		self.dictionary = {}
		self.formats_ = formats
		for format in self.formats():
			self.dictionary[format] = []

	def push(self, format, value):
		assert(self.formats().count(format) == 1)
		assert(isinstance(value, float))
		self.dictionary[format].append(value)

	def mean(self, format):
		assert(self.formats().count(format) == 1)
		assert(len(self.dictionary[format]) > 0)
		return statistics.mean(self.dictionary[format])

	def clean(self):
		for format in self.formats():
			self.dictionary[format].clear()

	def formats(self):
		return self.formats_
