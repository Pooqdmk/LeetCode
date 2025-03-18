class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # for i in range(n):
        #     for j in range(n):
        i,j=0,0
        for k in commands:
            if k=='RIGHT':
                j=j+1
            elif k=='LEFT':
                j=j-1
            elif k=='UP':
                i=i-1
                
            else:
                i=i+1
                
                
        return    (i*n)+j
