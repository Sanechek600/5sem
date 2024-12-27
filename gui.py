import os

from tkinter import *
import tkinter.filedialog as fd
from tkinter.ttk import Combobox

import rw_processes as rw
from search import find_doclist_by_query


def execute():
    root = Tk()
    root.title("Scour")
    root.geometry("400x600")
    
    def selected(event):
        # получаем выделенный элемент
        selection = search_mode.get()
        print(selection)
        label_t['text'] = f"Search mode {search_mode.get()}"
    
    def submit_path():
        label_t["text"] = f"Saving {path_string.get()}"
        pt = rw.scour_directory(path_string.get())
        rw.serialize_trie(pt, os.path.join(path_string.get(), "trie.pkl"))

    def load_path():
        label_t["text"] = f"Loading {path_string.get()}"
        if os.path.exists(os.path.join(path_string.get(), "trie.pkl")):
            label_t["text"] = f"Index found for {path_string.get()}"
        else:
            label_t["text"] = f"No index for {path_string.get()}"
        
    def run_query():
        pt = rw.deserialize_trie(os.path.join(path_string.get(), "trie.pkl"))
        mode = search_mode.get()
        if search_mode.get() == "":
            label_t["text"] = "Choose search paradigm"
        try:
            search_res = find_doclist_by_query(
                pt, query_string.get(), 
                search_mode.get()
                )
            res.set(search_res)
        except:
            res.set(["Invalid request"])

    search_modes = ["AND", "OR"]
    
    label = Label(text="Scour")
    label.pack(anchor=NW, fill=None, padx=5, pady=5)
    
    label_t = Label(root, text="Choose directory")
    label_t.pack(anchor=NW, fill=None, padx=5, pady=5)
    
    path_string = StringVar()
    path = Entry(root, textvariable=path_string)
    path.pack(anchor=NW, fill=X, padx=5, pady=5)
    
    submit_button = Button(root, text="Index and save")
    submit_button.pack(anchor=NE, fill=X, padx=5, pady=5)
    submit_button["command"] = submit_path

    load_button = Button(root, text="Load index")
    load_button.pack(anchor=NE, fill=X, padx=5, pady=5)
    load_button["command"] = load_path
    
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
    
    res = Variable(value = [])
    search_result = Listbox(root, listvariable=res)
    search_result.pack(anchor=NW, fill=BOTH, padx=5, pady=5)
    
    root.mainloop()