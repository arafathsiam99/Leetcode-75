from typing import List
class Solution:
    def increasingTriplet (self,nums:List[int]) -> bool:
        smallest = float('inf')
        middle = float ('inf')
        
        for num in nums:
            if num > middle:
                return True
            if num <= smallest:
                smallest = num
            else:
                middle = num
        return False