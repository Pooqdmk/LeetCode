class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
                
            cur = cur.children[i]
        cur.endNode = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur.children:               
                return False
            else:
                cur = cur.children[i]
        return cur.endNode
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            else:
                cur = cur.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)