class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            dest = True
            for j in range(len(paths)):

                if paths[i][1] == paths[j][0]:
                    dest = False
            if dest:
                return paths[i][1]