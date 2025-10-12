class MagicDictionary:

    def __init__(self):
        self.d = defaultdict(list)
        

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.d[len(i)].append(i)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        word = list(searchWord)
        if n in self.d:
            l=self.d[n]
            
            for i in l:
                m = list(i)
                if sum(1 for j,k in zip(word,m) if j == k ) == n-1:
                    
                    return True
            
        return False
                



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)