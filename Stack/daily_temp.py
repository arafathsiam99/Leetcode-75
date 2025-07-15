# Brute Force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n  # Initialize result array with zeros

        for i in range(n):
            # Look for the next warmer day
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i  # Distance between days
                    break
                # If no warmer day found, result[i] remains 0
        return res


# Optimum Solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, curr_temp in enumerate(temperatures):
            # Loop through the stack as long as it's not empty and the current temperature
            # is greater than the temperature at the index of the last element in the stack
            while stack and curr_temp > temperatures[stack[-1]]:
                # Pop the index of the temperature that is less than the current temperature
                prev_index = stack.pop()
                # Calculate the number of days between the previous and current temperature
                # and update the answer list
                res[prev_index] = index - prev_index
            # Append the current index to the stack
            stack.append(index)
        return res
