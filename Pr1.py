class Stack:
    def __init__(self):
        """Ініціалізація порожнього стека."""
        self._items = []  # Використовуємо список для зберігання елементів

    def push(self, item):
        """Додає елемент у верхню частину стека."""
        self._items.append(item)

    def pop(self):
        """Видаляє та повертає верхній елемент стека.
        Викликає помилку, якщо стек порожній.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Повертає верхній елемент стека без видалення.
        Викликає помилку, якщо стек порожній.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Перевіряє, чи стек порожній."""
        return len(self._items) == 0

    def size(self):
        """Повертає кількість елементів у стеку."""
        return len(self._items)

# Приклад використання
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Виведе: 3
print(stack.peek())  # Виведе: 2
print(stack.size())  # Виведе: 2
