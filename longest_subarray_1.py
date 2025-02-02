from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroes = res = 0

        start = 0

        for end, num in enumerate(nums):
            zeroes += 1 if num == 0 else 0

            while zeroes > 1:
                zeroes -= 1 if nums[start] == 0 else 0

                start += 1
            res = max(res, end - start)

        return res
