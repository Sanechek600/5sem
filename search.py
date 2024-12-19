from typing import List
import logging

from trie import PrefixTree
from text_processes import stem


def find_doclist_of_word(pt: PrefixTree, word: str) -> List[str]:
    term = stem(word)[0]
    doclist = pt.find_word(term).doclist
    logging.debug(f"Found doclist for {term}: {doclist}")
    return doclist

def find_doclist_of_term(pt: PrefixTree, term: str) -> List[str]:
    doclist = pt.find_word(term).doclist
    logging.debug(f"Found doclist for {term}: {doclist}")
    return doclist