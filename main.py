from tkinter import Tk

# Local Files
from Window import Launcher

___author___ = "Lachlan Cox"
___date___ = "26/2/2019"

# Create a window and create the launcher
def run ():
    root = Tk()
    win = Launcher(root)
    root.mainloop()

'''
If this was the file that was set to run then launch the application. Else do nothing.
The application can only run if this was the file set to run. 'py main.py'
'''
if __name__ == '__main__':
    run()