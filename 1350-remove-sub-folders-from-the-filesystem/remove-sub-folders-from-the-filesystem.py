class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        stack=[]

        for i in folder:
            if stack and i.startswith(stack[-1]) and i[len(stack[-1])] == '/':
                continue
            else:
                stack.append(i)
        return stack
