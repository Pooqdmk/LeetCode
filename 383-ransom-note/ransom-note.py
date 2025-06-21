class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=Counter(ransomNote)
        l=Counter(magazine)

        for key,val in d.items():
            if l[key] <val:
                return False
            #     if val>l[key]:
            #         return False
            # else:
            #     return False
        return True
                    


