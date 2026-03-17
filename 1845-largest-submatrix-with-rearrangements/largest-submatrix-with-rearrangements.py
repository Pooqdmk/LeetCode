class Solution:
    def largestSubmatrix(self, mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        res = 0
        prev = [0]*m
        for i in range(n):
            heights = mat[i][::]
            for j in range(m):
                if heights[j] > 0:
                    heights[j] += prev[j]
            sorted_heights = sorted(heights, reverse = True)
            for k in range(m):
                res = max(res, (k+1)*sorted_heights[k])
            prev = heights
        return res
        