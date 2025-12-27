items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Жадібний алгоритм: вибір за найвище співвідношення калорій до вартості
def greedy_algorithm(items, budget):
    # Список з розрахованим співвідношенням (ratio)
    items_list = []
    for name, data in items.items():
        ratio = data['calories'] / data['cost']
        items_list.append({
            "name": name,
            "cost": data['cost'],
            "calories": data['calories'],
            "ratio": ratio
        })
    
    # Сортування співвідношення (ratio) у спадному порядку
    items_list.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_calories = 0
    total_cost = 0
    chosen_items = []
    
    for item in items_list:
        if total_cost + item['cost'] <= budget:
            chosen_items.append(item['name'])
            total_cost += item['cost']
            total_calories += item['calories']
            
    return {
        "items": chosen_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }


# Динамічне програмування: абсолютний максимум калорій в межах бюджету
def dynamic_programming(items, budget):
    # Перетворення словника у список для індексації
    item_names = list(items.keys())
    n = len(item_names)
    
    # K[i][w] зберігає макс. калорій для i предметів при бюджеті w
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнення таблиці знизу вгору
    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        
        for w in range(budget + 1):
            if cost <= w:
                # Вибір: max(не брати, брати + калорії_від_залишку_бюджету)
                K[i][w] = max(K[i-1][w], K[i-1][w-cost] + calories)
            else:
                # Предмет занадто дорогий для поточного ліміту w
                K[i][w] = K[i-1][w]
    
    # Відновлення набору обраних страв (Backtracking)
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if K[i][w] != K[i-1][w]:
            # Предмет i-1 був включений
            item_name = item_names[i-1]
            chosen_items.append(item_name)
            w -= items[item_name]['cost']
            
    return {
        "items": chosen_items,
        "total_cost": budget - w,
        "total_calories": K[n][budget]
    }


if __name__ == '__main__':
    # Бюджет
    test_budget = 100
    
    # Виклик жадібного алгоритму
    greedy_result = greedy_algorithm(items, test_budget)
    
    # Виклик динамічного програмування
    dp_result = dynamic_programming(items, test_budget)
    
    print(f"Бюджет: {test_budget}\n")
    
    print("Жадібний алгоритм (Greedy)")
    print(f"Обрані страви: {greedy_result['items']}")
    print(f"Калорії: {greedy_result['total_calories']}, Вартість: {greedy_result['total_cost']}")
    
    print("\nДинамічне програмування (DP)")
    print(f"Обрані страви: {dp_result['items']}")
    print(f"Калорії: {dp_result['total_calories']}, Вартість: {dp_result['total_cost']}")

    # Аналіз результатів
    if greedy_result['total_calories'] == dp_result['total_calories']:
        print("\nВисновок: У цьому випадку жадібний алгоритм знайшов оптимальне рішення.")
    else:
        print("\nВисновок: Динамічне програмування знайшло краще рішення.")
    