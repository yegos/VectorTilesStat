import time
__name__ = "clicker"

class Clicker:
	def __init__(self):
		self.click()

	def click(self):
		self.time = time.time()

	def get(self):
		return time.time() - self.time
