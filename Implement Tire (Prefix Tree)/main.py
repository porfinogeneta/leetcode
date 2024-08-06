class TrieNode:
    def __init__(self):
        self.letters = {}
        self.is_end_of_word = False


class Trie(object):

    def __init__(self):
        # tworzymy pusty węzeł, z którego wszystko wychodzi
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        idea: Przechodzimy litera po literze, jeśli nie ma w danym node
        litery to ją dodajemy , przechodzimy do coraz niższych poziomów
        drzewa
        """
        cur = self.root
        for l in word:
            if l not in cur.letters:
                cur.letters[l] = TrieNode()
            cur = cur.letters[l]
        # jak dojdziemy do końca słowa trzeba ten koniec zaznaczyć
        cur.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        idea: Schodzimy po drzewie, po kolei używając liter ze słowa,
        jak się skończą litery to sprawdzamy czy aktualna litera
        jest końcem słowa, jak którejś litery nie ma to zwracamy False
        """
        cur = self.root
        for l in word:
            if l not in cur.letters:
                return False
            cur = cur.letters[l]
        return cur.is_end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        idea: Tak samo jak wyżej, tylko nie sprawdzamy czy to koniec słowa,
        skoro ma być prefiks
        """
        cur = self.root
        for l in prefix:
            if l not in cur.letters:
                return False
            cur = cur.letters[l]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)