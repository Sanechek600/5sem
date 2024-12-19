import logging
import os.path

from rw_processes import read_file, serialize_trie, deserialize_trie
from text_processes import stem
from trie import PrefixTree


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
    
    pt = PrefixTree

    for i in range(1, 5):
        path = os.path.join(dir_path, f"test{i}.txt")
        with open(path, 'r') as f:
            dict_of_file = read_file(path, encoding="utf-8")
            stemmed_words = stem(dict_of_file["Content"]).append(dict_of_file["Filename"])
            for word in stemmed_words:
                pt.insert(word, os.path.basename(path))