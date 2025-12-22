class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Реверс-сортування
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування однозв'язного списку
    def merge_sort(self):
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
        # Базовий випадок (пусто або 1 елемент)
        if head is None or head.next is None:
            return head

        # Пошук середини списку
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        # Рекурсивне сортування лівої та правої частин
        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)

        # Злиття обох відсортованих частин
        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Допоміжний метод злиття
    def _sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

# Об'єднання двох відсортованих списків
def merge_two_sorted_lists(list1: LinkedList, list2: LinkedList):
    merged_list = LinkedList()
    
    # Створення вузлу для початку нового списку
    dummy = Node(0)
    tail = dummy
    
    lst1 = list1.head
    lst2 = list2.head

    while lst1 and lst2:
        if lst1.data <= lst2.data:
            tail.next = lst1    
            lst1 = lst1.next
        else:
            tail.next = lst2
            lst2 = lst2.next
        tail = tail.next

    # Додавання залишків
    if lst1:
        tail.next = lst1
    elif lst2:
        tail.next = lst2

    merged_list.head = dummy.next
    return merged_list


# Запуск
if __name__ == "__main__":
    
    # ТЕСТ
    print("\nРЕВЕРСУВАННЯ")
    llist = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        llist.insert_at_end(i)
    
    print("Початковий список:")
    llist.print_list()
    
    llist.reverse_list()
    print("Реверсований список:")
    llist.print_list()

    print("\nСОРТУВАННЯ (Merge Sort)")
    llist_unsorted = LinkedList()
    for i in [3, 1, 4, 2, 5]:
        llist_unsorted.insert_at_end(i)
    
    print("Невідсортований список:")
    llist_unsorted.print_list()
    
    llist_unsorted.merge_sort()
    print("Відсортований список:")
    llist_unsorted.print_list()

    print("\nОБ'ЄДНАННЯ")
    l1 = LinkedList()
    l1.insert_at_end(1)
    l1.insert_at_end(3)
    l1.insert_at_end(5)
    
    l2 = LinkedList()
    l2.insert_at_end(2)
    l2.insert_at_end(4)
    l2.insert_at_end(6)

    print("Список 1:")
    l1.print_list()
    print("Список 2:")
    l2.print_list()

    merged_ll = merge_two_sorted_lists(l1, l2)
    print("Об'єднаний відсортований список:")
    merged_ll.print_list()
