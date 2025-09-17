"""
Модуль графического интерфейса для игры "Угадай число".
Использует библиотеку tkinter для создания GUI.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from main import GuessTheNumberGame

class GuessTheNumberGUI:
    """Класс для создания графического интерфейса игры."""
    
    def __init__(self):
        """Инициализация графического интерфейса."""
        self.game = GuessTheNumberGame()
        self.setup_gui()
    
    def setup_gui(self):
        """Настройка основных элементов интерфейса."""
        # Создание главного окна
        self.root = tk.Tk()
        self.root.title("Угадай число")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Настройка стилей
        self.setup_styles()
        
        # Создание элементов интерфейса
        self.create_widgets()
        
        # Обновление информации о игре
        self.update_game_info()
    
    def setup_styles(self):
        """Настройка стилей для элементов интерфейса."""
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10))
        style.configure("Header.TLabel", font=("Arial", 14, "bold"))
    
    def create_widgets(self):
        """Создание всех виджетов интерфейса."""
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Заголовок
        header_label = ttk.Label(
            main_frame, 
            text="🎯 Угадай число", 
            style="Header.TLabel"
        )
        header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Информация о игре
        self.info_label = ttk.Label(
            main_frame, 
            text="", 
            wraplength=400
        )
        self.info_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Поле для ввода
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=2, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(input_frame, text="Ваше предположение:").grid(row=0, column=0)
        
        self.guess_entry = ttk.Entry(input_frame, width=10, font=("Arial", 12))
        self.guess_entry.grid(row=0, column=1, padx=(10, 5))
        self.guess_entry.bind("<Return>", lambda event: self.on_guess())
        
        guess_button = ttk.Button(
            input_frame, 
            text="Угадать", 
            command=self.on_guess
        )
        guess_button.grid(row=0, column=2, padx=(5, 0))
        
        # Область для вывода результата
        self.result_text = tk.Text(
            main_frame, 
            height=8, 
            width=50, 
            font=("Arial", 10),
            state=tk.DISABLED
        )
        self.result_text.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        # Кнопки управления
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2)
        
        self.restart_button = ttk.Button(
            button_frame, 
            text="Новая игра", 
            command=self.on_restart,
            state=tk.NORMAL
        )
        self.restart_button.grid(row=0, column=0, padx=(0, 10))
        
        exit_button = ttk.Button(
            button_frame, 
            text="Выход", 
            command=self.root.quit
        )
        exit_button.grid(row=0, column=1)
    
    def update_game_info(self):
        """Обновление информации о текущей игре."""
        state = self.game.get_game_state()
        info_text = (
            f"Диапазон чисел: от {state['min_range']} до {state['max_range']}\n"
            f"Попыток: {state['attempts']}\n"
            f"Статус: {'Игра завершена' if state['game_over'] else 'Игра продолжается'}"
        )
        self.info_label.config(text=info_text)
    
    def append_result(self, text):
        """Добавление текста в область результатов."""

        self.result_text.config(state=tk.NORMAL)
        self.result_text.insert(tk.END, text + "\n")
        self.result_text.see(tk.END)
        self.result_text.config(state=tk.DISABLED)
    
    def on_guess(self):
        """Обработка события угадывания числа."""
        guess = self.guess_entry.get()
        if not guess:
            messagebox.showwarning("Внимание", "Пожалуйста, введите число")
            return
        
        result = self.game.make_guess(guess)
        
        if not result["valid"]:
            messagebox.showerror("Ошибка", result["message"])
            return
        
        self.append_result(f"Попытка {result['attempts']}: {guess} - {result['message']}")
        self.guess_entry.delete(0, tk.END)
        self.update_game_info()
        
        if result["status"] == "win":
            self.restart_button.config(state=tk.NORMAL)
            messagebox.showinfo("Поздравляем!", result["message"])
    
    def on_restart(self):
        """Обработка события начала новой игры."""
        self.game.reset_game()
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
        self.update_game_info()
        self.restart_button.config(state=tk.DISABLED)
        self.append_result("=== Новая игра началась ===")
    
    def run(self):
        """Запуск главного цикла приложения."""
        self.root.mainloop()

def main():
    """Основная функция для запуска GUI."""
    app = GuessTheNumberGUI()
    app.run()

if __name__ == "__main__":
    main()
