def knapsack_0_1(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    capacity = int(input("Enter the capacity of the knapsack: "))

    values = []
    weights = []
    for i in range(n):
        weight, value = map(int, input(f"Enter weight and value for item {i + 1} (e.g., 5 10): ").split())
        weights.append(weight)
        values.append(value)

    max_value, selected_items = knapsack_0_1(values, weights, capacity)

    print(f"Maximum value in the knapsack: {max_value}")
    print("Selected items:")
    for item in selected_items:
        weight, value = weights[item], values[item]
        print(f"  Item {item + 1}: Weight = {weight}, Value = {value}")
