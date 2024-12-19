import re
import logging

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


nltk.download("punkt_tab")

def cyrillic_check(text: str) -> bool:
    """Helper function that checks if there are cyrillic characters in the text
    Args:
        text: a str of text to be checked
    Returns:
        True if there are cyrillic characters, False otherwize
    """
    return bool(re.search(r"[а-яА-Я]", text))

def latin_check(text: str) -> bool:
    """Helper function that checks if there are latin characters in the text
    Args:
        text: a str of text to be checked
    Returns:
        True if there are latin characters, False otherwize
    """
    return bool(re.search(r"[a-zA-Z]", text))

def stem(text: str) -> list[str]:
    """Stems the words in the text leaving basic forms
    If given cyrrilic text, views as russian
    If given latin text, views as english
    Can stem russian and english in one text

    Args:
        text (str): a str of text to be stemmed
    Returns:
        list[str]: a list of strs containing stemmed words
    """
    out_c, out_l = [], []

    if cyrillic_check(text):
        stemmer = SnowballStemmer("russian")
        tokens = word_tokenize(text)
        stemmed_words_c = [stemmer.stem(word) for word in tokens]

        for word in stemmed_words_c:
            if cyrillic_check(word):
                out_c.append(word)
        logging.debug(f"Russian stemmed words: {out_c}")

    if latin_check(text):
        stemmer = SnowballStemmer("english")
        tokens = word_tokenize(text)
        stemmed_words_l = [stemmer.stem(word) for word in tokens]

        for word in stemmed_words_l:
            if latin_check(word):
                out_l.append(word)
        logging.debug(f"English stemmed words: {out_l}")

    return out_c + out_l