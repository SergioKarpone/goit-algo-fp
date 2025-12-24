import heapq


# Пошук найкоротшої відстані
def dijkstra(graph, start):
    
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Словник для збереження попередньої вершини
    previous_nodes = {vertex: None for vertex in graph}
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Запам'ятовуємо, звідки прийшли
                previous_nodes[neighbor] = current_vertex  
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, previous_nodes


# Відновлення шляху від start до target (словник попередників)
def get_path(previous_nodes, start, target):
    
    path = []
    current = target
    
    # Якщо цільова вершина недосяжна
    if previous_nodes[current] is None and current != start:
        return None
        
    while current is not None:
        path.append(current)
        if current == start:
            break
        current = previous_nodes[current]
        
    return path[::-1]  # Розвертаємо список (від початку до кінця)


# Граф: т.A - стартова, т.J - найвіддаленіша.
graph = {
    'A': {'B': 5, 'C': 10, 'E': 12},
    'B': {'A': 5, 'D': 3, 'E': 8},
    'C': {'A': 10, 'E': 2, 'F': 15},
    'D': {'B': 3, 'G': 6},
    'E': {'A': 12, 'B': 8, 'C': 2, 'G': 1, 'H': 4},
    'F': {'C': 15, 'H': 5},
    'G': {'D': 6, 'E': 1, 'I': 5},
    'H': {'E': 4, 'F': 5, 'I': 2, 'J': 8},
    'I': {'G': 5, 'H': 2, 'J': 3},
    'J': {'H': 8, 'I': 3}
}


# Тест
start_node = 'A'
dists, prevs = dijkstra(graph, start_node)

print(f"Результати для стартової вершини '{start_node}':\n")
print(f"{'Вершина':<10} | {'Відстань':<10} | {'Маршрут'}")
print("-" * 40)

for vertex in sorted(graph.keys()):
    if vertex == start_node:
        continue
        
    distance = dists[vertex]
    path_list = get_path(prevs, start_node, vertex)
    path_str = " -> ".join(path_list) if path_list else "Недосяжна"
    
    print(f"{vertex:<10} | {distance:<10} | {path_str}")

# Найдальша точка
target = 'J'
print(f"\nДетальний аналіз шляху до {target}:")
path_to_J = get_path(prevs, start_node, target)
print(f"Шлях: {' -> '.join(path_to_J)}")
print(f"Вартість: {dists[target]}")
