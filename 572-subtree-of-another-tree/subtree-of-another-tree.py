# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def match(a,b):
            if not a and not b:
                return True
            elif (not a and b) or (not b and a):
                return False
            
            if a.val != b.val:
                return False
            return match(a.left,b.left) and match(a.right,b.right)
                
            
        
        def dfs(a):
            if not a:
                return False
            
            if match(a,subRoot):
                return True
            return dfs(a.left) or dfs(a.right)
        
        return dfs(root)


