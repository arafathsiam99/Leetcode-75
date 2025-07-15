class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stack = []
        for num in nums2:
            # If the current number is greater than the last number in the stack,
            # It is the next greater element for that number in the stack.
            # Pop elements from the stack and update the mapping accordingly
            while stack and stack[-1] < num:
                idx = stack.pop()
                nge[idx] = num
            # Push the current number onto the stack
            stack.append(num)
        # Go through each number in the first list and get the next greater element from the mapping
        # If a number does not have a next greater element in the second list,
        # the get method returns -1
        return [nge.get(num, -1) for num in nums1]
