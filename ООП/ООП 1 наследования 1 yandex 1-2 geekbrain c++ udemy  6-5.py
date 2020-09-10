 # foxford 3 - oop class - mindmap  - tasks 3 - 
class Shape(object):
	"""docstring for Shape"""
	def __init__(self):
		super(Shape, self).__init__()
		# self.arg = arg
		print('Shape: Init')
		self.legs = 0


	def draw(self):
		print('drawing a Shape')

	def area(self):
		print('calc area')

	def perimeter(self):
		print('calc perimeter')

shape = Shape()

print(shape)
