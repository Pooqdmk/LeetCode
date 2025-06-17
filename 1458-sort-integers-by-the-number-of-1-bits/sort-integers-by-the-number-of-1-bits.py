class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # d={}

        # for i in arr:
        #     d[i]=bin(i)[2:].count('1')

        # l=dict(sorted(d.items(),key=lambda item:(item[1],item[0])))
        # return list(l.keys()) 
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
