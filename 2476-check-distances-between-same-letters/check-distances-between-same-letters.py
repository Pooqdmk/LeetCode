class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={chr(i+ord('a')):distance[i] for i in range(26)}
        for i in set(s):
            char_to_find=i
            indices=[index for index,char in enumerate (s) if char==char_to_find]
            if indices[1]-indices[0]-1 != d[i]:
                    return False
        return True
