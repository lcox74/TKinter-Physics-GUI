
# A Interface class that is to be inherited by shapes eg. Rectangle & Circle 
class Shape:
	def __init__ (self, x, y):
		self.x, self.y = (x, y) # Shape Position
		self.vx, self.vy = (0, 20) # Shape velocity with defaulted gravity
		self.ax, self.ay = (0, 0) # Shape acceleration

		# Object Attributes
		self.fillColour = '#ffffff'
		self.lineColour = '#000000'
		self.lineThickness = 1


		self.controller = 0 # Initialize to draw to a canvas	

	def update (self, elapsedTime):
		# Physics
		# Acceleration effected over time
		self.ax = -self.vx * 0.6	    # Horizontal friction slowing horizontal movment to 0
		self.ay = 98.1 * elapsedTime    # Constant Gravity

		# Add acceleration to velocity
		self.vx += self.ax * elapsedTime
		self.vy += self.ay * elapsedTime

		# Add velocity to position
		self.x += self.vx * elapsedTime
		self.y += self.vy * elapsedTime

		self.Update(elapsedTime) # Update independent shapes

	def Update (self, elapsedTime): # Interface Update Function
		pass

	def draw (self): # Interface Draw Function
		pass

	# Shape Attribute setters. Don't really need getters at the moment
	def SetFill (self, c): 
		self.fillColour = c
	def SetOutlineColour (self, c):
		self.lineColour = c
	def SetOutlineThickness (self, t):
		self.lineThickness = t
