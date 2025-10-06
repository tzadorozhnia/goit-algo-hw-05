from typing import Callable

def caching_fibonacci()-> Callable[[int], int]:
    """
    Повертає внутрішню функцію fibonacci(n), яка обчислює n-те число Фібоначчі
    з використанням кешування результатів.

    Returns:
        Callable[[int], int]: функція fibonacci(n), яка приймає ціле число n
        і повертає n-те число Фібоначчі.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0

        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610