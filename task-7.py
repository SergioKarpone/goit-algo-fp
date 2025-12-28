import random
import matplotlib.pyplot as plt


# Симуляція кидків двох кубиків задану кількість разів
def simulate_dice_rolls(num_simulations):
    
    # Ініціалізація лічильника сум (від 2 до 12)
    counts = {sum_val: 0 for sum_val in range(2, 13)}

    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        counts[roll_sum] += 1

    return counts


# Таблиця ймовірностей та порівняння з теоретичним значенням
def print_probabilities(counts, num_simulations):

    # Теоретичні ймовірності
    theoretical_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    # Заголовки таблиці
    print(f"{'Сума':^5} | {'Імовірність (теор)':^20} | {'Імовірність (MC)':^20} | {'Різниця':^15}")
    print("-" * 70)

    mc_probs = {}
    
    for sum_val in range(2, 13):
        count = counts[sum_val]
        mc_prob = (count / num_simulations) * 100
        mc_probs[sum_val] = mc_prob
        
        theory_prob = theoretical_probs[sum_val]
        diff = theory_prob - mc_prob
        
        # Форматування результатів
        mc_str = f"{mc_prob:.2f} %"
        theory_str = f"{theory_prob:.2f} %"
        diff_str = f"{diff:.2f} п.п."
        
        # Построчне виведення результатів
        print(f"{sum_val:^5} | {theory_str:^20} | {mc_str:^20} | {diff_str:^15}")

    return mc_probs, theoretical_probs


if __name__ == "__main__":
    
    # Кількість кидків
    NUM_SIMULATIONS = 1000000  

    print(f"\nСимуляція за методом Монте-Карло для {NUM_SIMULATIONS} кидків:\n")
    
    # Симуляція
    results = simulate_dice_rolls(NUM_SIMULATIONS)
    
    # Результати
    mc_percentages, theory_percentages = print_probabilities(results, NUM_SIMULATIONS)
