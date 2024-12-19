import logging
import os
import shutil

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import rw_processes as rw
from text_processes import stem
from trie import PrefixTree
from search import find_doclist_of_prefix, find_doclist_of_word, find_doclist_by_query


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/process.log"),
        logging.StreamHandler()
    ],
    encoding="utf-8"
)

# Creating the backend functions for python file explorer project
def open_file():
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])
    os.startfile(os.path.abspath(file))
def open_folder():
    folder = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder)
def list_files_in_folder():
    i = 0
    folder = fd.askdirectory(title='Select the folder whose files you want to list')
    files = os.listdir(os.path.abspath(folder))
    list_files_wn = Toplevel(root)
    list_files_wn.title(f'Files in {folder}')
    list_files_wn.geometry('250x250')
    list_files_wn.resizable(0, 0)
    listbox = Listbox(list_files_wn)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)
    while i < len(files):
        listbox.insert(END, files[i])
        i += 1

if __name__ == "__main__":
    # Initializing the window
    root = Tk()
    root.title("Scour")
    root.geometry('600x400')
    root.resizable(0, 0)
    root.config()
    # Creating and placing the components in the window
    Label(root, text="Scour", font=("Calibri", 20), wraplength=250).place(x=20, y=0)
    Button(root, text='Open a file', width=20, command=open_file).place(x=30, y=30)
    Canvas(root, width=20).place(x=100, y=0)
    Button(root, text='Open a folder', width=20, command=open_folder).place(x=30, y=60)
    Button(root, text='List all files in a folder', width=20,
        command=list_files_in_folder).place(x=30, y=330)
    # Finalizing the window
    root.update()
    root.mainloop()