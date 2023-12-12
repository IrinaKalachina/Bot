import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6328250333:AAG9FEq5BmU39qPkoAmmuj1x7_ag0yGcHuw')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Выбор задания'))
keyboard.add(KeyboardButton('Завершить программу'))

@bot.message_handler(commands=['start'])
def show_menu(message):
    bot.send_message(message.chat.id, 'Главное меню:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Выбор задания')
def show_task_menu(message):
    keyboard_tasks = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_tasks.add(KeyboardButton('Задание 1'))
    keyboard_tasks.add(KeyboardButton('Задание 2'))
    keyboard_tasks.add(KeyboardButton('Задание 3'))
    bot.send_message(message.chat.id, 'Выберите задание:', reply_markup=keyboard_tasks)

@bot.message_handler(func=lambda message: message.text == 'Задание 1')
def task1_handler(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    item_manual = telebot.types.KeyboardButton('1. Ввод вручную')
    item_auto = telebot.types.KeyboardButton('2. Генерация автоматически')
    markup.add(item_manual, item_auto)

    msg = bot.send_message(message.chat.id, "Выберите способ заполнения массивов:", reply_markup=markup)
    bot.register_next_step_handler(msg, task_1_step)

def task_1_step(message):
    if message.text == '1':
        arr1 = parse_input(input("Введите первый массив чисел через пробел: "))
        arr2 = parse_input(input("Введите второй массив чисел через пробел: "))
        if len(arr1) != len(arr2):
            bot.send_message(message.chat.id, "Массивы разной длины. Введите массивы одной длины.")
            return
    elif message.text == '2':
        n = int(input('Введите количество элементов массива: '))
        arr1 = generate(n)
        arr2 = generate(n)
        bot.send_message(message.chat.id, f'Массив 1:\n{arr1}\nМассив 2:\n{arr2}')
    else:
        bot.send_message(message.chat.id, "Неверный выбор. Пожалуйста, выберите пункт меню 1 или 2.")
        return

    result = [arr1[i] + arr2[i] if arr1[i] != arr2[i] else 0 for i in range(len(arr1))]
    bot.send_message(message.chat.id,
                     f"Результат:\n{sorted(result)}\nПервый массив, отсортированный по убыванию:\n{sorted(arr1, reverse=True)}\nВторой массив, отсортированный по возрастанию:\n{sorted(arr2)}")

@bot.message_handler(func=lambda message: message.text == 'Задание 2')
def task2_handler(message):
    # Ваш код для задания 2
    pass

@bot.message_handler(func=lambda message: message.text == 'Задание 3')
def task3_handler(message):
    # Ваш код для задания 3
    pass

# Обработка кнопки завершения программы
@bot.message_handler(func=lambda message: message.text == 'Завершить программу')
def exit_program(message):
    bot.send_message(message.chat.id, 'Программа завершена.')

    """
@bot.message_handler(commands=['1'])
def One(message):
    bot.send_message(message.chat.id, "Введите первый массив чисел через пробел: ")
    @bot.message_handler()
    def Massiv1(massiv):
        arr1 = str(massiv.text)
        bot.send_message(message.chat.id, "Введите второй массив чисел через пробел: ")
        @bot.message_handler()
        def Massiv2(mass):
            arr2 = str(mass.text)
            if len(arr1) != len(arr2):
                bot.send_message(message.chat.id, "Массивы разной длины. Введите массивы одной длины.")
            return arr2
        return arr1
    result = [int(arr1[i]) + int(arr2[i]) if int(arr1[i]) != int(arr2[i]) else 0 for i in range(len(arr1))]
    bot.send_message(message.chat.id, f"Результат: {sorted(result)} \nПервый массив, отсортированный по убыванию: {sorted(arr1, reverse=True)}\nВторой массив, отсортированный по возрастанию: {sorted(arr2)}")
"""
@bot.message_handler(commands=['2'])
def Two(message):
    bot.send_message(message.chat.id, 'Введите количество элементов массива: ')
    @bot.message_handler()
    def Elements(message):
        length = int(message.text)

        arr1 = generate(length)
        arr2 = generate(length)

        result = [int(arr1[i]) + int(arr2[i]) if int(arr1[i]) != int(arr2[i]) else 0 for i in range(len(arr1))]
        bot.send_message(message.chat.id, f'Массив 1:\n{arr1}\nМассив 2:\n{arr2}\nРезультат:\n{sorted(result)} \nПервый массив, отсортированный по убыванию: \n{sorted(arr1, reverse=True)}\nВторой массив, отсортированный по возрастанию: \n{sorted(arr2)}')


# Функция для генерации массива случайных чисел
generate = lambda length: [random.randint(1, 100) for _ in range(length)]  # Включение в последовательность

# Преобразование строки в список целых чисел
parse_input = lambda input_str: list(map(int, input_str.split()))

if __name__ == "__main__":
    bot.polling(none_stop=True)