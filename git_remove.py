# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

from git_remover import remove_git


# Function for opening the
# file explorer window
def browseFiles():
    # filename = filedialog.askopenfilename(initialdir="/",
    #                                       title="Select a File",
    #                                       filetypes=(("Text files",
    #                                                   "*.txt*"),
    #                                                  ("all files",
    #                                                   "*.*")))
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ))
    text = remove_git(file=filename)
    # Change label contents
    label_file_explorer.configure(text="Result" + text)



# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("700x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Remove .git folders",
                            width=100, height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)
button_ok = Button(window,
                   text="Ok",
                   command=window.destroy)
button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# Let the window wait for any events
window.mainloop()
