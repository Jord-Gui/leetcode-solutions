# Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# def rangeSum(acc, node, L, R):
#     if node is None:
#         return acc
#     elif node.val < L or node.val > R:
#         acc = rangeSum(acc, node.left, L, R)
#         acc = rangeSum(acc, node.right, L, R)
#         return acc
#     else:
#         acc = rangeSum(acc, node.left, L, R)
#         acc = rangeSum(acc, node.right, L, R)
#         return acc + node.val

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # return rangeSum(0, root, L, R)
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
