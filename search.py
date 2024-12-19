from typing import List
import logging

from trie import PrefixTree


def find_term_doclist(pt: PrefixTree, term: str) -> List[str]:
    doclist = pt.find_word(term).doclist
    logging.debug(f"Found doclist for {term}: {doclist}")
    return doclist