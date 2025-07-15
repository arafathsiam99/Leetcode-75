def calculate_stock_span(prices):

    # Calculate stock span for each day using stack-based approach.

    # Stock span for a day is the maximum number of consecutive days
    # (including current day) before current day where price <= current price.

    # Args:
    #     prices: List of stock prices

    # Returns:
    #     List of spans for each day

    n = len(prices)
    spans = [0] * n  # Initialize spans array
    stack = []  # Stack to store indices

    for i in range(n):
        # Remove elements from stack while stack is not empty
        # and price[stack.top()] <= price[i]
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        # If stack becomes empty, span = i + 1 (all previous days)
        # Otherwise, span = i - stack.top() or prev Highvalue
        if not stack:
            spans[i] = i + 1
        else:
            spans[i] = i - stack[-1]
        # Push current index to stack
        stack.append(i)
    return spans


# Input and solve
n = int(input())
prices = list(map(int, input().split()))

# Calculate and output spans
spans = calculate_stock_span(prices)
print(" ".join(map(str, spans)))
