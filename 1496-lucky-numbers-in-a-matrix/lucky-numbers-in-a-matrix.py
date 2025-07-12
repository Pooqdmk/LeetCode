class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        for j in range(len(matrix[0])):
            mx=-1
            row=-1
            for i in range(len(matrix)):
                c=mx
                mx=max(mx,matrix[i][j])
                if c!=mx:
                    row=i
            if min(matrix[row]) == mx:
                res.append(mx)
      
        return res