class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # r=l=d=u=0
        # for i in moves:
        #     if i=="R":
        #         r+=1
        #     elif i=="L":
        #         l+=1
        #     elif i=="U":
        #         u+=1
        #     else:
        #         d+=1
        # return (r==l) and (u==d)

        return moves.count("R")==moves.count("L") and moves.count("D")==moves.count("U")