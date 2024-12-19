import os
import logging
from typing import Dict


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