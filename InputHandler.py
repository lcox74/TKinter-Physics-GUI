# Local files
from Shapes import Rect, Circle

class InputHandler:
    def __init__ (self, win):
        self.MouseX, self.MouseY = (0, 0) # Mouse position (Event binded in main.py)

        self.window = win # A Reference to the window allowing access to the GUI Controller and Object Controller

        self.GUIFocus = False # Is the mouse over the properties side of the GUI

        # Bind the mouse events to the InputHandler Functions (In relation to the properties frame)
        self.window.guiController.frame.bind('<Enter>', self.EnteredProperties)
        self.window.guiController.frame.bind('<Leave>', self.ExitedProperties)

    '''
    Use the Enter and Leave mouse events in relation to the properties frame to determine 
    if the mouse focus is on the scene. This is useful because we want to make it not create
    and object if we are trying to change properties
    '''
    def EnteredProperties (self, e):
        self.GUIFocus = True
    def ExitedProperties (self, e):
        self.GUIFocus = False

    def MouseMovement (self, e):
        self.MouseX, self.MouseY = (e.x, e.y)
        # print(self.MouseX, ", ", self.MouseY)

    '''
    The Mouse Button Left Down event function first checks if the scene area is in focus. 
    If the mouse is within the properties side of the GUI then it returns and skips the function.

    But if it isn't, the function goes through a makeshift switch and case setup as python doesn't
    support switch and case statements unfortunately.

    If the shape selected in the properties section is a Rectangle and creates a new Rect object.
    If it is a circle instead it creates a new Circle object
    '''
    def MouseButtonLeftDown (self, e): # Add Object
        if self.GUIFocus:
            return

        def MakeRect ():
            s = Rect(self.MouseX, self.MouseY, int(self.window.guiController.width.get()), \
                                               int(self.window.guiController.height.get()))
            s.SetFill(self.window.guiController.fillColour['text'])
            s.SetOutlineColour(self.window.guiController.lineColour['text'])
            s.SetOutlineThickness(int(self.window.guiController.lineWidth.get()))

            self.window.objectController.addObject(s)

        def MakeCircle ():
            c = Circle(self.MouseX, self.MouseY, int(self.window.guiController.radius.get()))
            c.SetFill(self.window.guiController.fillColour['text'])
            c.SetOutlineColour(self.window.guiController.lineColour['text'])
            c.SetOutlineThickness(int(self.window.guiController.lineWidth.get()))

            self.window.objectController.addObject(c)

        tempSwitch = { 0 : MakeRect, 1 : MakeCircle}
        tempSwitch.get(self.window.guiController.shapeIndex)()

    # Try to remove an object if there is an object there to delete
    def MouseButtonRightDown (self, e): # Delete Object
        self.window.objectController.tryToRemoveObject(self.MouseX, self.MouseY)