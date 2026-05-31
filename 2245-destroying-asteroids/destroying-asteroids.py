class Solution:
    def asteroidsDestroyed(self, mass: int, a: List[int]) -> bool:
        a.sort()
        for i in a:
            if i <= mass:
                mass+=i
            else:
                if mass >= a[-1]:
                    return True
                else:
                    return False
        return True