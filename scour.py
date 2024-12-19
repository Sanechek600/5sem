import logging
import os.path

import rw_processes as rw
from text_processes import stem
from trie import PrefixTree
from search import find_doclist_of_term, find_doclist_of_word


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs\\process.log"),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    dir_path = "D:/Scour_test/"
    
    pt = PrefixTree()

    for i in range(1, 5):
        path = os.path.join(dir_path, f"test{i}.txt")
        rw.read_file_to_trie(pt, path)
    
    print(find_doclist_of_word(pt, word="альфа"))