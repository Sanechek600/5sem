from typing import List

from utility import extend_unique


class TrieNode:
    def __init__(self, term=''):
        self.term = term
        self.doclist = list()
        self.children = dict()
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str, doclist: List[str] = list()) -> None:
        """Inserts a word into the trie, adding nodes for each character
        If given doclist, each new node will have that doclist
        """
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current.children[char].doclist = extend_unique(
                current.children[char].doclist,
                doclist
            )
            current = current.children[char]
        current.is_word = True

    def find_word(self, word: str):
        """
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        if current.is_word:
            return current
        
    def __child_words_for(self, node, words: list[str]) -> None:
        """
        Private helper function. Cycles through all children
        of node recursively, adding them to words if they
        constitute whole words (as opposed to merely prefixes).
        """
        if node.is_word:
            words.append(node.term)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)
        
    def starts_with(self, prefix: str):
        """
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        """
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                return list()
            current = current.children[char]

        self.__child_words_for(current, words)
        return words

if __name__ == "__main__":
    pt = PrefixTree()
    pt.insert("aaa")
    pt.insert("aba")
    pt.insert("abb", doclist=['afile', 'pdfile'])
    pt.insert("abb", doclist=['bfile'])
    pt.insert("abb", doclist=['bfile'])
    print(pt.find_word("abb").doclist)
    print(pt.starts_with("ab"))