class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        e=[]
        for i in nums:
            if i%2==0:
                e.append(i)
        d=Counter(e)
        l=sorted(d.items(),key=lambda x:(-x[1],x[0]))
        return l[0][0] if l else -1