import tkinter
from tkinter import *

# import filedialog module
from tkinter import filedialog

from git_remover import remove_git



def open_files():
    """Returns list of filenames+paths given starting dir"""

    root = Tk()
    root.withdraw()  # Hide root window
    # filenames = filedialog.askopenfilenames(parent=root,initialdir=starting_dir)
    filenames = filedialog.askopenfilename(parent=root,
                                           filetypes=[("Txt file", "*.txt*")])
    text  = remove_git(filenames)
    # tkinter.messagebox.OK = 'text'

    return filenames


open_files()

if __name__ == '__main__':
    open_files()
