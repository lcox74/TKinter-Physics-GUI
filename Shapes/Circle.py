import math

# Local Files
from Shapes import Shape, Rect

class Circle (Shape):
	def __init__(self, x, y, r):
		Shape.__init__(self, x, y)

		self.radius = r

	def Update (self, elapsed_time):
		# Clamping to screen space
		if self.x < self.radius:
			self.x = self.radius
		elif self.x > 800 * 0.7 - self.radius:
			self.x = 800 * 0.7 - self.radius
		if self.y < self.radius:
			self.y = self.radius
		elif self.y > 600 - self.radius:
			self.y = 600 - self.radius

		for o in self.controller.objects:
			if o == self: # If the object is itself skip to next object in list
				continue
			
			if type(o) is Circle: # Collisions and displacements made from circle collisions against circles
				# Algorithm derived from javidx9 video 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwi2rPKs4NrgAhXUXCsKHQHhCywQwqsBMAB6BAgGEAQ&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DLPzyNOHY3A4&usg=AOvVaw3BCk5eqvPaUxDGaZrDP7sd'
				if (self.__CircleOverlap(o)):
					print("Circle Collided with Circle")
					circleDist = math.sqrt((self.x - o.x)**2 + (self.y - o.y)**2) # Calculate the distance between circles
					circleOverlap = 0.5 * (circleDist - self.radius - o.radius) # Calculate half overlap of the overlap distance to displace both circles equally

					# This Object's Displacement. Overlap distance * direction
					self.x -= circleOverlap * (self.x - o.x) / circleDist
					self.y -= circleOverlap * (self.y - o.y) / circleDist

					# Target Object Displacement. Overlap distance * direction. Opposite direction + not -
					o.x += circleOverlap * (self.x - o.x) / circleDist
					o.y += circleOverlap * (self.y - o.y) / circleDist
			elif type(o) is Rect:
				if self.__RectangleOverlap(o):
					print("Circle Collided with Rect")

	# Private function returns a boolean if this current circle is overlapping a target. Should make static for broader use
	def __CircleOverlap (self, target):
		return math.fabs((self.x - target.x)**2 + (self.y - target.y)**2) <= (self.radius + target.radius)**2

	# Function by e.James 'stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection'
	def __RectangleOverlap (self, target):
		circleDistX = abs(self.x - target.x - target.width/2)
		circleDistY = abs(self.y - target.y - target.height/2)

		if (circleDistX > (target.width/2 + self.radius)): return False
		if (circleDistY > (target.height/2 + self.radius)): return False

		if (circleDistX <= target.width/2): return True
		if (circleDistY <= target.height/2): return True

		cornerDist = (circleDistX - target.width)**2 + (circleDistY - target.height)**2
		return (cornerDist <= self.radius**2)

	# Interface function, called after each update. Once a frame
	def draw (self):
		self.controller.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, outline=self.lineColour, fill=self.fillColour, width=self.lineThickness)

	