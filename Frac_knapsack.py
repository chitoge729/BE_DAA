def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)  # Sort items by value-to-weight ratio (decreasing order)
    knapsack = []
    total_value = 0

    for item in items:
        if capacity <= 0:
            break

        weight, value = item
        fraction = min(weight, capacity)
        total_value += fraction * (value / weight)
        capacity -= fraction
        knapsack.append((fraction, item))

    return total_value, knapsack

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    capacity = float(input("Enter the capacity of the knapsack: "))

    items = []
    for i in range(n):
        weight, value = map(float, input(f"Enter weight and value for item {i + 1} (e.g., 5 10): ").split())
        items.append((weight, value))

    total_value, selected_items = fractional_knapsack(items, capacity)

    print(f"Maximum value in the knapsack: {total_value:.2f}")
    print("Selected items:")
    for fraction, (weight, value) in selected_items:
        print(f"  Weight: {weight:.2f}, Value: {value:.2f}, Fraction: {fraction:.2f}")
