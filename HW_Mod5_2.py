import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа, що знаходяться у тексті.
    Args:
        text (str): Вхідний рядок, який містить числа.
    Yields:
        float: Наступне дійсне число, знайдене у тексті.
    """
    # регулярний вираз для чисел з обох боків від пробілів
    pattern = r'(?<= )\d+\.\d+(?= )'
    for match in re.finditer(pattern, text):  # додаємо пробіли на початок/кінець
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює суму всіх дійсних чисел, згенерованих функцією generator_numbers.

    Args:
        text (str): Вхідний рядок з числами.
        func (Callable): Функція-генератор для отримання чисел.

    Returns:
        float: Загальна сума чисел.
    """
    return sum(func(text))


text1 = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, " \
        "доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
total_income = sum_profit(text1, generator_numbers)
print(f"Загальний дохід: {total_income}")
