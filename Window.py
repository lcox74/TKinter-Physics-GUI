from tkinter import Tk, Canvas, Frame, BOTH, Button, Toplevel
import time

# Controllers and Handlers
from ObjectController import ObjectController
from GUIController import GUIController
from InputHandler import InputHandler

'''
Create a small window that allows the user to press a button that runs the acctual app.
Use as the App Launcher, popular for alot of AAA PC games recently
'''
class Launcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Launcher")

         # Create the frame and button that allows interaction
        self.frame = Frame(self.root)
        self.button = Button(self.frame, text = 'Launch Program', width = 25, command = self.launch) # Call self.launch() when pressed
        self.button.pack()
        self.frame.pack()

    def launch(self):
        self.new_window = Toplevel(self.root) # Create a new window that appears above the launcher window before
        self.app = App(self.new_window) # Create a new App instance onto the new window
        self.root.destroy() # Close Launcher window when the app closes

class App:
    def __init__(self, root):
        # Window Size Variables
        self.WIDTH, self.HEIGHT = (800,600)
        self.root = root

        self.root.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT)) # Set Window Size
        self.root.resizable(False, False) # Not Resizable

        # Setup the window canvas
        self.canvas = Canvas(root, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        # Shape Object Controller Initialiser
        self.objectController = ObjectController(self)

        # GUI Handler Initialiser
        self.guiController = GUIController(self, root)

        # Input Handler Initialiser
        self.inputHandler = InputHandler(self)
        root.bind('<Motion>', self.inputHandler.MouseMovement) # This sets up the Mouse Movement Event
        root.bind('<Button 1>', self.inputHandler.MouseButtonLeftDown) # This is Left Mouse Button Click Event bind
        root.bind('<Button 3>', self.inputHandler.MouseButtonRightDown) # This is Right Mouse Button Click Event bind

        self.Update()

    # Send the update call to the Object Controller
    def Update (self):

        '''
        Set a max FPS and get a reference the the time in seconds.

        This is useful as it allows an object to travel the same
        distance if the elapsedtime is multiplied by the speed.
        '''
        elapsedTime = 0 # Initial Frame
        MaxFPS = 60
        fpsHistory = []
        fpsHistorySmooth = 10

        while True:
            # If the contents of the try statement can't be done, exit the while lop and close the App
            try:
                # Get the time at the beginning of the frame
                startTime = time.time()

                # Update the object positions and draw GUI to the screen
                self.objectController.Update(elapsedTime)
                self.objectController.Draw()
                self.root.update() # Updates the window

                # Get the difference between the current time and the time before the update calls of the frame                
                elapsedTime = time.time() - startTime
                if elapsedTime < 1/MaxFPS: # If the difference is smaller than the max fps it means it was faster.
                    time.sleep(1/MaxFPS - elapsedTime) # Sleep the program down to the max fps to cap it and keep consistency
                    elapsedTime = 1/MaxFPS

                fpsHistory.append(elapsedTime) # Create a history of the delta times between the frames
                if len(fpsHistory) > fpsHistorySmooth: # If the history has more than 10 remove the oldest as it isn't relevant
                    fpsHistory.pop(0) # Remove the oldest delta time from the history list

                # Change the title of the window to display the averaged fps so the user can see performace drops
                self.root.title("TKInter GUI Project | fps:" + str(int(1/(sum(fpsHistory)/float(len(fpsHistory))))))
                
            except Exception as e:
                print(e)
                return



        