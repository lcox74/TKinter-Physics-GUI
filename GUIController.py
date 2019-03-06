from tkinter import *
import tkinter.colorchooser

class GUIController:
	def __init__ (self, win, root):
		self.frame = Frame(root, bg='#D7D7D7')
		self.frame.place(relx=0.7, relwidth=0.3, relheight=1)

		self.window = win

		self.shapeIndex = 1
		self.shapes = ['Rectangle', 'Circle']

		self.InitialiseGUI()

	def InitialiseGUI (self):
		self.shapeTextString = StringVar()
		self.shapeTextString.set(self.shapes[self.shapeIndex])
		shapeLabel = Label(self.frame, textvariable=self.shapeTextString, font=20, bg='#EFEFEF')
		shapeLabel.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

		leftButton = Button(self.frame, text="<", command=self.LeftButtonPressed)
		leftButton.place(relx=0.1, rely=0.16, relwidth=0.4, relheight=0.05)

		rightButton = Button(self.frame, text=">", command=self.RightButtonPressed)
		rightButton.place(relx=0.5, rely=0.16, relwidth=0.4, relheight=0.05)

		fillLabel = Label(self.frame, text="Fill Colour", bg='#D7D7D7')
		fillLabel.place(relx=0.1, rely=0.23, relwidth=0.8, relheight=0.05)
		self.fillColour = Button(self.frame, text='#ffffff', bg='#ffffff', justify=CENTER, command=lambda: self.PickColour(self.fillColour))
		self.fillColour.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.05)

		linecLabel = Label(self.frame, text="Outline Colour", bg='#D7D7D7')
		linecLabel.place(relx=0.1, rely=0.33, relwidth=0.8, relheight=0.05)
		self.lineColour = Button(self.frame, text='#101010', bg='#101010', justify=CENTER, command=lambda: self.PickColour(self.lineColour))
		self.lineColour.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.05)

		linewLabel = Label(self.frame, text="Outline Width", bg='#D7D7D7')
		linewLabel.place(relx=0.1, rely=0.43, relwidth=0.8, relheight=0.05)
		self.lineWidth = Entry(self.frame, justify=CENTER)
		self.lineWidth.insert(0, '1')
		self.lineWidth.place(relx=0.1, rely=0.47, relwidth=0.8, relheight=0.05)


		# Shape Specific Values
		# -----------------------------
		
		self.shapeSpecificString = StringVar()
		sizeLabel = Label(self.frame, textvariable=self.shapeSpecificString, font=5, bg='#D7D7D7')
		sizeLabel.place(relx=0.1, rely=0.59, relwidth=0.8, relheight=0.05)

		# Circle
		self.radius = Entry(self.frame, justify=CENTER)
		self.radius.insert(0, '20')
		self.radius.place(relx=0.1, rely=0.64, relwidth=0.8, relheight=0.05)

		# Rect
		self.width = Entry(self.frame, justify=CENTER)
		self.width.insert(0, '20')
		self.width.place(relx=0.1, rely=0.64, relwidth=0.4, relheight=0.05)

		self.height = Entry(self.frame, justify=CENTER)
		self.height.insert(0, '20')
		self.height.place(relx=0.5, rely=0.64, relwidth=0.4, relheight=0.05)
		# -----------------------------
		
		self.RefreshHiddenItems()

	def LeftButtonPressed (self):
		self.shapeIndex = (self.shapeIndex - 1) % len(self.shapes)
		self.shapeTextString.set(self.shapes[self.shapeIndex])
		self.RefreshHiddenItems()

	def RightButtonPressed (self):
		self.shapeIndex = (self.shapeIndex + 1) % len(self.shapes)
		self.shapeTextString.set(self.shapes[self.shapeIndex])
		self.RefreshHiddenItems()

	def RefreshHiddenItems (self):
		def Rect ():
			self.width.place(relx=0.1, rely=0.64, relwidth=0.4, relheight=0.05)
			self.height.place(relx=0.5, rely=0.64, relwidth=0.4, relheight=0.05)

			self.radius.place_forget()

			self.shapeSpecificString.set("Width & Height")

		def Circle ():
			self.radius.place(relx=0.1, rely=0.64, relwidth=0.8, relheight=0.05)

			self.width.place_forget()
			self.height.place_forget()

			self.shapeSpecificString.set("Radius")

		tempSwitch = { 0 : Rect, 1 : Circle }
		tempSwitch.get(self.shapeIndex)()

	def PickColour (self, widget):
		color = tkinter.colorchooser.askcolor()[1]
		widget.config(bg=color, text=color)