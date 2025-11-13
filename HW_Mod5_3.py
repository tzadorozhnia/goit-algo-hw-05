import sys
import os

def parse_log_line(line: str) -> dict:
    """
    Парсить один рядок логу у словник з ключами:
    date, time, level, message
    """
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        raise ValueError(f"Неправильний формат логу: {line}")
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> list:
    """
    Завантажує логи з файлу і повертає список словників
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():  # ігноруємо порожні рядки
                    try:
                        logs.append(parse_log_line(line))
                    except ValueError as e:
                        print(f"Пропущено рядок: {e}")
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує список логів за рівнем
    """
    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Рахує кількість логів для кожного рівня
    """
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    """
    Виводить таблицю з кількістю записів за рівнями
    """
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    # підрахунок статистики
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # якщо вказаний рівень логування
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, level)
        if filtered:
            print(f"\nДеталі логів для рівня '{level}':")
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписів для рівня '{level}' не знайдено.")


if __name__ == "__main__":
    main()