class Solution:
    def longestZigZag(self, root) -> int:
        def dfs(node, left_length, right_length):
            if not node:
                return
            nonlocal max_length
            max_length = max(max_length, left_length, right_length)
            dfs(node.left, right_length + 1, 0)
            dfs(node.right, 0, left_length + 1)

        max_length = 0
        dfs(root, 0, 0)
        return max_length
