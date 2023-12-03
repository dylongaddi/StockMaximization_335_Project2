def stock_maximization_dp(n, stocks_and_values, amount):
    n = len(stocks_and_values)
    # Create a table where dp[i][j] will represent the maximum stocks that can be purchased
    # with i companies and j amount of money
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    # Build the table in bottom-up fashion
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            stocks, cost = stocks_and_values[i-1]
            if cost <= j:
                # If the cost of the current company's stock is less than the current amount,
                # then take the maximum of not taking this company's stock (dp[i-1][j]) or
                # taking it (stocks + dp[i-1][j-cost])
                dp[i][j] = max(dp[i-1][j], stocks + dp[i-1][j-cost])
            else:
                # If the cost of the current company's stock is more than the current amount,
                # then we can't buy stocks from this company, so just carry forward the value
                dp[i][j] = dp[i-1][j]

    # The last cell of the table will have the answer for the whole problem
    return dp[n][amount]

with open("input.txt") as input, open("output.txt", "a") as output:
    lines = input.readlines()


    for i in range(0, len(lines), 4):
        n = int(lines[i].strip())
        stocks_and_values = eval(lines[i + 1].strip())
        amount = int(lines[i + 2].strip())

        result = stock_maximization_dp(n, stocks_and_values, amount)
        output.write(f"Max Stocks (DP): {result}\n" )