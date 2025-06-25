class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=Counter(arr)

        l=list(d.values())
        l.sort()
        for i in range(len(l)-1):
            if l[i]==l[i+1]:
                return False
        return True

            