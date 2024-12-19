import logging

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
    abs_path = "D:/test.txt"
    
    a = read_file(abs_path, encoding="utf-8")
    print("Name: ", a["Filename"])
    print("Content: \n", a["Content"])

    stemmed_words = stem(a["Content"])

    pt = PrefixTree()
    for word in stemmed_words:
        pt.insert(word, [a["Filename"]])
    print(pt.find_word("alpha"))

    serialize_trie(pt, "test.pkl")
    npt = deserialize_trie("test.pkl")
    print(npt.find_word("alpha"))