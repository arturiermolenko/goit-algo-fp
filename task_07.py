import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_trials):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1

    sum_probabilities = {key: value / num_trials for key, value in sum_counts.items()}
    return sum_probabilities


def analytical_probabilities():
    return {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }


def plot_probabilities(monte_carlo, analytical):
    sums = range(2, 13)

    monte_carlo_probs = [monte_carlo[x] for x in sums]
    analytical_probs = [analytical[x] for x in sums]

    plt.bar(sums, monte_carlo_probs, alpha=0.6, label="Monte Carlo")
    plt.plot(sums, analytical_probs, color="red", marker="o", label="Analytical")

    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.title("Probability Distribution of Dice Sums")
    plt.legend()
    plt.grid(True)
    plt.xticks(sums)
    plt.show()


if __name__ == "__main__":
    num_trials = 1000000
    monte_carlo_probs = monte_carlo_simulation(num_trials)
    analytical_probs = analytical_probabilities()

    print("Monte Carlo Probabilities:")
    for sum_value in range(2, 13):
        print(f"Sum = {sum_value}: {monte_carlo_probs[sum_value]:.4f}")

    print("\nAnalytical Probabilities:")
    for sum_value in range(2, 13):
        print(f"Sum = {sum_value}: {analytical_probs[sum_value]:.4f}")

    plot_probabilities(monte_carlo_probs, analytical_probs)
