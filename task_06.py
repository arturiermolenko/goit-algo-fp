items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(item)
            total_cost += data["cost"]
            total_calories += data["calories"]
        if total_cost >= budget:
            break

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_name, data = item_list[i - 1]
            if data["cost"] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - data["cost"]] + data["calories"]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    selected_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, data = item_list[i - 1]
            selected_items.append(item_name)
            total_cost += data["cost"]
            w -= data["cost"]

    return selected_items, total_cost, total_calories


if __name__ == "__main__":
    budget = 150

    print("Greedy Algorithm:")
    selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
    print(f"Selected items: {selected_items}")
    print(f"Total cost: {total_cost}")
    print(f"Total calories: {total_calories}")

    print("\nDynamic Programming Algorithm:")
    selected_items, total_cost, total_calories = dynamic_programming(items, budget)
    print(f"Selected items: {selected_items}")
    print(f"Total cost: {total_cost}")
    print(f"Total calories: {total_calories}")
