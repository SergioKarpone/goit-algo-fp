import uuid
import networkx as nx
import matplotlib.pyplot as plt
import collections


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        # Колір вузла, який буде змінений
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Колір, збережений у вузлі
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap_array, index=0):
    if index >= len(heap_array):
        return None
    current_node = Node(heap_array[index])
    current_node.left = build_heap_tree(heap_array, 2 * index + 1)
    current_node.right = build_heap_tree(heap_array, 2 * index + 2)
    return current_node


# Генерація списку з n_steps кольорів від start_hex до end_hex
def generate_color_gradient(n_steps, start_hex="#1296F0", end_hex="#CCEEFF"):
    
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    
    colors = []
    for i in range(n_steps):
        # Інтерполяція складових (R, G, B)
        t = i / (n_steps - 1) if n_steps > 1 else 0
        new_rgb = (
            start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t,
            start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t,
            start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t
        )
        colors.append(rgb_to_hex(new_rgb))
    
    return colors


# Кількість вузлів (і кількість кольорів)
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Обхід в глибину (DFS) з використанням стека
def dfs_visualize(root):
    if not root:
        return

    # Підготовка кольорів
    total_nodes = count_nodes(root)
    colors = generate_color_gradient(total_nodes, start_hex="#003366", end_hex="#99CCFF") # Від темно-синього до світлого

    # Стек для DFS (Last In, First Out)
    stack = [root]
    visited_order = []
    
    step = 0
    while stack:
        node = stack.pop()
        
        # Фарбування вузла
        node.color = colors[step]
        step += 1
        visited_order.append(node.val)

        # Додаємо дітей у стек (правий -> лівий). 
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    print(f"Порядок обходу DFS: {visited_order}")
    draw_tree(root, title="DFS Traversal (Dark -> Light)")


# Візуалізація обходу в ширину (BFS) з використанням черги
def bfs_visualize(root):
    if not root:
        return

    # Підготовка кольорів (інша гамма)
    total_nodes = count_nodes(root)
    colors = generate_color_gradient(total_nodes, start_hex="#4B0082", end_hex="#E6E6FA") # Від індиго до лавандового

    # Черга для BFS (First In, First Out)
    queue = collections.deque([root])
    visited_order = []

    step = 0
    while queue:
        # Виймаємо з початку черги
        node = queue.popleft() 
        
        # Фарбуємо вузол
        node.color = colors[step]
        step += 1
        visited_order.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(f"Порядок обходу BFS: {visited_order}")
    draw_tree(root, title="BFS Traversal (Dark -> Light)")


if __name__ == "__main__":
    # Створення дерева з масиву
    heap_list = [0, 4, 1, 5, 10, 3]
    
    # DFS
    print("DFS Visualization")
    root_dfs = build_heap_tree(heap_list) 
    dfs_visualize(root_dfs)

    # BFS
    print("\nBFS Visualization")
    root_bfs = build_heap_tree(heap_list)
    bfs_visualize(root_bfs)
    