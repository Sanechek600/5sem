import logging
import os
import shutil

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from tkinter.ttk import Combobox

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

if __name__ == "__main__":
    root = Tk()
    root.title("Scour")
    root.geometry("400x600")
    
    pt = PrefixTree()
    
    def selected(event):
        # получаем выделенный элемент
        selection = search_mode.get()
        print(selection)
        label_t['text'] = search_mode.get()
    
    def submit_path():
        label_t["text"] = f"{path_string.get()}"
        pt = rw.scour_directory(path_string.get())
        rw.serialize_trie(pt, os.path.join(path_string.get(), "trie.pkl"))
        
    def run_query():
        pt = rw.deserialize_trie(os.path.join(path_string.get(), "trie.pkl"))
        listbox["listvariable"] = find_doclist_by_query(
            pt, query_string.get(), search_mode.get())
        
    
    search_modes = ["AND", "OR"]
    
    label = Label(text="Scour")
    label.pack(anchor=NW, fill=None, padx=5, pady=5)
    
    label_t = Label(root, text="Choose directory")
    label_t.pack(anchor=NW, fill=None, padx=5, pady=5)
    
    path_string = StringVar()
    path = Entry(root, textvariable=path_string)
    path.pack(anchor=NW, fill=X, padx=5, pady=5)
    
    submit_button = Button(root, text="Submit")
    submit_button.pack(anchor=NE, fill=X, padx=5, pady=5)
    submit_button["command"] = submit_path
    
    query_string = StringVar()
    query = Entry(root, textvariable=query_string)
    query.pack(anchor=NW, fill=X, padx=5, pady=5)
    
    search_mode = StringVar()
    combobox = Combobox(root, values=search_modes, state="readonly", textvariable=search_mode)
    combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
    combobox.bind("<<ComboboxSelected>>", selected)
    
    query_run = Button(root, text="Run query")
    query_run.pack(anchor=NE, fill=X, padx=5, pady=5)
    query_run["command"] = run_query
    
    listbox = Listbox(root)
    listbox.pack(anchor=NW, fill=BOTH, padx=5, pady=5)
    
    root.mainloop()