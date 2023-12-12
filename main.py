import telebot
import random
from telebot import types

bot = telebot.TeleBot('6328250333:AAG9FEq5BmU39qPkoAmmuj1x7_ag0yGcHuw')

@bot.message_handler(commands=['start', 'menu'])
def start(message):
    markup = types.ReplyKeyboardMarkup('')
    b1 = types.KeyboardButton('1 Задание', )
    markup.row(b1)
    b2 = types.KeyboardButton('2 Задание', )
    markup.row(b2)
    b3 = types.KeyboardButton('3 Задание', )
    markup.row(b3)
    bot.send_message(message.chat.id,'Здравствуйте!\n\nВыберите номер задания для выполнения:1,2 или 3', reply_markup=markup)

@bot.message_handler(commands=['command1'])
def First(message):
    bot.send_message(message.chat.id, "\nЗадание 1\n\nНахождение суммы чисел из массивов, сортировка массивов\n\n1. Ввод массивов вручную\n2. Генерация массивов автоматически\nВыберите действие: ")


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
generate = lambda length: [random.randint(1, 100) for _ in range(length)]

if __name__ == "__main__":
    bot.polling(none_stop=True)