class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        dp = [[-1 for j in range(3)]for i in range(3)]

        for i,c in enumerate(moves):
            if i%2 == 0:
                dp[c[0]][c[1]] = 0
            else:
                dp[c[0]][c[1]] = 10
        
        for i in range(3):
            if sum(dp[i]) == 0:
                return 'A'
            elif sum(dp[i]) == 30:
                return 'B'
            s = 0
            for j in range(3):
                
                s+=dp[j][i]
            if s == 0 :
                return 'A'
            elif s == 30:
                return 'B'
        d1,d2 = 0,0
        for i in range(3):
            d1+=dp[i][i]
            d2+=dp[i][3-i-1]
        if d1 == 0 or d2 == 0:
            return 'A'
        elif d2 == 30 or d1 == 30:
            return 'B'
                    
        if any(-1 in r for r in dp):
            return 'Pending'
        return 'Draw'
