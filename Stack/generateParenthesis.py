class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < n
        # valid if  open == closed == n
        stack = []
        res = []

        def backtracking(open_count, closed_count):
            # in that case we've finished, and basically our stack will contain the proper parenthesis
            if open_count == closed_count == n:
                # every character in the stack and join them together into an empty string,
                # once they have been joined together they will form a complete string and then will append to our result list
                res.append("".join(stack))
                return

            # if we want to add a open parenthesis we've to check our open parenthesis is less than n, if that's true we can do
            if open_count < n:
                stack.append("(")  # in our stack we append an open parenthesis

                # then we can recursively continue our backtracking ,
                # if we have to do that we have to increment our open count and closed count remain as it is
                backtracking(open_count + 1, closed_count)
                # after backtracking reterns we have to clear our stack by popping to update
                stack.pop()

            if closed_count < open_count:
                stack.append(")")
                backtracking(open_count, closed_count + 1)
                stack.pop()

        # call our backtrack function and pass (0,0) as initial and closed count  bcz our stack is initially empty
        backtracking(0, 0)
        return res
