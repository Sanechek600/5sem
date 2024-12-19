from typing import List
import logging

from trie import PrefixTree
from text_processes import stem
from utility import extend_unique


def find_doclist_of_term(pt: PrefixTree, term: str) -> List[str]:
    doclist = pt.find_word(term).doclist
    logging.debug(f"Found doclist for {term}: {doclist}")
    return doclist

def find_doclist_of_word(pt: PrefixTree, word: str) -> List[str]:
    term = stem(word)[0]
    doclist = find_doclist_of_term(pt, term)
    return doclist

def find_doclist_of_prefix(pt: PrefixTree, prefix: str) -> List[str]:
    term = stem(prefix)[0]
    wordlist = pt.starts_with(term)
    doclist = []
    for term_word in wordlist:
        doclist.extend(find_doclist_of_term(pt, term_word))
    logging.debug(f"Found doclist for prefix {prefix}: {doclist}")
    return doclist

def find_doclist_by_query(pt: PrefixTree, query: str, search_type="AND") -> List[str]:
    if search_type not in ("AND", "OR"):
        return []
    
    doclist = []

    stemmed_query = stem(query)
    for term in stemmed_query:
        if search_type == "OR" or not doclist:
            doclist = extend_unique(
                doclist, 
                find_doclist_of_term(pt, term)
            )
        else:
            doclist = list(
                set(doclist).intersection(
                set(find_doclist_of_term(pt, term))
                )
            )
    logging.debug(f"Found doclist for query {query}: {doclist}")
    return doclist