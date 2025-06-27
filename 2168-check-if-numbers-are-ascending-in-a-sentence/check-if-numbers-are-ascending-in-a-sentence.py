class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=s.split()
        res=[]
        for i in l:
            if i.isdigit():
                res.append(int(i))
    
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True

