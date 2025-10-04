class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = {c : i for i,c in enumerate(nums)}

        return d[target] if target in d else -1