import math

# Local files
from Shapes import Shape, Circle, Rect

class ObjectController:
	def __init__(self, win):
		self.objects = [] # List of all shape objects in the scene
		self.window = win # A reference to the window class allowing function calls to the GUI Controller and Input Handler
		self.canvas = win.canvas # A reference to the canvas for shape drawing

	# Update is called once a frame and updates every object in the scene object list
	# A try and except is used so when any movement of the screen doesn't cause an division error when limiting frame rate
	def Update (self, elapsedTime): # Elapsed time is multiplied by speeds to keep a consistent movement regardless of frame rate change
		for o in self.objects:
			try:
				o.update(elapsedTime)
			except Exception as e:
				continue
			

	# Much like Update, Draw is called once a frame to draw each shape in the sceen object list
	# Thr canvas is cleared first so there are no trails from the previous frames canvas
	def Draw (self):
		self.canvas.delete("all")
		for o in self.objects:
			o.draw()

	# Adds a reference shape to the object list as well as making the shape parsed through a child to the Object Controller
	def addObject (self, o):
		o.controller = self
		self.objects.append(o);

	# This function is called everytime you press the right mouse button and checks if the mouse is in the bounds of an object
	# in the Scene. If it is then it deletes it by removing it from the list so it can't be rendered or updated again
	def tryToRemoveObject(self, mx, my):
		for o in self.objects:
			# Due to Circles having a radius instead of a width and height variable the 
			# calculations between the two objects have to be slightly different
			if type(o) == Circle: 
				dist = math.sqrt((mx - o.x)**2 + (my - o.y)**2) # Pythagoras' Theorem
				if dist <= o.radius:
					self.objects.remove(o)
			else:
				if mx > o.x - o.width / 2 and mx < o.x + o.width / 2:
					if my > o.y - o.height / 2 and my < o.y + o.height / 2:
						self.objects.remove(o)
