import os
import logging
import pickle
from typing import Dict

from trie import PrefixTree


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
        with open(file_path, "r", encoding=encoding) as file:
            out["Filename"] = os.path.basename(file_path)
            out["Content"] = str(file.read())
    except Exception as e: 
        logging.error(f"Error in read_file: {e}")
    return out

def serialize_trie(trie: PrefixTree, file_path: str) -> None:
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(trie, file)
            logging.debug(f"Trie serialized into {file_path}")
    except Exception as e: 
        logging.error(f"Error in serialize_trie: {e}")

def deserialize_trie(file_path: str) -> PrefixTree:
    try:
        with open(file_path, 'rb') as file:
            pt = pickle.load(file)
            logging.debug(f"Trie deserialized from {file_path}")
            return pt
    except Exception as e: 
        logging.error(f"Error in deserialize_trie: {e}")