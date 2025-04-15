class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        li=[]
        d=Counter(digits)
        for i in range(100,999,2):
            c=Counter(str(i))
            if all(d[int(key)]>=val for key,val in c.items()):
                li.append(i)
        return li
