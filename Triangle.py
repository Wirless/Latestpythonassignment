

import math




class Triangle:
	'''
	Emulates a triangle 
	'''
	def __init__(self, b, h):
		'''
		(num, num) -> obj
		Constructor
		'''
		self.base = b
		self.height = h
		self.color = (0, 255, 0)
		self.position = [20, 20]
		
	def __str__(self):
		'''
		(triangle) -> str
		String representation of triangle used by print function print(triangle)
		>>> x = Triangle(b=10,h=5)
		>>> print(x)
		Triangle base = 10
		Triangle height = 5
		Triangle color = (0, 255, 0)
		Triangle position = [20, 20]
		'''
		return f" Triangle base = {self.base}\n Triangle height = {self.height}\n Triangle color = {self.color}\n Triangle position = {self.position}"
		
	def __repr__(self):
		'''
		(triangle) -> str
		A string representation of the Triangle
		>>> x = Triangle(b=10,h=5)
		>>> x
		<Triangle Object>
		height: 10;
		base: 5;
		color: (0,255,0);
		position: [20,20];
		'''
		return f"<Triangle object>\n height: {self.height};\n base: {self.base};\n color: {self.color}\n position: {self.position}"
		
	def area(self):
		'''
		(triangle) -> num
		returns the area of a triangle
		>>> x = Triangle(b=10,h=5)
		>>> Triangle.area(x)
		25
		'''
		return (self.base*self.height)/2
		
	def perimeter(self):
		'''
		(triangle) ->num
		returns the perimeter of a triangle
		'''
		newbase = self.base/2
		pit = (newbase**2)+(self.height**2)
		hype = math.sqrt(pit)
		return hype+hype+self.base
		
	def set_color(self, color):
		'''
		sets color of triangle
		(int)+(int)+(int) -> obj.color
		'''
		self.color = color
		return True
	
	def set_pos(self,position):
		'''
		sets triangle position
		(int)+(int) -> obj.pos
		'''
		self.position = position
		return True
	
	def draw(self):
		'''
		draw the triangle
		(obj) -> obj
		'''
		print(self.position)
		return True
		
if __name__ == "__main__":
	x = Triangle(20,20)
	print(x)
	print(x.perimeter())
	print(x.area())
	x.set_color((100, 100, 100))
	x.set_pos([100,100])
	print(x)
	print(x.__repr__())