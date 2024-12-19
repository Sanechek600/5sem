import logging
import os.path

import rw_processes as rw
from text_processes import stem
from trie import PrefixTree
from search import find_doclist_of_prefix, find_doclist_of_word, find_doclist_by_query


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs\\process.log"),
        logging.StreamHandler()
    ],
    encoding="utf-8"
)

if __name__ == "__main__":
    dir_path = "D:/Scour_test/"
    
    pt = PrefixTree()

    for i in range(1, 5):
        path = os.path.join(dir_path, f"test{i}.txt")
        rw.read_file_to_trie(pt, path)
    
    find_doclist_by_query(pt, query="альфа дзета", search_type="OR")