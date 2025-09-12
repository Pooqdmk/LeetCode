class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        return False if len(set(s).intersection({'a','e','i','o','u'})) == 0 else True