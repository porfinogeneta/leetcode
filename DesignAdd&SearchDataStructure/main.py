"""
    idea: Robimy Trie, z tą różnicą że w wyszukiwaniu jak pojawi się .,
    to dfsowo schodzimy do wszystkich możliwych dzieci i bierzemy or'a
    z tych wywołań rekurencyjnych
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        idea: standardowo jak w Trie
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        idea: jak przechodzimy standardowo, jak natrafimy na .,
        to puszczamy rekurencyjnie na wszystkich dzieciach,
        przerabiamy standardowe przechodzenie po Trie, dodając ten etap
        dfs
        """

        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_word_end

        return dfs(0, self.root)




