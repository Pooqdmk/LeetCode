class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s])
        visited = {s}
        res = s
        while queue:
            cur = queue.popleft()

            res = min(cur,res)
            add = list(cur)
            for i in range(1,len(add),2):
                add[i] = str((int(cur[i])+a) %10)
            add = ''.join(add)
            if add not in visited:
                visited.add(add)
                queue.append(add)

            rotate = cur[-b:] + cur[:-b]
            if rotate not in visited:
                visited.add(rotate)
                queue.append(rotate)
        return res


