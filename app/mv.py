# Import path module from os

from os import path
import shutil

def mv():

    source_path = "sg.txt"
    path.exists(source_path)
    destination_path = "templates"
    shutil.move(source_path, destination_path)
