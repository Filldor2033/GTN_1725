"""
Вспомогательные функции для игры "Угадай число".
Содержит утилиты для валидации, генерации чисел и другие вспомогательные функции.
"""

import random
import re

def validate_input(input_str, min_range, max_range):
    """
    Валидация ввода пользователя.
    
    Args:
        input_str (str): Введенная пользователем строка
        min_range (int): Минимальное допустимое значение
        max_range (int): Максимальное допустимое значение
        
    Returns:
        dict: Результат валидации с сообщением и флагом валидности
    """
    # Проверка на пустую строку
    if not input_str.strip():
        return {
            "valid": False,
            "message": "Ошибка: Введите число"
        }
    
    # Проверка на наличие только цифр и опционального знака минус
    if not re.match(r"^-?\d+$", input_str):
        return {
            "valid": False,
            "message": "Ошибка: Введите целое число"
        }
    
    # Преобразование в число
    try:
        number = int(input_str)
    except ValueError:
        return {
            "valid": False,
            "message": "Ошибка: Некорректное число"
        }
    
    # Проверка диапазона
    if number < min_range or number > max_range:
        return {
            "valid": False,
            "message": f"Ошибка: Число должно быть в диапазоне от {min_range} до {max_range}"
        }
    
    return {
        "valid": True,
        "message": "Валидация пройдена успешно"
    }

def get_random_number(min_val, max_val):
    """
    Генерация случайного числа в заданном диапазоне.
    
    Args:
        min_val (int): Минимальное значение
        max_val (int): Максимальное значение
        
    Returns:
        int: Случайное число в диапазоне [min_val, max_val]
    """
    return random.randint(min_val, max_val)

def format_game_statistics(attempts, secret_number, status):
    """
    Форматирование статистики игры для отображения.
    
    Args:
        attempts (int): Количество попыток
        secret_number (int): Загаданное число
        status (str): Статус игры ('win', 'too_low', 'too_high')
        
    Returns:
        str: Отформатированная строка со статистикой
    """
    status_messages = {
        'win': f"Победа! Число {secret_number} угадано за {attempts} попыток",
        'too_low': f"Попытка {attempts}: Слишком маленькое число",
        'too_high': f"Попытка {attempts}: Слишком большое число"
    }
    return status_messages.get(status, "Неизвестный статус игры")

def calculate_score(attempts, max_attempts=10):
    """
    Расчет счета игрока на основе количества попыток.
    
    Args:
        attempts (int): Количество использованных попыток
        max_attempts (int): Максимальное количество попыток для идеального счета
        
    Returns:
        int: Счет игрока (0-100)
    """
    if attempts <= 0:
        return 0
    
    # Формула: чем меньше попыток, тем выше счет
    score = max(0, 100 - (attempts - 1) * (100 / max_attempts))
    return round(score)

def validate_range(min_str, max_str):
    """
    Валидация диапазона чисел.
    
    Args:
        min_str (str): Минимальное значение диапазона
        max_str (str): Максимальное значение диапазона
        
    Returns:
        dict: Результат валидации с сообщением и флагом валидности
    """
    # Проверка на пустые строки
    if not min_str.strip() or not max_str.strip():
        return {
            "valid": False,
            "message": "Ошибка: Оба поля должны быть заполнены"
        }
    
    # Проверка на числа
    try:
        min_val = int(min_str)
        max_val = int(max_str)
    except ValueError:
        return {
            "valid": False,
            "message": "Ошибка: Введите целые числа"
        }
    
    # Проверка корректности диапазона
    if min_val >= max_val:
        return {
            "valid": False,
            "message": "Ошибка: Минимальное значение должно быть меньше максимального"
        }
    
    if max_val - min_val < 10:
        return {
            "valid": False,
            "message": "Ошибка: Диапазон должен быть не менее 10 чисел"
        }
    
    return {
        "valid": True,
        "min": min_val,
        "max": max_val,
        "message": "Диапазон валиден"
    }

# Тестирование вспомогательных функций
if __name__ == "__main__":
    # Тестирование валидации ввода
    test_cases = [
        ("", 1, 100),
        ("abc", 1, 100),
        ("50", 1, 100),
        ("0", 1, 100),
        ("150", 1, 100),
        ("-10", -100, 100)
    ]
    
    print("Тестирование валидации ввода:")
    for test in test_cases:
        result = validate_input(*test)
        print(f"Ввод: {test[0]}, Результат: {result['valid']}, Сообщение: {result['message']}")
    
    # Тестирование генерации чисел
    print("\nТестирование генерации чисел:")
    for _ in range(5):
        num = get_random_number(1, 100)
        print(f"Сгенерированное число: {num}")
    
    # Тестирование расчета счета
    print("\nТестирование расчета счета:")
    for attempts in range(1, 15):
        score = calculate_score(attempts)
        print(f"Попыток: {attempts}, Счет: {score}")
