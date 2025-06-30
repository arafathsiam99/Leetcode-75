from itertools import accumulate


class NumArray:
    def __init__(self, nums: List[int]):
        self.cumulative_sum = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]
