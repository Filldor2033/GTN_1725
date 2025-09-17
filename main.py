"""
Основной модуль игры "Угадай число".
Содержит основную логику игры.
"""

import random
from utils import validate_input, get_random_number

class GuessTheNumberGame:
    """Класс, реализующий основную логику игры."""
    
    def __init__(self, min_range=1, max_range=100):
        """Инициализация игры с заданным диапазоном."""
        self.min_range = min_range
        self.max_range = max_range
        self.secret_number = None
        self.attempts = 0
        self.game_over = False
        self.reset_game()
    
    def reset_game(self):
        """Сброс игры для нового раунда."""
        self.secret_number = get_random_number(self.min_range, self.max_range)
        self.attempts = 0
        self.game_over = False
    
    def make_guess(self, guess):
        """
        Обработка попытки угадать число.
        
        Args:
            guess (str или int): Предположение игрока
            
        Returns:
            dict: Результат попытки с подсказкой и статусом
        """
        # Валидация ввода
        validation_result = validate_input(guess, self.min_range, self.max_range)
        if not validation_result["valid"]:
            return validation_result
        
        # Преобразование в число и увеличение счетчика попыток
        guess_num = int(guess)
        self.attempts += 1
        
        # Проверка предположения
        if guess_num == self.secret_number:
            self.game_over = True
            return {
                "valid": True,
                "message": f"Поздравляем! Вы угадали число {self.secret_number} за {self.attempts} попыток!",
                "status": "win",
                "attempts": self.attempts
            }
        elif guess_num < self.secret_number:
            return {
                "valid": True,
                "message": "Слишком маленькое число! Попробуйте еще раз.",
                "status": "too_low",
                "attempts": self.attempts
            }
        else:
            return {
                "valid": True,
                "message": "Слишком большое число! Попробуйте еще раз.",
                "status": "too_high",
                "attempts": self.attempts
            }
    
    def get_game_state(self):
        """Получение текущего состояния игры."""
        return {
            "min_range": self.min_range,
            "max_range": self.max_range,
            "attempts": self.attempts,
            "game_over": self.game_over,
            "secret_number": self.secret_number if self.game_over else "hidden"
        }

if __name__ == "__main__":
    # Тестирование основной логики
    game = GuessTheNumberGame()
    print("Игра 'Угадай число' запущена!")
    print(f"Загадано число от {game.min_range} до {game.max_range}")
    
    while not game.game_over:
        user_input = input("Введите ваше предположение: ")
        result = game.make_guess(user_input)
        print(result["message"])
    
    print("Игра завершена!")
