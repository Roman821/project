import telebot
import info  # импортируем информацию о Шерлоке

# Подключаемся к боту
bot = telebot.TeleBot('6707022724:AAFSSs_Ld_2BtNKglrJTlQqSriOsldtoG-k')


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать на Бэйкер стрит 221Б. "
                          "Можете оставить заявку с помощи команды /help и в скором времени ваше дело будет раскрыто.")


# команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Доступные команды:\n"
        "/start - запуск бота\n"
        "/help - помощь\n"
        "/music - если хотите послушать скрипку"
        "Можно узнать имя, возраст, хобби, интересы и дела Шерлока."
        # Может добавлю больше информации
    )
    bot.reply_to(message, help_text)


# Шерлок хочет сыграть
@bot.message_handler(commands=['music'])
def send_audio(message):
    # Отправка аудиофайла пользователю
    with open(r'C:\Users\muhme\Desktop\Скрипка Шерлока Холмса.mp3', 'rb') as audio:
        bot.send_audio(message.chat.id, audio)


# Обработка user сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Принимаем сообщение
    user_text = message.text.lower()  # Преобразование в нижний регистр для нечувствительности к регистру

    # Проверка наличия запросов или команд
    if 'имя' in user_text or 'name' in user_text or 'как зовут детектива?' in user_text:
        bot.reply_to(message, f"Детектива зовут {info.name}.")

    elif 'возраст' in user_text or 'сколько ему лет?' in user_text or 'age' in user_text:
        bot.reply_to(message, f"На данный момент ему {info.age} лет.")

    elif 'хобби' in user_text or 'чем занимается Шерлок?' in user_text or 'hobbies' in user_text:
        bot.reply_to(message, f'В число хобби Холмса входит: {info.hobbies[0]}, {info.hobbies[1]}, {info.hobbies[2]}.')

    elif 'интересы' in user_text or 'чем интерисуется?' in user_text:
        bot.reply_to(message, f'Шерлоку Холмсу интересна {info.interests[0]} и {info.interests[1]}.')

    elif 'проекты' in user_text or 'работа' in user_text or 'над чем работает?' in user_text:
        bot.reply_to(message, f'Сейчас он занят делом под названием {info.projects[0]} и {info.projects[1]}.')

    # Можно добавить ещё инфы по желанию

    else:
        bot.reply_to(message, "Простите, я не вас не понимаю.")


# Ошибка
@bot.message_handler(content_types=['text'])
def handle_unknown(message):
    bot.reply_to(message, "Простите, я не понял. Введите /help для получения информации о доступных командах.")


# Запуск бота
if __name__ == '__main__':
    bot.polling()
