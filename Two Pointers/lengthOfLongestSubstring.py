# Brute Force Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()  # Creating a hashset
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res


# Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a set to store unique characters of the substring
        charSet = set()
        l = 0
        res = 0

        # Iterate over the string using the right_pointer
        for r in range(len(s)):
            # if the current char is already in the set,
            # remove characters from the left until the current char
            # is no longer in the set to assure all unique substring
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1  # Shrink the window from the left side
            # Add the current char to the set as it's unique in current window
            charSet.add(s[r])
            # Update the max_length if the current window size is greater
            res = max(res, r - l + 1)  # r-l+1 = current length
        return res
