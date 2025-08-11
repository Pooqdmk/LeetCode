class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        mx=-1
        for i in range(len(colors)):
            for j in range(len(colors)-1,-1,-1):
                if colors[i]!=colors[j]:
                    mx=max(mx,abs(j-i))
                    break

        return mx

