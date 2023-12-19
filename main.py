import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

bot = telebot.TeleBot('6328250333:AAG9FEq5BmU39qPkoAmmuj1x7_ag0yGcHuw')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Выбор функции'))
keyboard.add(KeyboardButton('Завершить программу'))


@bot.message_handler(commands=['start'])
def show_menu(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Для работы выберите пункт главного меню:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Выбор функции')
def show_task_menu(message):
    keyboard_tasks = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_tasks.add(KeyboardButton('Любое число до 1000'))
    keyboard_tasks.add(KeyboardButton('Любая буква'))
    keyboard_tasks.add(KeyboardButton('Завершить программу'))
    bot.send_message(message.chat.id, 'Выберите задание:', reply_markup=keyboard_tasks)

@bot.message_handler(func=lambda message: message.text == 'Любое число до 1000')
def task1_handler(message):
    a = random.randint(1, 1000)
    bot.send_message(message.chat.id, a)

@bot.message_handler(func=lambda message: message.text == 'Любая буква')
def get_random_letter(message):
    # Получаем случайную букву из русского алфавита
    random_letter = random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    # Отправляем букву пользователю
    bot.send_message(message.chat.id, f"Случайная буква: {random_letter}")


# Обработка кнопки завершения программы
@bot.message_handler(func=lambda message: message.text == 'Завершить программу')
def exit_program(message):
    bot.send_message(message.chat.id, 'Программа завершена.')

def gen():
    return random.randint(1, 1000)


if __name__ == "__main__":
    bot.polling(none_stop=True)