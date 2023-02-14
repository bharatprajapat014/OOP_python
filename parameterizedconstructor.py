class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, fst, snd):
		self.first = fst
		self.second = snd

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(2000, 2000)

# creating second object of same class
obj2 = Addition(100, 200)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()