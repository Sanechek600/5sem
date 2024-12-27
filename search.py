from typing import List
import logging

from trie import PrefixTree
from text_processes import stem
from utility import extend_unique


def find_doclist_of_term(pt: PrefixTree, term: str) -> List[str]:
    """
    Finds the list of documents associated with a given term.

    Args:
        pt (PrefixTree): The prefix tree containing the documents.
        term (str): The term to search for.

    Returns:
        List[str]: A list of document identifiers associated with the term.
    """
    try:
        doclist = pt.find_word(term).doclist
    except Exception as e:
        logging.error(f"Could't find doclist for {term}: {e}")
    logging.debug(f"Found doclist for {term}: {doclist}")
    return doclist


def find_doclist_of_word(pt: PrefixTree, word: str) -> List[str]:
    """
    Finds the list of documents associated with a given word after stemming.

    Args:
        pt (PrefixTree): The prefix tree containing the documents.
        word (str): The word to search for.

    Returns:
        List[str]: A list of document identifiers associated with the stemmed word.
    """
    stemmed_terms = stem(word)
    if not stemmed_terms:
        return []
    term = stemmed_terms[0]
    return find_doclist_of_term(pt, term)


def find_doclist_of_prefix(pt: PrefixTree, prefix: str) -> List[str]:
    """
    Finds the list of documents associated with a given prefix after stemming.

    Args:
        pt (PrefixTree): The prefix tree containing the documents.
        prefix (str): The prefix to search for.

    Returns:
        List[str]: A list of document identifiers associated with terms starting with the prefix.
    """
    stemmed_terms = stem(prefix)
    if not stemmed_terms:
        return []
    term = stemmed_terms[0]
    wordlist = pt.starts_with(term)
    doclist = []
    for term_word in wordlist:
        doclist.extend(find_doclist_of_term(pt, term_word))
    logging.debug(f"Found doclist for prefix {prefix}: {doclist}")
    return doclist


def find_doclist_by_query(pt: PrefixTree, query: str, search_type: str = "AND") -> List[str]:
    """
    Finds the list of documents that match a given query using specified search logic.

    Args:
        pt (PrefixTree): The prefix tree containing the documents.
        query (str): The query string to search for.
        search_type (str): The search logic to apply ("AND" or "OR"). Default is "AND".

    Returns:
        List[str]: A list of document identifiers matching the query.
    """
    if search_type not in ("AND", "OR"):
        return []

    doclist = []
    stemmed_query = stem(query)
    for term in stemmed_query:
        current_doclist = find_doclist_of_term(pt, term)
        if search_type == "OR" or not doclist:
            doclist = extend_unique(doclist, current_doclist)
        else:
            doclist = list(set(doclist).intersection(current_doclist))
    logging.debug(f"Found doclist for query {query}: {doclist}")
    return doclist
