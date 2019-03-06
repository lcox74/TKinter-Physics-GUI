# Local Files
from Shapes import Shape

class Rect (Shape):
	def __init__(self, x, y, w, h):
		Shape.__init__(self, x, y)

		self.width = w
		self.height = h

	def Update (self, elapsedTime):
		# Clamping to screen space
		if self.x < self.width/2:
			self.x = self.width/2
		elif self.x > 800 * 0.7 - self.width/2:
			self.x = 800 * 0.7 - self.width/2
		if self.y < self.height/2:
			self.y = self.height/2
		elif self.y > 600 - self.height/2:
			self.y = 600 - self.height/2

		for o in self.controller.objects:
			if o == self: # If the object is itself skip to next object in list
				continue

			# Currently Rectangle collisions aren't working
			# if type(o) is Rect: # Collisions and displacements made from circle collisions against circles
			# 	if self.y + self.height/2 > o.y - o.height/2 and self.y - self.height/2 > o.y + o.height/2: 
			# 		if self.x + self.width/2 > o.x - o.width/2 and self.x - self.width/2 > o.x + o.width/2:
			# 			print("Rect Collided with Rect")
			# 			if self.x < o.x:
			# 				self.x = o.x - o.width/2 - self.width/2
			# 			else:
			# 				self.x = o.x + o.width/2 + self.width/2

			# 			if self.y < o.x:
			# 				self.y = o.y - o.height/2 - self.height/2
			# 			else:
			# 				self.y = o.y + o.height/2 + self.height/2
				
	
	# Interface function, called after each update. Once a frame
	def draw (self):
		self.controller.canvas.create_rectangle(self.x - self.width/2, self.y - self.height/2, self.x + self.width/2, self.y + self.height/2, outline=self.lineColour, fill=self.fillColour, width=self.lineThickness)
