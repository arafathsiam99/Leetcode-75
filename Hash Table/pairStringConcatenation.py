from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        num_counter = Counter(nums)

        pair_count = 0

        for i in range(1, len(target)):
            prefix, suffix = target[:i], target[i:]

            if prefix != suffix:
                pair_count += num_counter[prefix] * num_counter[suffix]

            else:
                pair_count += num_counter[prefix] * (num_counter[prefix - 1])

        return pair_count
