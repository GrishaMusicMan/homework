from random import randint

class cube:

	def __init__(self, number_of_sides:int):
		self.number_of_sides = number_of_sides

	def shot(self):
		return randint(1, self.number_of_sides)

cube_1 = cube(6)
cube_2 = cube(20)

print(cube_1.shot())
print(cube_2.shot())