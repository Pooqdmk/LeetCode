class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie
        found = True
        word = word + '.'
        for c in word:
            if c not in d:
                found = False
                break
            d = d[c]
        return found

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        found = True
        for c in prefix:
            if c not in d:
                found = False
                break
            d = d[c]
        return found



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)