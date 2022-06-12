import telebot
import telegram
import random
from telebot import types
# Загружаем список интересных фактов

facts = ("Max", "Love", "Alena")

print(telebot.__file__)

# Загружаем список поговорок
thinks  = ("123", "321", "222")

def get_api(text):
    return str(text)

bot = telebot.TeleBot('5495976886:AAFg5RkCCPQ-TrCevIFO39hJDO6DJvZAxx8')

@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        item3=types.KeyboardButton("Диалоги")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка':
            answer = random.choice(thinks)
    elif message.text.strip() == 'Диалоги':
            answer = get_api(message.from_user)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer )
# Запускаем бота
bot.polling(none_stop=True, interval=0)