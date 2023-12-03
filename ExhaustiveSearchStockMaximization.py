def stock_maximization_exhaustive(n, stocks_and_values, amount):
    best_combination = None

    # Function to calculate the total number of stocks in a combination
    def total_value(combination):
        total = 0
        for i in combination:
            total += stocks_and_values[i][0]
        return total

    # Function to verify if a combination is valid based on the total cost
    def verify_combination(combination):
        total_cost = 0
        for i in combination:
            total_cost += stocks_and_values[i][1]
        return total_cost <= amount

    # Recursive function to generate all possible combinations
    def generate_combinations(index, current_combination):
        nonlocal best_combination

        if index == n:
            if verify_combination(current_combination):
                if not best_combination or total_value(current_combination) > total_value(best_combination):
                    best_combination = current_combination
            return

        generate_combinations(index + 1, current_combination)  # Exclude current stock
        generate_combinations(index + 1, current_combination + [index])  # Include current stock

    generate_combinations(0, [])

    # Check if there is a best combination and return its total value, otherwise return 0
    if best_combination:
        return total_value(best_combination)
    else:
        return 0


with open("input.txt") as input, open("output.txt", "w") as output:
    lines = input.readlines()


    for i in range(0, len(lines), 4):
        n = int(lines[i].strip())
        stocks_and_values = eval(lines[i + 1].strip())
        amount = int(lines[i + 2].strip())

        result = stock_maximization_exhaustive(n, stocks_and_values, amount)
        output.write(f"Max Stocks (Exhaustive Search): {result}\n" )





