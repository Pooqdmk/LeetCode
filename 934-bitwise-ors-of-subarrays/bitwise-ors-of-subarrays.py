class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n=len(arr)
        curr=set()
        res=set()
        for i in arr:
            new_curr={i}
            for j in curr:
                new_curr.add(j | i)
            
            curr=new_curr
            res.update(curr)
        return len(res)