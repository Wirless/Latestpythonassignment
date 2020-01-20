

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
		self.pos = [20, 20]
		
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
		return f"Triangle base = {self.base}\n Triangle height = {self.height}\n Triangle color = {self.color}\n Triangle position = {self.pos}"
		
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
		return (b*h)/2
		
	def perimeter(self):
		'''
		(triangle) ->num
		returns the perimeter of a triangle
		'''
		newbase = b/2
		pit = (newbase**2)+(h**2)
		return math.sqrt(pit+b+h)
		
	def set_color(newcolor):
		'''
		sets color of triangle
		(int)+(int)+(int) -> obj.color
		'''
		return self.color = newcolor
	
	def set_pos(posz):
		'''
		sets triangle position
		(int)+(int) -> obj.pos
		'''
		return self.pos = posz
	
	def draw(self):
		'''
		draw the triangle
		(obj) -> obj
		'''
		return self.triangle