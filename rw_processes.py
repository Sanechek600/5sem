import os
import logging
import pickle
from typing import Dict
from pathlib import Path
import docx

from trie import PrefixTree
from text_processes import stem


def read_file(file_path: str, encoding: str) -> Dict[str, str]:
    """Reads the needed .txt file, returns its name and contents
    Args:
        file_path (str): path to the neede file
        encoding (str): encoding to open the file with
    Returns:
        Dict[str]: Dictionary with keys "Filename" and "Content"
    """
    out = {"Filename": "", "Content": ""}
    try:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding=encoding) as file:
                out["Filename"] = Path(os.path.basename(file_path)).stem
                out["Content"] = str(file.read())
        elif file_path.endswith(".docx"):
            out["Filename"] = Path(os.path.basename(file_path)).stem
            text = ""
            doc = docx.Document(file_path)
            for paragrapth in doc.paragraphs:
                text = text + paragrapth.text + "\n"
            out["Content"] = text

            logging.debug(f"Read from {file_path}")
    except Exception as e: 
        logging.error(f"Error in read_file: {e}")
    return out

def read_file_to_trie(pt: PrefixTree, file_path: str) -> None:
    """Reads the needed .txt file, returns PrefixTree made from it
    Args:
        file_path (str): path to the neede file
        encoding (str): encoding to open the file with
    Returns:
        Dict[str]: Dictionary with keys "Filename" and "Content"
    """
    with open(file_path, 'r') as f:
        dict_of_file = read_file(file_path, encoding="utf-8")

    stemmed_words = stem(dict_of_file["Content"])

    for word in stemmed_words:
        pt.insert(word=word, doclist=[os.path.abspath(file_path)])
    pt.insert(word=dict_of_file["Filename"], doclist=[os.path.abspath(file_path)])

def scour_directory(dir_path: str) -> PrefixTree:
    files = []
    for file in os.listdir(dir_path):
        if file.endswith(".txt") or file.endswith(".docx"):
            files.append(os.path.join(dir_path, file))

    pt = PrefixTree()

    for file in files:
        read_file_to_trie(pt, file)
    
    return pt

def serialize_trie(trie: PrefixTree, file_path: str) -> None:
    """
    Serialize the prefix tree to a file.
    Args:
        trie (PrefixTree): The prefix tree to serialize.
        file_path (str): The path to the file where the tree will be saved.
    Errors:
        IOError: If an error occurs while writing to the file.
        pickle.PickleError: If an error occurs during serialization.
    """
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(trie, file)
            logging.info(f"Trie serialized into {file_path}")
    except (IOError, pickle.PickleError) as e: 
        logging.error(f"Error in serialize_trie: {e}")

def deserialize_trie(file_path: str) -> PrefixTree:
    """
    Deserialize the prefix tree from a file.
    Args:
        file_path (str): The path to the file from which the tree will be loaded.
    Returns: 
        PrefixTree: The deserialized prefix tree.
    Errors:
        IOError: If an error occurs while reading the file.
        pickle.UnpicklingError: If an error occurs during deserialization.
    """
    try:
        with open(file_path, 'rb') as file:
            pt = pickle.load(file)
            logging.info(f"Trie deserialized from {file_path}")
            return pt
    except (IOError, pickle.UnpicklingError) as e: 
        logging.error(f"Error in deserialize_trie: {e}")
        return None
