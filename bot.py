import telebot
from telebot import types
import requests

bot = telebot.TeleBot('1452148253:AAErFQqqCavVVsv4nVxExQ-DNdyJTlewg5w')
#button1
markup_button1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bnt_book1 = types.InlineKeyboardButton("Электронные книги 📚")
btn_audio2 = types.InlineKeyboardButton("Аудиокниги 🎧")
btn_pogoda = types.InlineKeyboardButton("Погода🔮")
markup_button1.add(bnt_book1, btn_audio2, btn_pogoda)


#button2
markup_button2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_bk1 = types.InlineKeyboardButton("Классика")
btn_bk2 = types.InlineKeyboardButton("Фантастика")
btn_bk3 = types.InlineKeyboardButton("Приключения")
btn_bk4 = types.InlineKeyboardButton("Детские книги")
btn_bk5 = types.InlineKeyboardButton("Книги по психологии")
btn_bk6 = types.InlineKeyboardButton("Повести, рассказы")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_button2.add(btn_bk1, btn_bk2, btn_bk3, btn_bk4, btn_bk5, btn_bk6, btn_back)

#classic
markup_classic = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_classic1 = types.InlineKeyboardButton("Идиот. Фёдор Достоевский")
btn_classic2 = types.InlineKeyboardButton("Анна Каренина. Лев Толстой.")
btn_classic3 = types.InlineKeyboardButton("Абай жолы. Мұхтар Әуезов")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_classic.add(btn_classic1, btn_classic2, btn_classic3, btn_back)

#fan
markup_fan = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_fan1 = types.InlineKeyboardButton("Алхимик. Пауло Коэльо")
btn_fan2 = types.InlineKeyboardButton("Гарри Поттер")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_fan.add(btn_fan1, btn_fan2, btn_back)

#Истории успеха
markup_pr = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_pr1 = types.InlineKeyboardButton("Самый богатый человек в Вавилоне")
btn_pr2 = types.InlineKeyboardButton("Монарх, который продал свой Ferrari")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_pr.add(btn_fan1, btn_fan2, btn_back)

#Тайм менеджмент
markup_ch = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_ch1 = types.InlineKeyboardButton("Магия утра. Хэл Элорд")
btn_ch2 = types.InlineKeyboardButton("Мастер времени. Трейси")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_ch.add(btn_fan1, btn_fan2, btn_back)

#Книги по психологии
markup_ps = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_ps1 = types.InlineKeyboardButton("Куриный бульон для души 101 история о женщинах")
btn_ps2 = types.InlineKeyboardButton("Бывшие. Наталья Краснова")
btn_ps3 = types.InlineKeyboardButton("Сила воли")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_ps.add(btn_ps1, btn_ps2, btn_ps3, btn_back)

#Повести, рассказы
markup_rass = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_rass1 = types.InlineKeyboardButton("Балалық шаққа саяхат. Б.Соқпақбаев")
btn_rass2 = types.InlineKeyboardButton("Шұғаның белгісі. Бейімбет Майлин")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_rass.add(btn_rass1,btn_rass2, btn_back)

#audio

markup_audio = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_aud1 = types.InlineKeyboardButton("Отдельная реальность. Карлос Кастанеда")
btn_aud2 = types.InlineKeyboardButton("Магия утра")
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_audio.add(btn_aud1, btn_aud2, btn_back)


#Погода
markup_pogoda = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_pogoda1 = types.InlineKeyboardButton('Нур-Султан🏛')
btn_pogoda2 = types.InlineKeyboardButton('Алматы🏔')
btn_pogoda3 = types.InlineKeyboardButton('Семей🌉')
btn_pogoda4 = types.InlineKeyboardButton('Тараз🕌')
btn_pogoda5 = types.InlineKeyboardButton('Шымкент🎆')
btn_back = types.InlineKeyboardButton('Вернуться на главную ↩️')
markup_pogoda.add(btn_pogoda1, btn_pogoda2, btn_pogoda3, btn_pogoda4, btn_pogoda5, btn_back)

@bot.message_handler(commands=['start'])
def message_start(message):
    send_message = f"Привет,{message.from_user.first_name}!\nВыбери то, что тебя интересует. " \
                   f" 🧐\n"
    bot.send_message(message.chat.id, send_message, reply_markup=markup_button1)

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        if message.text == 'Электронные книги 📚':
            bot.send_message(message.from_user.id,"Выбери жанр",reply_markup=markup_button2)
            #классика
        elif message.text == 'Классика':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_classic)
        elif message.text == 'Идиот. Фёдор Достоевский':
            document = open("audio12.pdf",'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Анна Каренина. Лев Толстой.':
            document = open("audio13.pdf",'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Абай жолы. Мұхтар Әуезов':
            document = open("audio8.pdf",'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
           #Фантастика
        elif message.text == 'Фантастика':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_fan)
        elif message.text == 'Алхимик. Пауло Коэльо':
            document = open("audio2.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Гарри Поттер':
            document = open("audio11.pdf",'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        #Истории успеха
        elif message.text == 'Истории успеха':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_fan)
        elif message.text == 'Самый богатый человек в Вавилоне':
            document = open("audio6.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Монарх, который продал свой Ferrari':
            document = open("audio1.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        # Тайм менеджмент
        elif message.text == 'Тайм менеджмент':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_ch)
        elif message.text == 'Магия утра. Хэл Элорд':
            document = open("audio3.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Мастер времени. Трейси':
            document = open("audio14.pdf",'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        #Книги по психологии
        elif message.text == 'Книги по психологии':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_ps)
        elif message.text == 'Куриный бульон для души 101 история о женщинах':
            document = open("audio4.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Бывшие. Наталья Краснова':
            document = open("audio5.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Сила воли':
            document = open("audio7.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

        #Повести, рассказы
        elif message.text == 'Повести, рассказы':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_rass)
        elif message.text == 'Балалық шаққа саяхат. Б.Соқпақбаев':
            document = open("audio9.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        elif message.text == 'Шұғаның белгісі. Бейімбет Майлин':
            document = open("audio10.pdf", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()


        #Аудио
        elif message.text == 'Аудиокниги 🎧':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_audio)

        elif message.text == "Отдельная реальность. Карлос Кастанеда":
            audio = open(' ', 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_audio(message.from_user.id, audio)
            audio.close()

        elif message.text == "Магия утра":
            audio = open(' ', 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_audio(message.from_user.id, audio)
            audio.close()

        elif message.text == 'Вернуться на главную ↩️':
            bot.send_message(message.from_user.id, 'Выбери одну', reply_markup=markup_button1)

        #Погода
        elif message.text == 'Погода🔮':
            bot.send_message(message.from_user.id, 'Выбери город🇰🇿', reply_markup=markup_pogoda)
        elif message.text == 'Нур-Султан🏛':
            city = 'Нур-Султан'

            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?&units=metric&q=%s&appid=0c9f3c052f1d81b7062750ff0926f345' % (
                    city))
            data = r.json()
            temp = data["main"]["temp"]
            bot.send_message(message.chat.id, "Сегодня в городе: {} : \n"
                                              "температура воздуха: {} °C🌡".format(city, temp))
        elif message.text == 'Алматы🏔':
            city = 'Алматы'

            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?&units=metric&q=%s&appid=0c9f3c052f1d81b7062750ff0926f345' % (
                    city))
            data = r.json()
            temp = data["main"]["temp"]
            bot.send_message(message.chat.id, "Сегодня в городе: {} : \n"
                                              "температура воздуха: {} °C🌡".format(city, temp))
        elif message.text == 'Семей🌉':
            city = 'Семей'

            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?&units=metric&q=%s&appid=0c9f3c052f1d81b7062750ff0926f345' % (
                    city))
            data = r.json()
            temp = data["main"]["temp"]
            bot.send_message(message.chat.id, "Сегодня в городе: {} : \n"
                                              "температура воздуха: {} °C🌡".format(city, temp))
        elif message.text == 'Тараз🕌':
            city = 'Тараз'

            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?&units=metric&q=%s&appid=0c9f3c052f1d81b7062750ff0926f345' % (
                    city))
            data = r.json()
            temp = data["main"]["temp"]
            bot.send_message(message.chat.id, "Сегодня в городе: {} : \n"
                                              "температура воздуха: {} °C🌡".format(city, temp))
        elif message.text == 'Шымкент🎆':
            city = 'Шымкент'

            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?&units=metric&q=%s&appid=0c9f3c052f1d81b7062750ff0926f345' % (
                    city))
            data = r.json()
            temp = data["main"]["temp"]
            bot.send_message(message.chat.id, "Сегодня в городе: {} : \n"
                                              "температура воздуха: {} °C🌡".format(city, temp))
        else:
             bot.send_message(message.from_user.id, "Извини, я не могу ответить на это 🗿.")
        bot.polling(none_stop=True)