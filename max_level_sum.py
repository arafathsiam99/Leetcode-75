from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum = -inf
        level = 0
        answer = 0

        while queue:
            level += 1
            current_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                current_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if max_sum < current_sum:
                max_sum = current_sum
                answer = level
        return answer
